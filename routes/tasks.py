from flask import render_template

def tasks_route():
  return render_template('tasks.html')