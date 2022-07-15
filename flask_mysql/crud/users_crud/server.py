from flask import Flask, render_template, request, redirect
from users import users

app = Flask(__name__)

@app.route("/users")
def index():
    return render_template("index.html", all_users = users.get_all())

@app.route("/user/new")
def input():
    return render_template("new.html")

@app.route("/user/create", methods=["POST"])
def new():
    new_id = users.save(request.form)
    return redirect(f'/user/show/{new_id}')

@app.route("/user/update", methods=["POST"])
def update():
    users.updated(request.form)
    return redirect('/users')

@app.route("/user/edit/<int:id>")
def edit(id):
    data = {
        "id": id
    }
    return render_template("edit.html", user= users.get_one(data))

@app.route("/user/delete/<int:id>")
def delete(id):
    data = {
        "id": id
    }
    users.delete(data)
    return redirect('/users')

@app.route("/user/show/<int:id>")
def show(id):
    data = {
        "id": id
    }
    return render_template("show.html", user= users.get_one(data))


if __name__ == "__main__":
    app.run(debug=True, port=5001)