'''
Demo code for interacting with GPT-3 in Python.

To run this you need to 
* first visit openai.com and get an APIkey, 
* which you export into the environment as shown in the shell code below.
* next create a folder and put this file in the folder as gpt.py
* finally run the following commands in that folder

On Mac
% pip3 install openai
% export APIKEY="......."  # in bash
% python3 gpt.py

On Windows:
% pip install openai
% $env:APIKEY="....." # in powershell
% python gpt.py
'''
import openai


class GPT():
    ''' make queries to gpt from a given API '''
    def __init__(self,apikey):
        ''' store the apikey in an instance variable '''
        self.apikey=apikey
        # Set up the OpenAI API client
        openai.api_key = apikey #os.environ.get('APIKEY')

        # Set up the model and prompt
        self.model_engine = "text-davinci-003"

    def getResponse(self,prompt):
        ''' Generate a GPT response '''
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )

        response = completion.choices[0].text
        return response
    
    def rewriteCode(self, code):
        '''
        Refactor this code to make it work the same way as the original code.
        '''
        task = "Help me convert the code in another way, but does the same thing! (just show me the code with comments, no extra words)\n"
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=task+code,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )

        response = completion.choices[0].text
        return response

    def addComments(self, code):
        '''
        Add comments to the code.
        Return the commented code.
        '''
        prefix = "Add comments to below code: (just show me the code with comments, no extra words)\n"
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=prefix + code,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )

        response = completion.choices[0].text
        return response
    
    def getResponseForTimeComplexity(self,prompt):
        ''' 
        return the time complexity of the input code
        '''
        prefix = 'What is time complexity of the following codes: \n'
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=prefix + prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )

        response = completion.choices[0].text
        return response

if __name__=='__main__':
    '''
    '''
    import os
    g = GPT("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")
    print(g.getResponse("what does openai's GPT stand for?"))
