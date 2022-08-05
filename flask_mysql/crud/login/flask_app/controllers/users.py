from crypt import methods
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import Users
from flask_app.models.language import Languages

@app.route('/')
def index():
    return render_template("index.html", all_languages=Languages.get_languages())

@app.route('/user/create', methods=['POST'])
def create(cls, data):
    if not Users.validate_user(request.form):
        session['first_name'] = request.form['first_name']
        session['last_name'] = request.form['last_name']
        session['email'] = request.form['email']
        return redirect('/')
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": request.form['password'],
        "birthdate": request.form['birthdate'],
        "age": request.form['age'],
        "location": request.form['location'],
        "languages": request.form['languages']
    }
    new_id = Users.save(data)
    session['user_id'] = new_id
    return redirect(f'/user/show/{new_id}')

@app.route('user/show/<int:id>')
def show(id):
    data = {
        "id": id
    }
    return render_template("show.html", )