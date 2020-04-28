from flask import Flask, jsonify, request, make_response, abort
from dotenv import load_dotenv
import os
import time
import pymongo as db
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import Counter

path = os.getenv('ENV_FILE_PATH')

load_dotenv(dotenv_path=path)
db_host = os.getenv('DATABASE_HOST', 'mongo')
db_port = os.getenv('DATABASE_PORT', '27017')

app = Flask(__name__)

metrics = PrometheusMetrics(app)


mongoClient = db.MongoClient("mongodb://%s:%s" % (db_host, db_port))
mongoCollection = mongoClient["babble"]["blabs"]

responses = []
next_id = 1
blabCounter = Counter('TotalBlabs', 'The total amount of blabs that have been added')



@app.route('/api/blabs/<id>', methods=['DELETE'])
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


@app.route('/api/blabs', methods=['GET'])
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


@app.route('/api/blabs', methods=['POST'])
def add_blab():
    blabCounter.inc()
    global next_id
    author = request.get_json().get('author')
    message = request.get_json().get('message')

    response = {
        'postTime': int(time.time()),
        'author': author,
        'message': message}
    mongoCollection.insert_one(response)
    next_id += 1
    response['id'] = str(response['_id'])
    del response['_id']
    return make_response(jsonify(response), 201)
