from flask import Flask, jsonify, request, make_response, abort
import time
app = Flask(__name__)

responses = []
next_id = 1


@app.route('/api/blabs/<id>', methods=['DELETE'])
def remove_blab(id):
    for response in responses:
        if (response["id"] == id):
            responses.remove(response)
            return make_response(jsonify(response), 200)
    return abort(404)


@app.route('/api/blabs', methods=['GET'])
def get_blabs():
        args = request.args
        created_since = args.get("createdSince")
        toReturn = []
        for response in responses:
                if response.get("postTime")>=int(created_since):
                        toReturn.append(response)
        return make_response(jsonify(toReturn), 200)



@app.route('/api/blabs', methods=['POST'])
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
        return make_response(jsonify(response), 201)