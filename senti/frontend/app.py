from flask import Flask,render_template
from backend.sentiment import classify

app = Flask(__name__)

@app.route('/senti/<message>')
def hello(message=None):
    return render_template('hello.html', person=classify(message)[0]["label"])