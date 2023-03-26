# initial libraries
from datetime import datetime, timezone
from datetime import datetime as dt
import pandas as pd
import warnings
import tweepy
import string
import time

# libraries from google
from google.colab import auth
auth.authenticate_user()
import gspread
from gspread_dataframe import set_with_dataframe
from google.auth import default
creds, _ = default()
autoriza = gspread.authorize(creds)

# collapse_show
warnings.filterwarnings('ignore')
pd.set_option('display.max_colwidth', -1)

# header
titulos = ['Scraping ID',
          'Tweet ID',
          'Date',
          'Username',
          'Followers',
          'Location',
          'Retweet',
          'Text',
          'Retweet',
          'Favorite',
          'Hashtags',
          'Mentions',
          'Urls']

str_titulos = list(string.ascii_uppercase[len(titulos)-1])

# tweepy credentials
consumer_key = ('*************************')                                # your consumer key / get it: https://developer.twitter.com/
consumer_secret = ('**************************************************')    # your consumer key secret / get it: https://developer.twitter.com/
access_token = ('**************************************************')       # your acess token / get it: https://developer.twitter.com/
access_token_secret = ('*********************************************')     # your acess token secret / get it: https://developer.twitter.com/

# accessing twitter api
auth=tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token=(access_token, access_token_secret)
api= tweepy.API(auth, wait_on_rate_limit= True)

# getting text from a profile
def extract_profile_tweets(twitter_user: str, worksheet_name = 'webscraping_twitter', include_retweets = True):
  index = 1
  tweets = []
  new_tweets = api.user_timeline(screen_name=twitter_user, count=200, tweet_mode='extended')
  tweets.extend(new_tweets)
  oldest_tweet = tweets[-1].id - 1

  # try to open the worksheet in your google drive
  try:
      sheet = autoriza.open(worksheet_name).sheet1

      # the spreadsheet already exists, you don't need to create another one
  except gspread.exceptions.SpreadsheetNotFound:

      # the spreadsheet does not exist yet, create a new one
      sh = autoriza.create(worksheet_name)
  sheet = autoriza.open(worksheet_name).sheet1

  # clear the worksheet completely before filling
  sheet.clear()
  campos = sheet.range(f'A1:{str_titulos[0]}1')
  for i in range(0, len(campos)):
    campos[i].value = titulos[i]
  sheet.update_cells(campos)

  # starts to fill it
  while len(new_tweets) > 0:
    new_tweets = api.user_timeline(screen_name=twitter_user, count=200, max_id=oldest_tweet, tweet_mode='extended', include_rts = include_retweets)
    tweets.extend(new_tweets)
    oldest_tweet = tweets[-1].id - 1
  
  profile_tweet_list = []
  for tweet in tweets:

    hashtags = str(tweet.entities['hashtags']).replace("{", "").replace("}", "").replace("[", "").replace("]", "").replace("'", "")
    mentions = str(tweet.entities['user_mentions']).replace("{", "").replace("}", "").replace("[", "").replace("]", "").replace("'", "")
    urls = str(tweet.entities['urls']).replace("{", "").replace("}", "").replace("[", "").replace("]", "").replace("'", "")

    if 'retweeted_status' in tweet._json:
        tweet_full = tweet._json['retweeted_status']['full_text']
        is_retweet = True
    else:
        tweet_full = tweet.full_text
        is_retweet = False

    profile_tweet_list.append([f'#ID{index:05}',
                str(tweet.id),
                tweet.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                f'@{tweet.user.screen_name}',
                tweet.user.followers_count,
                tweet.user.location,
                is_retweet,
                tweet_full,
                tweet.retweet_count,
                tweet.favorite_count,
                hashtags,
                mentions,
                urls]
      )

    # update loop parameters
    index = index + 1

  # end
  print(f'----------------------------------------\n#Concluded! #{index-1:05} posts were scraped!\n----------------------------------------')

  df_profile = pd.DataFrame(profile_tweet_list, columns = titulos)

  profile_tweets_list = df_profile.values.tolist()
  sheet.append_rows(profile_tweets_list)
  
  
  # getting text from a search string
def extract_topic_tweets(count: int, text_query: str, lang: str, result_type = 'recent', worksheet_name = 'webscraping_twitter'):
  index = 1
  tweets = []

  # try to open the worksheet in your google drive
  try:
      sheet = autoriza.open(worksheet_name).sheet1

      # the spreadsheet already exists, you don't need to create another one
  except gspread.exceptions.SpreadsheetNotFound:

      # the spreadsheet does not exist yet, create a new one
      sh = autoriza.create(worksheet_name)
  sheet = autoriza.open(worksheet_name).sheet1

  # clear the worksheet completely before filling
  sheet.clear()
  campos = sheet.range(f'A1:{str_titulos[0]}1')
  for i in range(0, len(campos)):
    campos[i].value = titulos[i]
  sheet.update_cells(campos)

  # starts to fill it
  tweets = tweepy.Cursor(api.search_tweets, q = text_query, tweet_mode = "extended", lang = lang, result_type = result_type).items(count)

  # getting the information from twitter object
  string_tweet_list = []
  for tweet in tweets:

    hashtags = str(tweet.entities['hashtags']).replace("{", "").replace("}", "").replace("[", "").replace("]", "").replace("'", "")
    mentions = str(tweet.entities['user_mentions']).replace("{", "").replace("}", "").replace("[", "").replace("]", "").replace("'", "")
    urls = str(tweet.entities['urls']).replace("{", "").replace("}", "").replace("[", "").replace("]", "").replace("'", "")

    if 'retweeted_status' in tweet._json:
        tweet_full = tweet._json['retweeted_status']['full_text']
        is_retweet = True
    else:
        tweet_full = tweet.full_text
        is_retweet = False
    
    string_tweet_list.append([f'#ID{index:05}',
                  str(tweet.id),
                  tweet.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                  f'@{tweet.user.screen_name}',
                  tweet.user.followers_count,
                  tweet.user.location,
                  is_retweet,
                  tweet_full,
                  tweet.retweet_count,
                  tweet.favorite_count,
                  hashtags,
                  mentions,
                  urls]
    )

    # update loop parameters
    index = index + 1

  # end
  print(f'----------------------------------------\n#Concluded! #{index-1:05} posts were scraped!\n----------------------------------------')
    
  df_string = pd.DataFrame(string_tweet_list, columns = titulos)

  string_tweets_list = df_string.values.tolist()
  sheet.append_rows(string_tweets_list)
  
  
### RUN IT 01 ###

# tweets from a profile
extract_profile_tweets(
    twitter_user = 'jairbolsonaro',       # don't need @, just username
    worksheet_name = 'your_worksheet',    # it will be created in your Drive
    include_retweets = False)             # just use True or False without ""

### RUN IT 02 ###

# tweets from a string
extract_topic_tweets(
    count = 50,                           # how many tweets you want
    text_query = 'lula',                  # the term you want to search
    lang = 'en',                          # 'en', 'pt', 'es' and others
    result_type = 'recent',               # 'recent', 'popular', or 'mix'
    worksheet_name = 'your_worksheet')    # it will be created in your Drive
