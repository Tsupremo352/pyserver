from flask import Blueprint, request
from .User import User
from App.Controller.Auth import login, logout, getSession
from App.Middlewares import auth
Routes = Blueprint('Routes', __name__)

@Routes.route('/')
def index():
  return "Hello World!"

@Routes.route('/login', methods=['POST'])
def _login():
  return login(request.get_json())

@Routes.route('/logout', methods=['POST'])
def _logout():
  return logout()

@Routes.route('/session')
@auth
def _getSession():
  return getSession()

Routes.register_blueprint(User, url_prefix='/user')