from flask import Flask, jsonify, request
import time
app = Flask(__name__)

responses = []

@app.route('/blabs')
def get_blabs():
        created_since = request.query_string
        #This was just for testing queries, not at all what spec requires us to do
        
        return created_since

@app.route('/blabs', methods = ['POST'])
def add_blab():
        author = request.get_json().get('author')
        message = request.get_json().get('message')
        
        #need to not hardcode in the post id
        response = {
                'id': str(1), 
                'postTime':int(time.time()),
                'author': author,
                'message': message }
        responses.append(response)
        return jsonify(response)