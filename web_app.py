from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/knockknock")
def halloween():
    return "Trick or Treat!"

@app.route("/<message>")
def echo(message):
    return (message + '~') * 3

if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 5000)