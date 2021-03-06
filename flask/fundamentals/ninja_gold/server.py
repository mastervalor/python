from flask import Flask, render_template, redirect, session, request
import random, datetime
app = Flask(__name__)
app.secret_key = 'ef2f2bfiheb29e8y2389fdhd2be9d28hfb923eg8fh'


@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
        session['turn'] = 0
        session['message'] = []
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process():
    buildings = {"farm": {"min":10,"max":20}, "cave": {"min": 5, "max":10}, "house": {"min": 2, "max": 5}, "casino": {"min": -50, "max": 50}}
    building = request.form['building']
    minumum = buildings[building]["min"]
    maximum = buildings[building]["max"]
    new = random.randint(minumum,maximum)
    ct= datetime.datetime.now().strftime('%x %-I:%M %p')
    if building == 'casino':
        if new >= 0:
            session['message'].append(f'<p class="text-success">Entered a casino and won {new} golds... YAY.. ({ct})</p>')
        else:
            session['message'].append(f'<p class="text-danger">Entered a casino and lost {new} golds... Ouch.. ({ct})</p>')
    else:
        session['message'].append(f'<p class="text-success">Earned {new} golds from {building}! ({ct})</p>')
    session['gold'] += new
    session['turn'] += 1
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True, port=5001)