from flask import Flask
from flask_mongoengine import MongoEngine
from mongoengine import connect

db = MongoEngine()

app = Flask(__name__)

app.config['MONGODB_DB'] = 'flask_mongo'
app.config['MONGODB_HOST'] = 'localhost'
app.config['MONGODB_PORT'] = 12027

connect("flask_mongo")