from flask import render_template, request, abort
from flask_login import current_user
from routes import db

def category_route(category_name):
  user_id = current_user.id
  category_id = request.args.get("Yhdu")
  if not category_id:
    abort(404)

  try:
    category_id = int(category_id)
  except:
    abort(404)

  cursor = db.cursor()
  cursor.execute("SELECT * FROM categories WHERE user_id = %s AND category_id = %s", (user_id, category_id))
  category_info = cursor.fetchone()
  # cursor.execute("SELECT * FROM task_category WHERE category_id = %s", (category_id,))
  cursor.execute("SELECT * FROM tasks t JOIN task_category tc ON t.task_id = tc.task_id WHERE t.user_id = %s AND tc.category_id = %s", (user_id, category_id))
  category_tasks = cursor.fetchall()
  

  print(category_info)

  return render_template("category.html", category_name=category_name, category_tasks=category_tasks, category_info=category_info)