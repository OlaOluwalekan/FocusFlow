from flask import render_template, request, flash, redirect
from routes import db
from flask_login import current_user

def create_category_route():

  user_id = current_user.id
  # print(user_id)

  action = request.args.get('action', 'create')
  if action == 'create':
    action_text = 'Add Category'
  else:
    action_text = 'Update Category'

  if request.method == "POST":
    category = request.form.get("category")
    custom_category = request.form.get("custom")
    color = request.form.get("color")

    # print(category, custom_category, color)

    if not category:
      flash("Please Select a category", "error")
      return render_template('create-category.html', action=action_text)
    
    if category == "Custom" and not custom_category:
      flash("Name your Category", "error")
      return render_template('create-category.html', action=action_text)
    
    if not color:
      flash("Please Select a Color", "error")
      return render_template('create-category.html', action=action_text)
    
    if category == "Custom":
      category = custom_category
    
    cursor = db.cursor()
    cursor.execute("INSERT INTO categories (user_id, category_name, category_color) VALUES (%s, %s, %s)", (user_id, category, color))
    db.commit()
    flash("category created successfully", "success")

    return redirect("/dashboard?tab=categories")

  
  return render_template('create-category.html', action=action_text)