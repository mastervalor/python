from crypt import methods
from flask import Flask, render_template, redirect, session, request
import random
app = Flask(__name__)
app.secret_key = 'ef2f2bfiheb29e8y2389fdhd2be9d28hfb923eg8fh'


@app.route('/')
def index():
    if "num" not in session:
        session['num'] = random.randint(1,100)
    return render_template("index.html")

@app.route('/guess',methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)