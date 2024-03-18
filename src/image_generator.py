from selenium import webdriver
from reddit_request import Reddit_Request
import os
from dotenv import load_dotenv
from PIL import Image

driver = webdriver.Chrome()

load_dotenv()

USERNAME = os.environ.get('USERNAME') 
PASSWORD = os.environ.get('PASSWORD')
CLIENT_ID = os.environ.get('CLIENTID')
SECRET_TOKEN = os.environ.get('SECRET_TOKEN')

rq = Reddit_Request(USERNAME, PASSWORD, CLIENT_ID, SECRET_TOKEN)
rq.search_subreddit("Showerthoughts")

url = rq.get_dataframe_row(2)['url']

driver.get(url)

driver.save_screenshot('../assets/screenshots/screenshot.png')

image = Image.open('../assets/screenshots/screenshot.png')

image.show()

