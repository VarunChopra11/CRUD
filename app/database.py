from flask_pymongo import PyMongo
from config import Config

mongo = PyMongo()

def init_app(app):
    global mongo
    app.config["MONGO_URI"] = Config.MONGODB_URI
    mongo.init_app(app)
    return mongo.db