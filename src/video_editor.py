from reddit_request import Reddit_Request
from image_generator import Reddit_Image_Generator
from text_to_speech import speak
from dotenv import load_dotenv
import os

class Video_Editor:
    def __init__(self, username, password, client_id, secret_token):
        self.r_req = Reddit_Request(username, password, client_id, secret_token)
        self.df = self.r_req.get_dataframe()
        self.r_image = None # image instance
        self.reddit_story_data = None

    def create_tts(self):
        self.reddit_story_data = self.r_req .get_highest_upvoted_story()
        speak(self.reddit_story_data['title'])
        return self.reddit_story_data 

    def get_reddit_image(self):
        if (self.reddit_story_data):
            self.r_image = Reddit_Image_Generator(self.reddit_story_data['url'])
            self.r_image.crop_image()
    

load_dotenv()

USERNAME = os.environ.get('USERNAME') 
PASSWORD = os.environ.get('PASSWORD')
CLIENT_ID = os.environ.get('CLIENTID')
SECRET_TOKEN = os.environ.get('SECRET_TOKEN')

ve = Video_Editor(USERNAME, PASSWORD, CLIENT_ID, SECRET_TOKEN)

print(ve.create_tts())
ve.get_reddit_image()

    