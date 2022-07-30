from flask import render_template, request, redirect, session
from flask_app.models.user import Users
from flask_app import app

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
    new_id = Users.save(request.form)
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
