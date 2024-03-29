from os import getenv
from dotenv import load_dotenv
from flask import Flask
from App.Utils import bcrypt
from App.Routes.Routes import Routes
from App.Model.Model import DB
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
DB.init_app(app)
bcrypt.init_app(app)

app.register_blueprint(Routes, url_prefix='/')

if __name__ == '__main__':
  app.run(debug=True)