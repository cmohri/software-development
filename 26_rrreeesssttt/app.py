import urllib
import json

from flask import Flask, render_template

app = Flask(__name__)

KEY1 = '07d8075b-29f4-4f56-92ed-1fe051f96c24'
URL_STUB1 = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/database?key='
URL1 = URL_STUB1 + KEY1

KEY2 = ''
URL_STUB2 = 'http://api.icndb.com/jokes/random'
URL2 = URL_STUB2 + KEY2

KEY3 = '10707437-22531ab5c1d14e87da43cea56'
URL_STUB3 = 'https://pixabay.com/api/?image_type=photo&pretty=true&category=nature&editors_choice=true&key='
URL3 = URL_STUB3 + KEY3

url = [URL1, URL2, URL3]

@app.route('/', methods = ['GET'])
def index():
    data1 = getData(URL1)
    data2 = getData(URL2)
    data3 = getData(URL3)
    return render_template('index.html', data = data1, data_ = data2, d = data3)

#function to get data as json dictionary
def getData(u):
    req = urllib.request.urlopen(u)
    data = json.loads(req.read())
    return data

#run
if __name__ == '__main__':
    app.debug = True
    app.run()
