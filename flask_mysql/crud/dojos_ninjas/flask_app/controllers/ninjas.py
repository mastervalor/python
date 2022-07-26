from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.ninja import Ninjas
from flask_app.models.dojo import Dojos

@app.route('/ninjas')
def add_ninja():
    return render_template("add_ninja.html", all_dojos= Dojos.get_all())

@app.route('/ninja/create', methods=['POST'])
def create():
    print(request.form)
    Ninjas.save(request.form)
    ninja_id = request.form['dojo_name']
    return redirect(f"/dojos/{ninja_id}")