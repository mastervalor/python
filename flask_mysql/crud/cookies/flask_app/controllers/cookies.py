from crypt import methods
from flask import render_template, request, redirect, session
from flask_app.models.cookie import Cookie
from flask_app import app

@app.route('/')
def default():
    return redirect('/cookies')

@app.route('/cookies')
def index():
    return render_template("index.html", all_cookies = Cookie.get_all())

@app.route('/cookie/new')
def input():
    return render_template("new.html")

@app.route('/cookie/create', methods=["POST"])
def new():
    if not Cookie.validate_cookie(request.form):
        session['name'] = request.form['name']
        session['cookie'] = request.form['cookie']
        session['boxes'] = request.form['boxes']
        return redirect('/cookie/new')
    session.pop('name')
    session.pop('cookie')
    session.pop('boxes')
    Cookie.save(request.form)
    return redirect(f'/cookies')

@app.route("/cookie/update", methods=["POST"])
def update():
    if not Cookie.validate_cookie(request.form):
        session['name'] = request.form['name']
        session['cookie'] = request.form['cookie']
        session['boxes'] = request.form['boxes']
        return redirect('/cookie/new')
    session.pop('name')
    session.pop('cookie')
    session.pop('boxes')
    Cookie.updated(request.form)
    return redirect('/cookies')

@app.route("/cookie/edit/<int:id>")
def edit(id):
    data= {
        'id':id
    }
    return render_template("edit.html", cookie = Cookie.get_one(data))