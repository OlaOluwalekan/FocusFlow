from flask import render_template

def settings_route():
  return render_template('settings.html')