from flask import render_template

def not_found_route():
  return render_template("404.html")