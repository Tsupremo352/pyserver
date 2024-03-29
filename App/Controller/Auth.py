from App.Model.User import User
from App.Utils import bcrypt
from flask import jsonify

def login(request):
  user = User.query.filter_by(email = request['email']).first()
  if user is None or not bcrypt.check_password_hash(user.password, request['password']):
    return jsonify({"Error": "Unauthorized"}), 401
  return jsonify(user)