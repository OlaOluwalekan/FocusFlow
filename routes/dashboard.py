from flask import render_template, request
from routes import db
from flask_login import current_user
from routes.tasks import tasks_route
from routes.categories import categories_route
from routes.settings import settings_route

def dashboard_route():
  tab = request.args.get('tab', 'default-tab')
  
  cursor = db.cursor()
  cursor.execute("SELECT * FROM users WHERE id = %s", (current_user.id,))
  dbUser = cursor.fetchone()

  if tab == "tasks":
    return tasks_route()
  
  if tab == "categories":
    return categories_route()
  
  if tab == "categories":
    return settings_route()

  return render_template('dashboard.html', user=dbUser)