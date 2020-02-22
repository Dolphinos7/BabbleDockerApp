from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
        return "hello world"

@app.route('/greetings')
def greetings():
        to_return = [1, 2, 3]
        return jsonify(greetings=to_return)

app.run(host="0.0.0.0")

#docker run -p 5000:5000 -v ${PWD}/src:/app/src -e FLASK_APP=src/app.py -e FLASK_ENV=development python-with-flask