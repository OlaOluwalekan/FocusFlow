from flask import render_template

def category_route(category_name):
  return render_template("category.html", category_name=category_name)