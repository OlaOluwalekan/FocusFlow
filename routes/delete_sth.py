from flask import redirect, request, flash
from flask_login import current_user
from routes import db

def delete_task_route():
  user_id = current_user.id
  task_id = request.form.get("delete_id")
  print("Referrer is ===", request.referrer)
  cursor = db.cursor()

  cursor.execute("DELETE from task_category WHERE task_id = %s", (task_id,))
  db.commit()

  cursor.execute("DELETE from tasks WHERE task_id = %s AND user_id = %s", (task_id, user_id))
  db.commit()

  flash("Task deleted successfully", "success")

  return redirect('/dashboard?tab=tasks')