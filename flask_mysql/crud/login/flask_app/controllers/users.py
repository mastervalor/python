from flask_bcrypt import Bcrypt
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import Users
from flask_app.models.language import Languages

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("index.html", all_languages=Languages.get_languages())

@app.route('/user/create', methods=['POST'])
def create():
    if not Users.validate_user(request.form):
        session['first_name'] = request.form['first_name']
        session['last_name'] = request.form['last_name']
        session['email'] = request.form['email']
        return redirect('/')
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password']),
        "birthdate": request.form['birthdate'],
        "age": request.form['age'],
        "location": request.form['location'],
    }
    new_id = Users.save(data)
    session['user_id'] = new_id
    lang_data =  request.form.getlist('languages')
    for i in lang_data:
        user_data ={
            'language_id': i,
            'user_id': new_id
        }
        Languages.add_languages(user_data)
    return redirect('/dashboard')

@app.route('/user/login',methods=['POST'])
def login():
    user = Users.get_by_email(request.form)
    if not user:
        flash("Invalid Email","login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password","login")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/dashboard')
    
@app.route('/dashboard')
def show():
    data = {
        "id": session['user_id']
    }
    userssss= Users.get_by_id(data)
    print(userssss.location)
    return render_template("show.html", user=Users.get_by_id(data), languages=Languages.get_languages_by_user_id(data))

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')