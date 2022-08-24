from flask import Flask
app = Flask(name)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

if name == "main":
    app.run(host='0.0.0.0')