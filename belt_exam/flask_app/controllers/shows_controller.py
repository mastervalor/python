from crypt import methods
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.show_model import Shows
from flask_app.models.user_model import Users
from flask_app.models.like_model import Likes


@app.route('/shows')
def posts():
    if 'user_id' not in session:
        return redirect('/')
    user = {
        "id": session['user_id']
    }
    return render_template('shows.html', user = Users.get_by_id(user), shows =Shows.all_shows(), unliked = Shows.unfavored_show(user), liked = Shows.favored_show(user))

@app.route('/show/new')
def new_show():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('new.html')

@app.route('/show/create', methods=['POST'])
def create_show():
    session['title'] = request.form['title']
    session['description'] = request.form['description']
    session['network'] = request.form['network']
    if not Shows.validate_show(request.form):
        return redirect('/show/new')
    session.pop('title')
    session.pop('description')
    session.pop('network')
    data = {
        'title': request.form['title'],
        'description': request.form['description'],
        'release_date': request.form['release_date'],
        'network': request.form['network'],
        'poster_id': session['user_id']
    }
    Shows.create_show(data)
    return redirect('/shows')

@app.route('/show/view/<int:id>')
def view_show(id):
    if 'user_id' not in session:
            return redirect('/')
    data = {
        "id": id
    }
    user = {
        "id": session['user_id']
    }
    return render_template('view.html', show= Shows.get_one_show(data), user = Users.get_by_id(user),likes=Likes.likes(data))

@app.route('/show/edit/<int:id>')
def edit_show(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": id
    }
    return render_template('edit.html', show= Shows.get_one_show(data))


@app.route('/show/change/<int:id>', methods=["POST"])
def change_show(id):
    if not Shows.validate_show(request.form):
        return redirect(f'/show/change/{id}')
    data = {
        'id': id,
        'title': request.form['title'],
        'description': request.form['description'],
        'release_date': request.form['release_date'],
        'network': request.form['network'],
    }
    Shows.Update_show(data)
    return redirect('/shows')

@app.route('/show/delete/<int:id>')
def destroy_show(id):
    data = {
        "id": id
    }
    Shows.delete_show(data)
    return redirect("/shows")

@app.route('/show/like/<int:id>')
def like_a_show(id):
    data = {
        'show_id': id,
        'user_id': session['user_id']
    }
    Shows.like_show(data)
    return redirect('/shows')


@app.route('/show/unlike/<int:id>')
def unlike_a_show(id):
    data = {
        'show_id': id,
        'user_id': session['user_id']
    }
    Shows.unlike_show(data)
    return redirect('/shows')