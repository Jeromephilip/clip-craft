from reddit_request import Reddit_Request
from image_generator import Reddit_Image_Generator
from text_to_speech import speak
from dotenv import load_dotenv
import os

class Video_Editor:
    def __init__(self, username, password, client_id, secret_token):
        self.rq = Reddit_Request(username, password, client_id, secret_token)
        self.df = self.rq.get_dataframe()

    def create_tts(self):
        title = self.rq.get_highest_upvoted_story()
        speak(title)

        return title
    

load_dotenv()

USERNAME = os.environ.get('USERNAME') 
PASSWORD = os.environ.get('PASSWORD')
CLIENT_ID = os.environ.get('CLIENTID')
SECRET_TOKEN = os.environ.get('SECRET_TOKEN')

ve = Video_Editor(USERNAME, PASSWORD, CLIENT_ID, SECRET_TOKEN)

print(ve.create_tts())

    