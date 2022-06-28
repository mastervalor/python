from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = 'ef2f2bfiheb29e8y2389fdhd2be9d28hfb923eg8fh'

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] += 1
        session['total'] += 1
    return render_template("index.html")


@app.route('/reset')
def reset():
    #session.clear()
    session.pop('count')
    return redirect('/')

@app.route('/double')
def double():
    session['count'] += 1
    session['total'] += 1
    return redirect('/')

@app.route('/increment', methods = ["POST"])
def increment():
    session['count'] = session['count'] + int(request.form['increment']) - 1
    session['total'] = session['total'] + int(request.form['increment']) - 1
    return redirect('/')

@app.route('/destroy_session')
def destroy():
    # session.clear()
    session.pop('count')
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)