from dataclasses import dataclass
from .Model import DB

@dataclass
class User(DB.Model):
  __tablename__ = 'users'
  id: int
  username: str
  password: str
  email: str
  active: bool

  id = DB.Column(DB.Integer, primary_key=True)
  username = DB.Column(DB.String(50), unique=True)
  password = DB.Column(DB.String(50))
  email = DB.Column(DB.String(50), unique=True)
  active = DB.Column(DB.Boolean, default=True)

  def __repr__(self):
    return f"<User('{self.username}', '{self.email}')>"