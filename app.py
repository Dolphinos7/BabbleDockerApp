from flask import Flask, jsonify, request
app = Flask(__name__)

greetings = ["hello", "hey"]

@app.route('/')
def get_all_greetings():
        return jsonify(greetings)

@app.route( '/greetings' , methods = [ 'POST'])
def add_greeting():
        content = request.json
        newGreeting = "Hello %s" % content[ 'name']
        greetings.append(newGreeting)
        return jsonify({ "greeting" : newGreeting })

app.run(host="0.0.0.0")

#docker run -p 5000:5000 neberizer/babble
