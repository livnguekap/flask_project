from flask import Flask, render_template
from urllib.parse import quote as url_quote


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/app')
def blog():
    return "Hello, from the App!!"


if __name__ == "__main__":
    app.run(threaded=True,host="0.0.0.0", port=8000)