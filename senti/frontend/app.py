from flask import Flask,render_template

app = Flask(__name__)

@app.route('/senti/<message>')
def hello(message=None):
    return render_template('hello.html', person=message)