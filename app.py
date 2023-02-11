from flask import Flask,jsonify
import models
from flask_cors import CORS
from flask_login import LoginManager
import os
from dotenv import load_dotenv
from resources.apartment import apartments
from resources.user import user

DEBUG = True
PORT = 8000

app = Flask(__name__)

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)