from flask import render_template
from flask_login import current_user
from routes import db

def tasks_route():
  user_id = current_user.id

  cursor = db.cursor()
  cursor.execute("SELECT * FROM tasks WHERE user_id = %s", (user_id,))
  user_tasks = cursor.fetchall()

  for user_task in user_tasks:
    cursor.execute("SELECT c.category_name, c.category_color FROM categories c JOIN task_category tc ON c.category_id = tc.category_id WHERE task_id = %s", (user_task["task_id"],))
    task_categories = cursor.fetchall()
    user_task["task_categories"] = task_categories
    # print("*********************************")
    # print(user_task["task_name"])
    # print(user_task)
    # print("*********************************")

  # print(user_tasks)

  return render_template('tasks.html', tasks=user_tasks)