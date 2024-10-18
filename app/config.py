import os

class Config:
    MONGODB_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017/users_db")
    DEBUG = True
    PORT = 5000