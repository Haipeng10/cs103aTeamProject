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
from flask import request,redirect,url_for,Flask,render_template
from gpt import GPT
import os

app = Flask(__name__, template_folder="templates")
gptAPI = GPT(os.environ.get('APIKEY'))

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'xxxxxx'

@app.route('/')
def index():
    ''' display a link to the general query page '''
    print('processing / route')
    return render_template('index.html')

@app.route('/about')
def about():
    ''' display a link to the about page '''
    print('processing / route')
    return render_template('about.html')

@app.route('/conversion', methods=['GET', 'POST'])
def conversion():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = "Convert the following code to " + request.form['target_language'] + "\n\n" + request.form['code']
        answer = gptAPI.getResponse(prompt)
        return render_template('conversion_response.html', answer=answer)
    else:
        return render_template('conversion.html')

'''time complexity'''
@app.route('/runtime', methods=['GET', 'POST'])
def runtime():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = "What is time complexity of the following codes: \n " +  request.form['code']
        answer = gptAPI.getResponse(prompt)
        return render_template('conversion_response.html', answer=answer)
    else:
        return render_template('runtime.html')  

    
@app.route('/gptdemo', methods=['GET', 'POST'])
def gptdemo():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.getResponse(prompt)
        return f'''
        <h1>GPT Demo</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('gptdemo')}> make another query</a>
        '''
    else:
        return '''
        <h1>GPT Demo App</h1>
        Enter your query below
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''

if __name__=='__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True,port=5001)
