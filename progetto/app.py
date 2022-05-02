from flask import Flask , request, jsonify, Response
from flask_cors import CORS
from bson import json_util 

from flask_pymongo import PyMongo

app = Flask(__name__ )

app.config["MONGO_URI"] = "mongodb://khaled:33311Ee9@cluster0-shard-00-00.2e0wc.mongodb.net:27017,cluster0-shard-00-01.2e0wc.mongodb.net:27017,cluster0-shard-00-02.2e0wc.mongodb.net:27017/progetto?ssl=true&replicaSet=atlas-3iutc4-shard-0&authSource=admin&retryWrites=true&w=majority"
mongo = PyMongo(app)
CORS(app)

@app.route("/ciao")
def get():
    uss = mongo.db.stazioni.find()
    resp = json_util.dumps(uss)
    return Response(resp, mimetype = 'application/json') 

if __name__ == '__main__':
    app.run()