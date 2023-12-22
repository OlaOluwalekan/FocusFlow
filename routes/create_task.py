from flask import render_template, request, redirect, flash, abort
from flask_login import current_user
from routes import db

def create_task_route():

  user_id = current_user.id
  cursor = db.cursor()

  action = request.args.get('action', 'create')
  edit_task_id = ''

  # print("ACTION IS:", action)
  
  if action == 'create':
    edit_task_info = None
    action_text = 'Add Task'
  elif action == 'edit':
    action_text = 'Update Task'
    edit_task_id = request.args.get("id")

    try:
      edit_task_id = int(edit_task_id)
    except:
      return redirect('/dashboard/task')
    
    # print(type(edit_task_id))
    cursor.execute("SELECT * FROM tasks WHERE user_id = %s AND task_id = %s", (user_id, edit_task_id))
    edit_task_info = cursor.fetchone()

    if not edit_task_info:
      abort(404)
    else:
      cursor.execute("SELECT category_id FROM task_category WHERE task_id = %s", (edit_task_id,))
      edit_task_categories = cursor.fetchall()
      edit_task_categories = [item["category_id"] for item in edit_task_categories]
      edit_task_info["task_categories"] = edit_task_categories

    # print(edit_task_info)

  else:
    return redirect('/dashboard/task')
    
  
  cursor.execute("SELECT * FROM categories WHERE user_id = %s", (user_id,))
  user_categories = cursor.fetchall()


  if request.method == "POST":
    post_action = request.form.get("action")
    task_name = request.form.get("title")
    task_description = request.form.get("description")
    selected_categories = request.form.getlist("category")

    if not task_name:
      flash("Input a title/name for your task", "error")
      return

    # print(post_action)

    if post_action == "Add Task":
      cursor.execute("INSERT INTO tasks (user_id, task_name, task_description) VALUES (%s, %s, %s) RETURNING task_id", (user_id, task_name, task_description))
      task_id = cursor.fetchone()["task_id"]
      db.commit()

      if selected_categories:
        for category in selected_categories:
          cursor.execute("INSERT INTO task_category (task_id, category_id) VALUES (%s, %s)", (task_id, int(category)))
          db.commit()

      flash("Task created successfully", "success")

    elif post_action == "Update Task":
      edit_task_id = request.form.get("id")
      try:
        edit_task_id = int(edit_task_id)
      except:
        return redirect('/dashboard/task')
      
      cursor.execute("UPDATE tasks SET task_name = %s, task_description = %s WHERE task_id = %s", (task_name, task_description, edit_task_id))
      db.commit()

      cursor.execute("SELECT category_id FROM task_category WHERE task_id = %s", (edit_task_id,))
      task_category = cursor.fetchall()

      task_category = [element['category_id'] for element in task_category]

      selected_categories = [int(element) for element in selected_categories]

      for category in task_category:
        print(category)
        if category not in selected_categories:
          # REMOVE CATEGORY_ID NOT PRESENT FROM DB
          cursor.execute("DELETE FROM task_category WHERE category_id = %s", (category,))
          db.commit()
      for selected_category in selected_categories:
        if selected_category not in task_category:
          cursor.execute("INSERT INTO task_category (task_id, category_id) VALUES(%s, %s)", (edit_task_id, selected_category))

      flash("Task updated successfully", "success")

    else:
      return redirect('/dashboard/task')
    
    return redirect("/dashboard?tab=tasks")

    # print(selected_categories)

  return render_template('create-task.html', action=action_text, categories=user_categories, task_info=edit_task_info)