'''
Clara Mohri
SoftDev1 Pd07
K13 -- Echo Echo Echo
2018-09-27
'''

from flask import Flask, render_template
import random
from flask import request
app = Flask(__name__) #instantiates the Flask class using a constructor

#form:
@app.route('/')
def home():
 print(app)
 return render_template('page.html')

#greeting based on user input
@app.route('/auth')
def authenticate():
 #list of greetings
 greetings = ['Hello there, ', 'Good morning, ', 'Good afternoon, ', 'Good evening, ', 'Hello, ', 'Wassup, ']
 return random.choice(greetings) + request.args['username'] + "!<br> We used the request.args dictionary to access your name"

app.debug = True
app.run()


