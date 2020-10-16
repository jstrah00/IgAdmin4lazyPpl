from selenium import webdriver
import time
import requests

class IgLazyBot():
    def __init__(self):
        import local_settings
        self.ig_username = local_settings.ig_username
        self.ig_password = local_settings.ig_password
        self.webdriver_path = "chromedriver"
        self.ig_base_url = "https://www.instagram.com/"


    def start_driver(self):
        self.driver = webdriver.Chrome(self.webdriver_path)

    def login_instagram(self):
        self.driver.get(self.ig_base_url + "accounts/login/")
        self.driver.find_element_by_name("username").send_keys(self.ig_username)
        self.driver.find_element_by_name("password").send_keys(self.ig_password)
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(4)

    def download_images(self, url_list):
        pass

    def get_images(self):
        self.start_driver()
        self.login_instagram()
