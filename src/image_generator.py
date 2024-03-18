from selenium import webdriver
from reddit_request import Reddit_Request
import os
from dotenv import load_dotenv
from PIL import Image

class Reddit_Image_Generator:
    def __init__(self, url, username, password, client_id, secret_token):
        self.username = username
        self.password = password
        self.client_id = client_id
        self.secret_token = secret_token
        self.url = url
        self.image = None
        self.cropped_image = None

    def generate_image(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        driver.save_screenshot('../assets/screenshots/screenshot.png')
        self.image = Image.open('../assets/screenshots/screenshot.png')
        return self.image.show()

    def crop_image(self):
        self.generate_image()
        left, right, top, bottom = 260, 870, 60, 281 # manually calculated values
        if (self.image):
            cropped_image = self.image.crop((left, top, right, bottom))
            return cropped_image.show()
        return None

load_dotenv()

USERNAME = os.environ.get('USERNAME') 
PASSWORD = os.environ.get('PASSWORD')
CLIENT_ID = os.environ.get('CLIENTID')
SECRET_TOKEN = os.environ.get('SECRET_TOKEN')

rq = Reddit_Request(USERNAME, PASSWORD, CLIENT_ID, SECRET_TOKEN)
rq.search_subreddit("Showerthoughts")

url = rq.get_dataframe_row(10)['url'] # TODO: get random row based on highest upvote ratio

ig = Reddit_Image_Generator(url, USERNAME, PASSWORD, CLIENT_ID, SECRET_TOKEN)
ig.crop_image()


