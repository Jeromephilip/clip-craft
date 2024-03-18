import requests
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

# environment vars
USERNAME = os.environ.get('USERNAME') 
PASSWORD = os.environ.get('PASSWORD')
CLIENT_ID = os.environ.get('CLIENTID')
SECRET_TOKEN = os.environ.get('SECRET_TOKEN')

# note that CLIENT_ID refers to 'personal use script' and SECRET_TOKEN to 'token'
auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_TOKEN)

# here we pass our login method (password), username, and password
data = {'grant_type': 'password',
        'username': USERNAME,
        'password': PASSWORD}

# setup our header info, which gives reddit a brief description of our app
headers = {'User-Agent': 'MyBot/0.0.1'}

# send our request for an OAuth token
res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers) # gets access token for requests.

# convert response to JSON and pull access_token value
TOKEN = res.json()['access_token']

# add authorization to our headers dictionary
headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)

res = requests.get("https://oauth.reddit.com/r/Showerthoughts", headers=headers)

data = res.json()

df = pd.DataFrame()

for post in data['data']['children']:
    new_data = {'subreddit': post['data']['subreddit'],
                'title': post['data']['title'],
                'selftext': post['data']['selftext'],
                'upvote_ratio': post['data']['upvote_ratio'],
                'ups': post['data']['ups'],
                'downs': post['data']['downs'],
                'score': post['data']['score']}
    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
# print(df)


