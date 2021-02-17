from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import requests
import json
from selenium import webdriver
import os, sys
from config import *


app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db'

db = SQLAlchemy(app)

class Pull(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    log_path = db.Column(db.String(100))
    image_path = db.Column(db.String(100))
    date_created = db.Column(db.DateTime, default=datetime.now)



## Assume this method runs on trigger for every pull request ##
@app.route('/')
def index():
    response = requests.get("https://api.github.com/repos/{}/{}/pulls".format(REPO_OWNER, REPO_NAME)).content
    urls = [(i+1, json.loads(response)[i]['html_url']) for i in range(len(json.loads(response)))]

    for idx, url in urls:
        screenshot_path = "{}/{}.png".format(SCREENSHOT_PATH, idx)
        log_path = "{}/{}.json".format(LOGS_PATH, idx)
        if os.path.exists(log_path):
            continue

        with open(log_path, 'a') as log_file:
            log_file.write(str(response[idx-1]))

        #driver = webdriver.Chrome('./chromedriver')
        #driver.get(url)
        #driver.save_screenshot(screenshot_path)
        #sleep(2)
        #driver.quit()

        pull_request = Pull(log_path=log_path, image_path=screenshot_path)
        db.session.add(pull_request)
        db.session.commit()

    return str(urls)
