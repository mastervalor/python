from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.dojo import Dojos

@app.route('/')
def start():
    return redirect('/dojos')

@app.route("/dojos")
def index():
    return render_template("dojos.html", all_dojos = Dojos.get_all())

@app.route("/dojo/create", methods=['POST'])
def new_dojo():
    Dojos.save(request.form)
    return redirect('/dojos')
    
@app.route("/dojos/<int:dojo_id>")
def show(dojo_id):
    data = {
        'id': dojo_id
    }
    return render_template('dojo_ninjas.html', all_ninjas=Dojos.get_dojos_with_ninjas(data))