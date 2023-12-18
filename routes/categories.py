from flask import render_template

def categories_route():
  return render_template('categories.html')