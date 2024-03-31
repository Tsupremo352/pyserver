from App.Model.User import User
from App.Utils import bcrypt, sess
from flask import jsonify, session

def login(request):
  user = User.query.filter_by(email = request['email']).first()
  if user is None or not bcrypt.check_password_hash(user.password, request['password']):
    return jsonify({"Error": "Unauthorized"}), 401
  session['user'] = user.email
  return jsonify(user)

def getSession():
  print(session.get('user'))
  return jsonify(session.get('user')) 

def logout():
  session.pop('user', None)
  return jsonify({"Message": "Logged out"})