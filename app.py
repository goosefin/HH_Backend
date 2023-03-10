from flask import Flask,jsonify,after_this_request
import models
from flask_cors import CORS
from flask_login import LoginManager
import os
from dotenv import load_dotenv
from resources.apartment import apartments
from resources.user import user

load_dotenv()

DEBUG = True
PORT = os.environ.get("PORT")

app = Flask(__name__)

app.secret_key = os.environ.get("SECRET_KEY")

app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='None'
)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    try:
        return models.User.get(models.User.id == user_id)
    except models.DoesNotExist:
        return None

app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app, resources={r"/*": {"origins": "*"}})
CORS(apartments, origins=['*'], supports_credentials=True)
CORS(user, origins=['*'], supports_credentials=True)

app.register_blueprint(apartments,url_prefix='/api/v1/apartments')
app.register_blueprint(user,url_prefix='/api/v1/user')

@app.before_request
def before_request():
    """Connect to the db before each request"""
    print('You should see this before every request')
    models.DATABASE.connect()

    @after_this_request
    def after_request(response):
        """Close the db connection after each request"""
        print("You should see this after each request")
        models.DATABASE.close()
        return response

# if os.environ.get('FLASK_ENV') != 'development':
#   print('\non heroku!')
#   models.initialize()

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)