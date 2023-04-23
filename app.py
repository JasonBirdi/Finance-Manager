from flask import Flask, render_template
from webscrape import WebScraper
import os
from dotenv import load_dotenv

# Use config file for login credentials
sensitive_info_path = os.environ.get('Sensitive_Info_Folder')
dotenv_path = os.path.join(sensitive_info_path, 'Finance Manager\.env')
load_dotenv(dotenv_path)

CARD = os.getenv('CARD')
PASSWORD = os.getenv('PASSWORD')

app = Flask(__name__)

@app.route('/')
def index():
    scraper = WebScraper()
    output = scraper.login(CARD, PASSWORD)
    print(output)
    return render_template('index.html')
    

if __name__ == '__main__':
    app.run()
