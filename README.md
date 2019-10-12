<p align="center"><img src="https://raw.githubusercontent.com/anfederico/Flaskex/master/media/flaskex-logo.png" width="128px"><p>

 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
 ![Python](https://img.shields.io/badge/python-v3.6-blue.svg)
 ![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)
 [![GitHub Issues](https://img.shields.io/github/issues/anfederico/flaskex.svg)](https://github.com/anfederico/flaskex/issues)
 ![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)
 [![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
 [![Codacy Badge](https://api.codacy.com/project/badge/Grade/ef2f8f65c67a4043a9362fa6fb4f487a)](https://www.codacy.com/app/RDCH106/Flaskex?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=RDCH106/Flaskex&amp;utm_campaign=Badge_Grade)

 <br><br>

 <p align="center"><img src="https://raw.githubusercontent.com/anfederico/Flaskex/master/media/flaskex-demo.png" width="100%"><p>

## Introduction
DocHat is an integrated medical chatbot web app. DocHat uses:
- Flaskex framework for the web design's prototype
- Stripe for integrated payment solution
- Dialogflow for chatbot application
- Messenger-like chat interface

## Setup
DocHat has been tested with Python 3.6 or 3.7. Run the commands below to setup your environment.
``` 
git clone https://github.com/SaAPro/DocHat
cd DocHat
pip install -r requirements.txt
python app.py
```
Open the folowing url http://127.0.0.1:5000/ in your favorite navigator and you are done !

## How to use the web app
- Start by signing up
- On the payment page, copy the card number and click on pay. It will send you on the dedicated checkout Stripe servers
- Give an email, the card n° 4242 4242 4242 4242 and arbitrary mm/yy, CVC and name
- After payment, you will be redirected to the chatbot interface
- You can start chatting with your personnal chatbot doctor !

## Note
This is an on-going work. The Dialogflow agent has been developped for the web app prototype and is not complete.
