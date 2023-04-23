import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import os
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class WebScraper:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self, CARD, PASSWORD):
        # Navigate to the TD EasyWeb website
        self.driver.get("https://authentication.td.com/uap-ui/?consumer=easyweb&locale=en_CA#/uap/login")
        time.sleep(1)

        # Find the username input field, enter the username, and submit the form
        username_field = self.driver.find_element("id", "username")
        username_field.send_keys(CARD)
        password_field = self.driver.find_element("id", "uapPassword")
        password_field.send_keys(PASSWORD)
        button = self.driver.find_element("xpath", '//button[contains(@class, "td-button-secondary")]')
        button.click()

        # Check if login was successful
        if "EasyWeb" in self.driver.title:
            # Logged in successfully
            return True
        else:
            # Login failed
            return False