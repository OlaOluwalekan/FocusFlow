from flask import render_template, request, redirect, flash
from flask_login import current_user
from routes import db

def create_task_route():

  user_id = current_user.id

  action = request.args.get('action', 'create')
  
  if action == 'create':
    action_text = 'Add Task'
  else:
    action_text = 'Update Task'

  cursor = db.cursor()
  cursor.execute("SELECT * FROM categories WHERE user_id = %s", (user_id,))
  user_categories = cursor.fetchall()


  if request.method == "POST":
    task_name = request.form.get("title")
    task_description = request.form.get("description")
    selected_categories = request.form.getlist("category")

    if not task_name:
      flash("Input a title/name for your task", "error")
      return

    if action == "create":
      cursor.execute("INSERT INTO tasks (user_id, task_name, task_description) VALUES (%s, %s, %s) RETURNING task_id", (user_id, task_name, task_description))
      task_id = cursor.fetchone()["task_id"]
      db.commit()

      if selected_categories:
        for category in selected_categories:
          cursor.execute("INSERT INTO task_category (task_id, category_id) VALUES (%s, %s)", (task_id, int(category)))
          db.commit()

      flash("Task created successfully", "success")
      return redirect("/dashboard?tab=tasks")

    # print(selected_categories)

  return render_template('create-task.html', action=action_text, categories=user_categories)