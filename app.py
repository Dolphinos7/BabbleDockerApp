from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/blabs')
def get_blabs():
        created_since = request.query_string

        #right now just return the timestamp until the rest is implemented
        return created_since