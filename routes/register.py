from flask import render_template, flash, request, redirect
from flask_login import current_user
from routes import db
import hashlib

def register_route():
  if request.method == "POST":
    # GET FORM INPUTS
    email = request.form.get("email")
    username = request.form.get("username")
    password = request.form.get("password")
    confirm = request.form.get("confirm")

    # CHECK FOR EMPTY EMAIL
    if not email:
      flash('email is required', 'error')
      return render_template("register.html")

    # CHECK FOR EMPTY USERNAME
    if not username:
      flash('username is required', 'error')
      return render_template("register.html")
    
    # CHECK FOR EMPTY PASSWORD
    if not password:
      flash('password is required', 'error')
      return render_template("register.html")
    
    # CHECK PASSWORD CONFIRMATION
    if confirm != password:
      flash('password must match', 'error')
      return render_template("register.html")
    
    cursor = db.cursor()
    cursor.execute("SELECT email FROM users WHERE email = %s", (email,))
    dbEmail = cursor.fetchall()

    # CHECK FOR DUPLICATE EMAIL
    if dbEmail:
      flash('email ' + email + ' already registered', 'error')
      return render_template("register.html")
    
    cursor.execute("SELECT email FROM users WHERE username = %s", (username,))
    dbUsername = cursor.fetchall()

    # CHECK FOR DUPLICATE USERNAME
    if dbUsername:
      flash('username ' + username + ' already chosen', 'error')
      return render_template("register.html")
    
    # REGISTER USER
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", (username, email, hashed_password))
    db.commit()
    flash('user ' + username + ' successfully created', 'success')
    
    return redirect("/")
  
  if current_user.is_authenticated:
    return redirect('/dashboard')

  return render_template("register.html")