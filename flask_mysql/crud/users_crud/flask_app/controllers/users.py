from flask import render_template, request, redirect, session, flash
from flask_app.models.user import Users
from flask_app import app
from flask_bcrypt import Bcrypt  

bcrypt = Bcrypt(app)

@app.route('/')
def default():
    return redirect('/users')

@app.route("/users")
def index():
    return render_template("index.html", all_users = Users.get_all())

@app.route("/user/new")
def input():
    return render_template("new.html")

@app.route("/user/create", methods=["POST"])
def new():
    if not Users.validate_user(request.form):
        session['fname'] = request.form['fname']
        session['lname'] = request.form['lname']
        session['email'] = request.form['email']
        return redirect ('/user/new')
    session.pop('fname')
    session.pop('lname')
    session.pop('email')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    
    data = {
        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "email": request.form['email'],
        "password" : pw_hash
    }

    new_id = Users.save(data)

    session['user_id'] = new_id
    return redirect(f'/user/show/{new_id}')

@app.route("/user/update", methods=["POST"])
def update():
    Users.updated(request.form)
    return redirect('/users')

@app.route("/user/edit/<int:id>")
def edit(id):
    data = {
        "id": id
    }
    return render_template("edit.html", user= Users.get_one(data))

@app.route("/user/delete/<int:id>")
def delete(id):
    data = {
        "id": id
    }
    Users.delete(data)
    return redirect('/users')

@app.route("/user/show/<int:id>")
def show(id):
    data = {
        "id": id
    }
    return render_template("show.html", user= Users.get_one(data))

@app.route('/login', methods=['POST'])
def login():
    # see if the username provided exists in the database
    data = { "email" : request.form["email"] }
    user_in_db = Users.get_by_email(data)
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/users")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password")
        return redirect('/users')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    # never render on a post!!!
    return redirect(f'/users')