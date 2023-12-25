from flask import Flask
from routes import app
from routes.index import home_route
from routes.login import login_route
from routes.register import register_route
from routes.dashboard import dashboard_route
from routes.logout import logout_route
from routes.create_task import create_task_route
from routes.create_category import create_category_route
from routes.errors import not_found_route
from routes.category import category_route
from routes.task_details import task_details_route, toggle_task_completion_route
from routes.delete_sth import delete_task_route
from flask_login import login_required

app.debug = True

@app.route("/")
def index():
  return home_route()

@app.route("/dashboard/category/<category>")
@login_required
def category(category):
  return category_route(category_name=category)

@app.route('/dashboard/category', methods=["GET", "POST"])
@login_required
def create_category():
  return create_category_route()

@app.route('/dashboard/task', methods=["GET", "POST"])
@login_required
def create_task():
  return create_task_route()

@app.route('/dashboard')
@login_required
def dashboard():
  return dashboard_route()

@app.route('/dashboard/tasks/delete', methods=["POST"])
@login_required
def delete_task():
  return delete_task_route()

@app.route("/login", methods=["GET", "POST"])
def login():
  return login_route()

@app.route('/logout')
@login_required
def logout():
  return logout_route()

@app.route("/register", methods=["GET", "POST"])
def register():
  return register_route()

@app.route("/dashboard/task/<task>")
@login_required
def task_details(task):
  return task_details_route(task_name=task)

@app.route("/dashboard/task/<task>/update_completed", methods=["POST"])
@login_required
def toggle_task_completion(task):
  return toggle_task_completion_route(task_name=task)


@app.errorhandler(404)
def page_not_found(e):
  return not_found_route()



if __name__ == "__main__":
  app.run()