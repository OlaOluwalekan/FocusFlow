from flask import render_template, request, abort
from routes import db
from flask_login import current_user
from routes.tasks import tasks_route
from routes.categories import categories_route
from routes.settings import settings_route
from routes.dashboard_home import dashboard_home_route

def dashboard_route():
  tab = request.args.get('tab', 'default-tab')
  # print(tab)

  if tab == "tasks":
    return tasks_route()
  
  if tab == "categories":
    return categories_route()
  
  if tab == "settings":
    return settings_route()
  
  if tab == 'home' or tab == 'default-tab':
    return dashboard_home_route()
  
  return abort(404)