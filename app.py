from flask import Flask
# This is change that I have done

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello My name is  Smit'


if __name__ == '__main__':

    app.run()
