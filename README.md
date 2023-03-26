# Web Scraping Twitter by Key-words and Accounts

This code **<a href="https://github.com/ergoncugler/web-scraping-twitter-by-key-words-and-accounts/blob/main/web-scraping-twitter.py">[code here]</a>** aims to **scrape data** from Twitter, it can be a key-word or an account. It uses the Tweepy Library, also integrating Google's Gspread Library **and printing the results in a Google Spreadsheet at once**.

In summary, it is possible to to scrape all the desired content, returning: **'Scraping ID', 'Tweet ID', 'Date', 'Username', 'Followers ', 'Location', 'Retweet', 'Text', 'Retweet', 'Favorite', 'Hashtags', 'Mentions', 'Urls'** for each tweet.

### Output Example:
It was asked to scrape 50 tweets using the key-word "Lula" in english, then it returned:
![image](https://user-images.githubusercontent.com/81989837/227799797-e333cbaa-4257-40fe-94b6-7c92edda0f6f.png)

___

## !Pip Before Coding

```python
pip install tweepy
```
```python
pip install gspread
```

___

## Run the Code (03 easy steps! Just your first run!)

### Just First Time:

**01.)** It should ask you 'allow this laptop to access your Google credentials?' This will allow code running on this notebook to access your Google Drive and Google Cloud data. Review the code before allowing access. Put ir 'Allow':

![image](https://user-images.githubusercontent.com/81989837/219951620-9f939108-2660-4965-8744-e8429cd867fb.png)

**02.)** Choose an account to proceed to Collaboratory Runtimes. To continue, Google will share your name, email address, preferred language, and profile picture with the Collaboratory Runtimes app. Please review the Collaboratory Runtimes app's Privacy Policy and Terms of Service before using it:

![image](https://user-images.githubusercontent.com/81989837/219951831-c2ff8a85-7076-414f-8a5a-aadd8f59ad99.jpg)

**03.)** Use your credentials here:

***Attention: If you don't have the necessary credentials, you can create it for free on the official Telegram for Developers website: https://developer.twitter.com/. There you can get your 'consumer key' and 'acess token'.***

```python
# tweepy credentials
consumer_key = ('*************************')                                # your consumer key / get it: https://developer.twitter.com/
consumer_secret = ('**************************************************')    # your consumer key secret / get it: https://developer.twitter.com/
access_token = ('**************************************************')       # your acess token / get it: https://developer.twitter.com/
access_token_secret = ('*********************************************')     # your acess token secret / get it: https://developer.twitter.com/
```

**And that's it!**

### To Scrape Profiles:

```python
# tweets from a profile
extract_profile_tweets(
    twitter_user = 'jairbolsonaro',       # don't need @, just username
    worksheet_name = 'your_worksheet',    # it will be created in your Drive
    include_retweets = False)             # just use True or False without ""
```

**Done? You can run it! And it will be like:**

![image](https://user-images.githubusercontent.com/81989837/227799750-1ff8731a-d6e1-4879-8301-0190af6b9bc9.png)

### To Scrape Key-words:

```python
# tweets from a string
extract_topic_tweets(
    count = 50,                           # how many tweets you want
    text_query = 'lula',                  # the term you want to search
    lang = 'en',                          # 'en', 'pt', 'es' and others
    result_type = 'recent',               # 'recent', 'popular', or 'mix'
    worksheet_name = 'your_worksheet')    # it will be created in your Drive
```

**Done? You can run it! And it will be like:**

![image](https://user-images.githubusercontent.com/81989837/227799797-e333cbaa-4257-40fe-94b6-7c92edda0f6f.png)

## More About:

### [Data] [Academic Research] [Scientific Research] [Public Policy] [Political Science] [Data Science]

Its use is highly encouraged and recommended for academic and scientific research, content analysis, sentiment and speech. It is free and open, and academic use is encouraged. Its responsible use is the sole responsibility of those who adapt and manipulate the data.

___

## Author Info:

Ergon Cugler de Moraes Silva, from Brazil, mailto: <a href="contato@ergoncugler.com">contato@ergoncugler.com</a> / Master's Program in Public Administration and Government, Getulio Vargas Foundation (FGV) / Funded Researcher by the National Council for Scientific and Technological Development (CNPq) / Center of Bureaucratic Studies (NEB) / Núcleo de Estudos da Burocracia (NEB).

### How to Cite it:

**SILVA, Ergon Cugler de Moraes. Web Scraping Twitter by Key-words and Accounts. (mar) 2023. Avaliable at: <a>https://github.com/ergoncugler/web-scraping-twitter-by-key-words-and-accounts/<a>.**
