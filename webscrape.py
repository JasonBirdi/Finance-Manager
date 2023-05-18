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
    def __init__(self, login_timer):
        self.login_timer = login_timer
        self.driver = webdriver.Chrome()
        self.login_status = False
    
    def login(self):
        self.driver.get("https://authentication.td.com/uap-ui/?consumer=easyweb&locale=en_CA#/uap/login")

        for i in range(self.login_timer-4):
            time.sleep(1)
            print("Timer: " + str(self.login_timer-4 - i))

        if self.driver.current_url == "https://easyweb.td.com/waw/ezw/webbanking":
            self.login_status = True
        else:
            self.login_status = False

    def scrape_accounts(self):
        self.driver.get("https://easyweb.td.com/waw/ezw/webbanking")
        page_source = self.driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        account_info = {}
        total_account = soup.find('td', {'class': 'td-copy-align-right td-table-border-top-mediumgrey'})
        account_info['account_totals'] = total_account
        account_names = soup.find_all("a", class_="td-link-standalone td-link-standalone-secondary")
        account_amounts = soup.find_all("td", class_="td-copy-align-right")
        for i in range(len(account_names)):
            account_info[account_names[i].text] = account_amounts[i].text
        print(account_info)
        return account_info
