from flask import render_template, request, redirect, flash
from routes import db
import hashlib
from routes import User
from flask_login import login_user

def login_route():
  if request.method == "POST":
    username = request.form.get('username')
    password = request.form.get('password')

    if not username:
      flash("username is required", 'error')
      return render_template('login.html')

    if not password:
      flash("password is required", 'error')
      return render_template('login.html')
    
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE email = %s OR username = %s", (username, username))
    dbUser = cursor.fetchone()

    if not dbUser:
      flash('invalid username/email or password', 'error')
      return render_template('/login.html')
    
    correctPassword = hashlib.sha256(password.encode()).hexdigest() == dbUser['password']

    if not correctPassword:
      flash('invalid username/email or password', 'error')
      return render_template('login.html')
    
    user_id = dbUser['id']
    
    user = User(user_id)

    login_user(user)
    
    flash('successfully logged in', 'success')
    return redirect('/dashboard')

  return render_template("login.html")