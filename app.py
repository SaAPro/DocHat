#!/usr/bin/python3.6.8
# -*- coding: utf-8 -*-

from scripts import tabledef
from scripts import forms
from scripts import helpers
from flask import Flask, redirect, url_for, render_template, request, session
import json
import sys
import os
import random

app = Flask(__name__)
app.secret_key = os.urandom(12)  # Generic key for dev purposes only

import stripe
stripe.api_key = 'sk_test_C6iVFB1rpk66QFoAe8kUtgBu00QwYSHcuX'

import dialogflow_v2 as dialogflow
from google.oauth2 import service_account
credentials = service_account.Credentials.from_service_account_file('credentials/newagent-bvcpok-2cfb831cdd63.json')
project_id = 'newagent-bvcpok'
session_id = random.randrange(999999999)
language_code = 'en-US'
session_client = dialogflow.SessionsClient(credentials=credentials)
session_dialogflow = session_client.session_path(project_id, session_id)

# ======== Routing =========================================================== #
# -------- Login ------------------------------------------------------------- #
@app.route('/', methods=['GET', 'POST'])
def login():
	if not session.get('logged_in'):
		form = forms.LoginForm(request.form)
		if request.method == 'POST':
			username = request.form['username'].lower()
			password = request.form['password']
			if form.validate():
				if helpers.credentials_valid(username, password):
					session['logged_in'] = True
					session['username'] = username
					return json.dumps({'status': 'Login successful'})
				return json.dumps({'status': 'Invalid user/pass'})
			return json.dumps({'status': 'Both fields required'})
		return render_template('login.html', form=form)
	user = helpers.get_user()
	if not session.get('payment_success'):
		return render_template('payment.html', user=user)
	return render_template('home.html', user=user)

@app.route('/payment_success')
def payment_success():
	session['payment_success'] = True
	return redirect(url_for('login'))

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect(url_for('login'))


# -------- Signup ---------------------------------------------------------- #
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if not session.get('logged_in'):
        form = forms.LoginForm(request.form)
        if request.method == 'POST':
            username = request.form['username'].lower()
            password = helpers.hash_password(request.form['password'])
            email = request.form['email']
            if form.validate():
                if not helpers.username_taken(username):
                    helpers.add_user(username, password, email)
                    session['logged_in'] = True
                    session['username'] = username
                    return json.dumps({'status': 'Signup successful'})
                return json.dumps({'status': 'Username taken'})
            return json.dumps({'status': 'User/Pass required'})
        return render_template('login.html', form=form)
    return redirect(url_for('login'))


# -------- Settings ---------------------------------------------------------- #
@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if session.get('logged_in'):
        if request.method == 'POST':
            password = request.form['password']
            if password != "":
                password = helpers.hash_password(password)
            email = request.form['email']
            helpers.change_user(password=password, email=email)
            return json.dumps({'status': 'Saved'})
        user = helpers.get_user()
        return render_template('settings.html', user=user)
    return redirect(url_for('login'))

@app.route('/get')
def get_bot_response():
	userText = request.args.get('msg')
	text_input = dialogflow.types.TextInput(text=userText, language_code=language_code)
	query_input = dialogflow.types.QueryInput(text=text_input)
	response = session_client.detect_intent(session=session_dialogflow, query_input=query_input)
	return str(response.query_result.fulfillment_text)

# ======== Main ============================================================== #
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
