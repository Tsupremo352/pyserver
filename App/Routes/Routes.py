from flask import Blueprint, request
from .User import User
from App.Controller.Auth import login
Routes = Blueprint('Routes', __name__)

@Routes.route('/')
def index():
  return "Hello World!"

@Routes.route('/login', methods=['POST'])
def _login():
  return login(request.get_json())

Routes.register_blueprint(User, url_prefix='/user')