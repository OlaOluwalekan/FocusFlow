from flask import render_template, request, flash, redirect
from flask_login import current_user
from routes import db
import hashlib

def settings_route():
  user_id = current_user.id

  cursor = db.cursor()

  if request.method == "POST":
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")

    cursor.execute("UPDATE users SET first_name = %s, last_name = %s WHERE id = %s", (first_name, last_name, user_id))
    db.commit()
    flash("Name updated successfully", 'success')

  cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))

  user = cursor.fetchone()

  return render_template('settings.html', user=user)

def password_change_route():

  user_id = current_user.id

  password = request.form.get('password')
  confirm = request.form.get('confirm')

  if not password:
    flash("Enter a new password", "error")
    return redirect('/dashboard?tab=settings')
  
  if confirm != password:
    flash("Passwords need to match", "error")
    return redirect('/dashboard?tab=settings')
  
  hashed_password = hashlib.sha256(password.encode()).hexdigest()

  cursor = db.cursor()
  cursor.execute("UPDATE users SET password = %s WHERE id = %s", (hashed_password, user_id))
  db.commit()
  flash("Password updated successfully", "success")

  return redirect('/dashboard?tab=settings')