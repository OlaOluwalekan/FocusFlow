from flask import render_template
from routes import db
from flask_login import current_user
from datetime import datetime
from routes.filters import time_ago_filter

def dashboard_home_route():
  user_id = current_user.id
  cursor = db.cursor()

  # GET CURRENT USER INFO
  cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
  dbUser = cursor.fetchone()

  # GET ALL ONGOING TASKS
  cursor.execute("SELECT * FROM tasks WHERE user_id = %s AND is_completed = FALSE", (user_id,))
  ongoing_tasks = cursor.fetchall()

  # GET ALL COMPLETED TASKS
  cursor.execute("SELECT * FROM tasks WHERE user_id = %s AND is_completed = TRUE", (user_id,))
  completed_tasks = cursor.fetchall()

  # GET ALL TASKS CREATED TODAY
  today = datetime.now().date()
  cursor.execute("SELECT * FROM tasks WHERE user_id = %s AND DATE(created_at) = %s", (user_id, today))
  today_tasks = cursor.fetchall()

  # GET ALL TASKS CREATED LESS THAN 24 HOURS AGO
  cursor.execute("SELECT * FROM tasks WHERE user_id = %s AND created_at >= NOW() - INTERVAL '24 hours' ORDER BY created_at DESC", (user_id,))
  recent_tasks = cursor.fetchall()

  return render_template('dashboard.html', user=dbUser, ongoing_tasks=ongoing_tasks, completed_tasks=completed_tasks, today_tasks=today_tasks, recent_tasks=recent_tasks)