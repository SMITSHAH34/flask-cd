from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello,My name is Smit!</h1>'

if name == "main":
    app.run(host='0.0.0.0')