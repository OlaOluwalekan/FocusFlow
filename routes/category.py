from flask import render_template, request, abort
from flask_login import current_user
from routes import db
from datetime import datetime

def category_route(category_name):
  user_id = current_user.id
  category_id = request.args.get("Yhdu")
  if not category_id:
    abort(404)

  try:
    category_id = int(category_id)
  except:
    abort(404)

  # print(category_name, category_id)
  category_info = None
  category_tasks = None

  cursor = db.cursor()
  if category_name == "Ongoing" and category_id == 0:
    category_info = {
        'category_id': 0,
        'user_id': 2,
        'category_name': 'Ongoing', 'category_color': '#ff0000',
        'created_at': ''
      }
    cursor.execute("SELECT * FROM tasks WHERE user_id = %s AND is_completed = FALSE", (user_id,))
    category_tasks = cursor.fetchall()
  elif category_name == "Completed" and category_id == 0:
    category_info = {
        'category_id': 0,
        'user_id': 2,
        'category_name': 'Completed', 'category_color': '#00ff00',
        'created_at': ''
      }
    cursor.execute("SELECT * FROM tasks WHERE user_id = %s AND is_completed = TRUE", (user_id,))
    category_tasks = cursor.fetchall()
  elif category_name == "Today" and category_id == 0:
    today = datetime.now().date()
    category_info = {
        'category_id': 0,
        'user_id': 2,
        'category_name': 'Today', 'category_color': '#0000ff',
        'created_at': today
      }
    cursor.execute("SELECT * FROM tasks WHERE user_id = %s AND DATE(created_at) = %s", (user_id, today))
    category_tasks = cursor.fetchall()
  else:
    cursor.execute("SELECT * FROM categories WHERE user_id = %s AND category_id = %s", (user_id, category_id))
    category_info = cursor.fetchone()
    
    # SELECT ALL TASKS IN A CATEGORY
    cursor.execute("SELECT * FROM tasks t JOIN task_category tc ON t.task_id = tc.task_id WHERE t.user_id = %s AND tc.category_id = %s", (user_id, category_id))
    category_tasks = cursor.fetchall()
  

  # print(category_info)

  # return render_template("tst.html")
  return render_template("category.html", category_name=category_name, category_tasks=category_tasks, category_info=category_info)