from flask import Flask, jsonify, request, make_response, abort
import time
import pymongo as db
app = Flask(__name__)

mongoClient = db.MongoClient("mongodb://mongo:27017")
mongoCollection = mongoClient["babble"]["blabs"]

responses = []
next_id = 1


@app.route('/blabs/<id>', methods=['DELETE'])
def remove_blab(id: int):
    query = {'_id': int(id)}
    to_delete = mongoCollection.find_one(query)
    if to_delete:
        to_return = to_delete.copy()
        to_return['id'] = str(to_delete['_id'])
        del to_return['_id']
        mongoCollection.delete_one(query)
        return make_response(jsonify(to_return), 200)
    return abort(404)


@app.route('/blabs', methods=['GET'])
def get_blabs():
    args = request.args
    created_since = args.get("createdSince")
    if created_since is None:
        created_since = 0
    toReturn = []
    for response in mongoCollection.find():
        if response.get("postTime") >= int(created_since):
            i = response.copy()
            i['id'] = str(response['_id'])
            del i['_id']
            toReturn.append(i)
    return make_response(jsonify(toReturn), 200)


@app.route('/blabs', methods=['POST'])
def add_blab():
    global next_id
    author = request.get_json().get('author')
    message = request.get_json().get('message')

    response = {
        '_id': next_id,
        'postTime': int(time.time()),
        'author': author,
        'message': message}
    mongoCollection.insert_one(response)
    next_id += 1
    response['id'] = str(response['_id'])
    del response['_id']
    return make_response(jsonify(response), 201)
