from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world"

@app.route("/")##/<string:name>")
def index():##name):
    ##return "Hello, world{}".format(name)
    headline = "Hello, world!"
    return render_template("index.html",headline=headline)
