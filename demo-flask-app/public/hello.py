from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"
