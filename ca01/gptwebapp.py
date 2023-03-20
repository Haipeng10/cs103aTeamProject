# -*- coding: utf-8 -*-
'''
gptwebapp shows how to create a web app which ask the user for a prompt
and then sends it to openai's GPT API to get a response. You can use this
as your own GPT interface and not have to go through openai's web pages.

We assume that the APIKEY has been put into the shell environment.
Run this server as follows:

On Mac
% pip3 install openai
% pip3 install flask
% export APIKEY="......."  # in bash
% python3 gptwebapp.py

On Windows:
% pip install openai
% pip install flask
% $env:APIKEY="....." # in powershell
% python gptwebapp.py
'''
from flask import request, redirect, url_for, Flask, render_template
from gpt import GPT
import os


app = Flask(__name__, static_url_path='/static', static_folder='static', template_folder="templates")
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_MIMETYPE'] = 'application/json;charset=utf-8'

app = Flask(__name__, template_folder="templates")
gptAPI = GPT(os.environ.get('APIKEY'))

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'xxxxx'


@app.route('/')
def index():
    ''' display a link to the general query page '''
    return render_template('index.html')


@app.route('/about')
def about():
    ''' display a link to the about page '''
    return render_template('about.html')


@app.route('/team')
def team():
    ''' display a link to the about page '''
    return render_template('team.html')


#time complexity
@app.route('/runtime', methods=['GET', 'POST'])
def runtime():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['code']
        answer = gptAPI.get_response_for_time_complexity(prompt)
        return render_template('response.html', answer=answer)
    return render_template('runtime.html')


@app.route('/refactor', methods=['GET', 'POST'])
def refactor():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['code']
        answer = gptAPI.refactor(prompt)
        return render_template('response.html', answer=answer)
    return render_template('refactor.html')

@app.route('/comment', methods=['GET', 'POST'])
def comment():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['code']
        answer = gptAPI.comment(prompt)
        return render_template('response.html', answer=answer)
    return render_template('comment.html')

@app.route('/conversion', methods=['GET', 'POST'])
def conversion():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        target = request.form['target_language']
        code = request.form['code']
        answer = gptAPI.change_code_language(target, code)
        return render_template('response.html', answer=answer)
    return render_template('conversion.html')


if __name__ == '__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True, port=5001)
