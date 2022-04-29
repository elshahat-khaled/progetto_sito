from flask import Flask , request, jsonify, Response
from flask_restful import Resource , Api ,reqparse
from flask_cors import CORS
import pandas as pd

from flask_pymongo import PyMongo

app = Flask(__name__ )

app.config["MONGO_URI"] = "mongodb://khaled:33311Ee9@cluster0-shard-00-00.2e0wc.mongodb.net:27017,cluster0-shard-00-01.2e0wc.mongodb.net:27017,cluster0-shard-00-02.2e0wc.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-3iutc4-shard-0&authSource=admin&retryWrites=true&w=majority"

mongo = PyMongo(app)

CORS(app)
api = Api(app)


class UsersApi(Resource):
    def get(self):
        uss = mongo.db.stazioni.find()
        resp = json_util.dumps(uss)
        return Response(resp, mimetype = 'application/json') 
    def post(self):
        country = request.json["country"]
        latitude = request.json["latitude"]
        longitude = request.json["longitude"]
        name = request.json["name"]
        time_zone = request.json["time_zone"]
        if country and latitude and longitude and name and time_zone:
            id = mongo.db.stazioni.insert_one(
                {
                'country': country,
                'latitude': latitude,
                'longitude': longitude,
                'name': name,
                'time_zone': time_zone 
                }
            )
            resp = {
                "id" : str(id),
                'country': country,
                'latitude': latitude,
                'longitude': longitude,
                'name': name,
                'time_zone': time_zone
            }
            return resp
        else:
            return {'message': 'received'}

api.add_resource(UsersApi, '/stazioni')



if __name__ == '__main__':
    app.run()