from crypt import methods
from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = 'ef2f2bfiheb29e8y2389fdhd2be9d28hfb923eg8fh'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return render_template("result.html", name=session['name'], location=session['location'],
                            language=session['language'], comment=session['comment'])
    
@app.route('/return', methods=['POST'])
def going_back():
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)