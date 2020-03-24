from flask import Flask, jsonify, request
import time
app = Flask(__name__)

responses = []
next_id = 1

@app.route('/blabs', methods = ['GET'])
def get_blabs():
        args = request.args
        created_since = args.get("createdSince")
        toReturn = []
        for response in responses:
                if response.get("postTime")>=int(created_since):
                        toReturn.append(response)
        return jsonify(toReturn)

@app.route('/blabs', methods = ['POST'])
def add_blab():
        global next_id
        author = request.get_json().get('author')
        message = request.get_json().get('message')
        
        response = {
                'id': str(next_id), 
                'postTime':int(time.time()),
                'author': author,
                'message': message }
        responses.append(response)
        next_id+=1
        return jsonify(response)