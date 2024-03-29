import json
from flask import Blueprint, request
from App.Controller.User import getUser, createUser
User = Blueprint('User', __name__)

@User.route('/', methods=['GET'])
def _getUser():
  return getUser()

@User.route('/', methods=['POST'])
def _createUser():
  return createUser(request.get_json())