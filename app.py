from flask import Flask, render_template
from webscrape import WebScraper
from credentials import Credentials
import os
from dotenv import load_dotenv
import threading

# Use config file for login credentials
sensitive_info_path = os.environ.get('Sensitive_Info_Folder')
dotenv_path = os.path.join(sensitive_info_path, 'Finance Manager\.env')
load_dotenv(dotenv_path)

CARD = os.getenv('CARD')
PASSWORD = os.getenv('PASSWORD')
LOGIN_TIMER = os.getenv('LOGIN_TIMER')
LOGIN_TIMER = int(LOGIN_TIMER)

app = Flask(__name__)

@app.route('/')
def index():
    credentials = Credentials(CARD, PASSWORD, LOGIN_TIMER)
    scraper = WebScraper(LOGIN_TIMER)

    # create a separate thread for scraper
    scraper_thread = threading.Thread(target=scraper.login)
    scraper_thread.start()

    # run tkinter in the main thread for credential GUI
    credentials.display_credentials()

    # join scraper thread to wait for it to finish
    scraper_thread.join()

    if scraper.login_status:
        account_info = scraper.scrape_accounts()
        return render_template('index.html', account_info=account_info)
    else:
        return render_template('login_failed.html')
    
if __name__ == '__main__':
    app.run()
