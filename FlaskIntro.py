from flask import Flask, jsonify
import greetings
app = Flask(__name__)

@app.route('/')
def hello_world():
        return "hello world"

@app.route('/greetings')
def greetings():
        to_return = ["Hello there", "Welcome"]
        return jsonify(greetings=to_return)

app.run(host="0.0.0.0")

#docker run -p 500:5000 -v ${PWD}/src:/app/src -e FLASK_APP=src/app.py -e FLASK_ENV=development python-with-flask