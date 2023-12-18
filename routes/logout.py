from flask_login import logout_user
from flask import redirect, flash

def logout_route():
  logout_user()
  flash("Logged out successfully", "success")
  return redirect('/')