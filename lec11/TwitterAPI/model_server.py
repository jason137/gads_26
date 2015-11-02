from flask import Flask
from flask import request
import sentiment_model

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/sentimentcheck")
def sentiment_check():
    sent = request.args.get('q', '')
    

if __name__ == '__main__':
    app.run()
