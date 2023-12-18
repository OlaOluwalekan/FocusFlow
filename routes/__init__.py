from flask import Flask
from dotenv import load_dotenv
import os
import psycopg2
from psycopg2.extras import RealDictCursor
from flask_login import LoginManager, UserMixin

app = Flask(__name__)

app.secret_key = "jwduui2l29u94kjsjh3r99ueknd"

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

db = psycopg2.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME, cursor_factory=RealDictCursor)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin):
  def __init__(self, user_id):
    self.id = user_id

  @staticmethod
  def get(user_id):
    conn = psycopg2.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME, cursor_factory=RealDictCursor, port=5432)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user_data = cursor.fetchone()
    conn.close()

    if user_data:
      return User(user_data['id'])
    
    return None

@login_manager.user_loader
def load_user(user_id):
  return User.get(user_id)



