from flask import Flask, render_template, request, redirect
#from users import users
from users import users

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", all_users = users.get_all())

@app.route("/new")
def input():
    return render_template("new.html")

@app.route("/new_user", methods=["POST"])
def new():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }
    users.save(data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, port=5001)