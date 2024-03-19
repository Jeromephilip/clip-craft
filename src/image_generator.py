from selenium import webdriver
from reddit_request import Reddit_Request
import os
from dotenv import load_dotenv
from PIL import Image

class Reddit_Image_Generator:
    def __init__(self, url):
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
            cropped_image.save('../assets/screenshots/cropped_image.png')
            return cropped_image.show()
        return None

