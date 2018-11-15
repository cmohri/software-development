import urllib
import json

from flask import Flask, render_template

app = Flask(__name__)

KEY = "697684d3-9e9e-45e8-b3a4-b28ed5a741d9"
URL_STUB = "https://content.guardianapis.com/search?api-key="
URL = URL_STUB + KEY

@app.route("/", methods=["GET"])
def index():
    req = urllib.request.urlopen(URL)
    data = json.loads(req.read())
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.debug = True
    app.run()
