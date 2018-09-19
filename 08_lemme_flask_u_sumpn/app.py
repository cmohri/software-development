'''
Clara Mohri
SoftDev1 Pd07
K08 -- Fill Yer Flask
2018-09-19
'''

from flask import Flask
app = Flask(__name__) #instantiates the Flask class using a constructor

#route 1
@app.route('/')
def home():
 return "<a href = 'http://127.0.0.1:5000/route1'>Click this link!</a>"

#route 2
@app.route('/route1')
def next():
 return "<a href = 'http://127.0.0.1:5000/route1/route2'>Click <i>this</i> link!</a>"

#route 3
@app.route('/route1/route2')
def route2():
 return "you have arrived"

app.debug = True
app.run()

#Note: These links will only work for me.
