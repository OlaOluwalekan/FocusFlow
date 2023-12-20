from flask import render_template
from flask_login import current_user
from routes import db

def categories_route():

  user_id = current_user.id

  cursor = db.cursor()
  cursor.execute("SELECT * FROM categories WHERE user_id = %s", (user_id,))
  user_categories = cursor.fetchall()

  # print(user_categories)

  return render_template('categories.html', categories=user_categories)