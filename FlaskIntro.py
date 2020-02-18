from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
        return "hello world"

app.run(host="0.0.0.0")

#docker run -p 500:5000 -v ${PWD}/src:/app/src -e FLASK_APP=src/app.py -e FLASK_ENV=development python-with-flask