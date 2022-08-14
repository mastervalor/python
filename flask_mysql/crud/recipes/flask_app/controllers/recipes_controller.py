from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user_model import Users
from flask_app.models.recipe_model import Recipes

@app.route('/recipes')
def posts():
    if 'user_id' not in session:
        return redirect('/')
    user = {
        "id": session['user_id']
    }
    return render_template('recipes.html', user = Users.get_by_id(user), recipes =Recipes.all_recipes())

@app.route('/recipe/new')
def new_recipe():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('new.html')
    
@app.route('/recipe/edit/<int:id>')
def edit_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": id
    }
    return render_template('edit.html', recipe= Recipes.get_one_recipe(data))

@app.route('/recipe/change/<int:id>', methods=["POST"])
def change_recipe(id):
    if not Recipes.validate_recipe(request.form):
        return redirect(f'/recipe/new/{id}')
    data = {
        'id': id,
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'date_made': request.form['date_made'],
        'cook_time': request.form['cook_time']
    }
    Recipes.Update_recipe(data)
    return redirect('/recipes')

@app.route('/recipe/view/<int:id>')
def view_recipe(id):
    if 'user_id' not in session:
            return redirect('/')
    data = {
        "id": id
    }
    user = {
        "id": session['user_id']
    }
    return render_template('view.html', recipe= Recipes.get_one_recipe(data), user = Users.get_by_id(user))


@app.route('/recipe/create', methods=['POST'])
def create_recipe():
    if not Recipes.validate_recipe(request.form):
        session['name'] = request.form['name']
        session['description'] = request.form['description']
        session['instructions'] = request.form['instructions']
        return redirect('/recipe/new')
    data = {
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'date_made': request.form['date_made'],
        'cook_time': request.form['cook_time'],
        'user_id': session['user_id']
    }
    Recipes.create_recipe(data)
    return redirect('/recipes')

@app.route('/recipe/delete/<int:id>')
def destroy_recipe(id):
    data = {
        "id": id
    }
    Recipes.delete_post(data)
    return redirect("/recipes")