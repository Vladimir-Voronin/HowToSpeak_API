from flask_session import Session
from pymongo import MongoClient
from flask import Flask, session

from APIServer.Cashing.casher import Casher
from APIServer.config import SECRET_KEY, DB_HOST, DB_PORT


def database_connection():
    client = MongoClient(f'mongodb://{DB_HOST}:{DB_PORT}')
    db = client.hts_db
    return db


app = Flask(__name__)
app.secret_key = SECRET_KEY

SESSION_TYPE = 'mongodb'
app.config.from_object(__name__)
Session(app)

DB = database_connection()
CasherHTS = Casher()

BASE_URL = "/howtospeak/api"

from APIServer.Errors.server_errors import *
from APIServer.Roots.authentication_roots import *
from APIServer.Roots.vocabulary_roots import *

if __name__ == "__main__":
    app.run(debug=True)
