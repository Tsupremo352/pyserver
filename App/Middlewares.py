from flask import session
from functools import wraps

def auth(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    if 'user' not in session:
      return "Unauthorized", 401
    return f(*args, **kwargs)
  return decorated