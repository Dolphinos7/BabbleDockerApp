from flask import Flask, jsonify, request, Response, abort
import time
app = Flask(__name__)

responses = []


@app.route('/blabs/<id>', methods=['DELETE'])
def remove_blab(id):
    for response in responses:
        if (response["id"] == id):
            responses.remove(response)
            return Response(response , status=200, mimetype='application/json')
    return abort(404)


@app.route('/blabs', methods=['GET'])
def get_blabs():
    created_since = request.args
    return jsonify(responses)

    #created_since = request.curl -X POST -d '{ "author": { "email": "user@example.com", "name": "string"}, "message": "Hello there"}' localhost/blabs --header "Content-Type:application/json"
    #This was just for testing queries, not at all what spec requires us to do

    #return created_since


@app.route('/blabs', methods=['POST'])
def add_blab():
    author = request.get_json().get('author')
    message = request.get_json().get('message')

    #need to not hardcode in the post id
    response = {
        'id': str(1),
        'postTime': int(time.time()),
        'author': author,
        'message': message}
    responses.append(response)
    return jsonify(response)
