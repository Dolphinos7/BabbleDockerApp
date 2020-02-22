from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
        return "hello world"

@app.route('/greetings')
def greetings():
        to_return = ["Hello there", "Welcome"]
        return jsonify(greetings=to_return)

app.run(host="0.0.0.0")

#docker run -p 5000:5000 babble