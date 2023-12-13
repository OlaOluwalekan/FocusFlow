from flask import Flask
from routes.index import home_route
from routes.login import login_route
from routes.register import register_route

app = Flask(__name__)

@app.route("/")
def index():
  return home_route()

@app.route("/login")
def login():
  return login_route()

@app.route("/register")
def register():
  return register_route()


if __name__ == "__main__":
  app.run(debug=True)