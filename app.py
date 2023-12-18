from flask import Flask
from routes import app
from routes.index import home_route
from routes.login import login_route
from routes.register import register_route
from routes.dashboard import dashboard_route
from routes.logout import logout_route
from flask_login import login_required

app.debug = True

@app.route("/")
def index():
  return home_route()

@app.route("/login", methods=["GET", "POST"])
def login():
  return login_route()

@app.route("/register", methods=["GET", "POST"])
def register():
  return register_route()

@app.route('/dashboard')
@login_required
def dashboard():
  return dashboard_route()

@app.route('/logout')
def logout():
  return logout_route()


if __name__ == "__main__":
  app.run()