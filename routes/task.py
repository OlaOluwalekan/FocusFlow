from flask import render_template, request, abort
from flask_login import current_user
from routes import db

def task_route(task_name):
  user_id = current_user.id
  task_id = request.args.get("XQrd")

  cursor = db.cursor()
  cursor.execute("SELECT * FROM tasks WHERE task_id = %s AND user_id = %s", (task_id, user_id))
  task_info = cursor.fetchone()

  if not task_info:
    abort(404)

  # print(task_info)

  return render_template("task.html", task_info=task_info)