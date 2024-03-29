from flask import jsonify, Response
from App.Model.User import User, DB
from App.Utils import bcrypt

def getUser():
  result = User.query.all()
  return jsonify(result)

def createUser(request):
  user = User.query.filter_by(email = request['email']).first()
  if user:
    return jsonify({"Error": "User Already Exists"}), 409

  password = bcrypt.generate_password_hash(request['password'], 10).decode('utf-8')
  newUser = User(username=request['username'], password=password, email=request['email'])
  DB.session.add(newUser)
  DB.session.commit()
  return jsonify(newUser)