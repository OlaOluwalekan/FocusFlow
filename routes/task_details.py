from flask import render_template, request, abort, redirect, url_for, jsonify
from flask_login import current_user
from routes import db

def task_details_route(task_name):
  user_id = current_user.id
  task_id = request.args.get("XQrd")

  try:
    task_id = int(task_id)
  except:
    abort(404)

  cursor = db.cursor()
  cursor.execute("SELECT * FROM tasks WHERE task_id = %s AND user_id = %s", (task_id, user_id))
  task_info = cursor.fetchone()

  if not task_info:
    abort(404)

  cursor.execute("SELECT c.category_name, c.category_color FROM task_category tc JOIN categories c ON tc.category_id = c.category_id WHERE task_id = %s", (task_id,))
  task_category = cursor.fetchall()

  task_info["task_categories"] = task_category

  return render_template("task-details.html", task_info=task_info)

def toggle_task_completion_route(task_name):
  is_complete = request.json.get("is_completed")
  task_id = request.json.get("task_id")
  try:
    task_id = int(task_id)
  except:
    abort(404)

  cursor = db.cursor()
  cursor.execute("UPDATE tasks SET is_completed = %s WHERE task_id = %s", (is_complete, task_id))
  db.commit()
  # print(task_id, is_complete)

  return jsonify({"message": "task updated successfully"})