import requests
import pandas as pd
from datetime import datetime, timedelta

class Reddit_Request:
    def __init__(self, username, password, client_id, secret_token):
        self.username = username
        self.password = password
        self.client_id = client_id
        self.secret_token = secret_token
        self.access_token = None
        self.headers = None
        self.df = pd.DataFrame()
        self.get_access_token()
        self.search_subreddit("Showerthoughts")

    def get_access_token(self):
        auth = requests.auth.HTTPBasicAuth(self.client_id, self.secret_token)

        data = {'grant_type': 'password',
                'username': self.username,
                'password': self.password}

        headers = {'User-Agent': 'MyBot/0.0.1'}

        res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)

        self.access_token = res.json()['access_token']

        self.headers = {**headers, **{'Authorization': f"bearer {self.access_token}"}}

    def search_subreddit(self, subreddit):
        time_frame = datetime.now() - timedelta(days=30) # last 30 days
        res = requests.get("https://oauth.reddit.com/r/%s" % subreddit, headers=self.headers, params={'limit': 100})
        
        for post in res.json()['data']['children']:
            post_time = datetime.fromtimestamp(post['data']['created_utc'])
            if (post_time > time_frame):
                new_data = {'id': post['data']['id'],
                            'subreddit': post['data']['subreddit'],
                            'title': post['data']['title'],
                            'url': post['data']['url'],
                            'upvote_ratio': post['data']['upvote_ratio'],
                            'created_utc': datetime.fromtimestamp(post['data']['created_utc'])}
                self.df = pd.concat([self.df, pd.DataFrame([new_data])], ignore_index=True)

        self.df = self.df.sort_values('created_utc')
    
    def get_dataframe(self):
        return self.df

    def get_dataframe_row(self, index):
        get_row = self.df.iloc[index]
        return get_row
    
    def get_highest_upvoted_story(self):

        highest_upvoted_story_data = { 'upvote_ratio': 0, 
                                      'title': None, 
                                      'url': None }

        for index, row in self.df.iterrows():
            # print(row['title'], ' ----> ', row['upvote_ratio'])
            if row['upvote_ratio'] > highest_upvoted_story_data['upvote_ratio']:
                highest_upvoted_story_data['upvote_ratio'] = row['upvote_ratio']
                highest_upvoted_story_data['title'] = row['title']
                highest_upvoted_story_data['url'] = row['url']

        return highest_upvoted_story_data
        


