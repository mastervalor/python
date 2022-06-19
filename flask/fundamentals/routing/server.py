from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo'

@app.route('/<string:word>')
def word(word):
    return 'Hi ' + word

@app.route('/repeat/<int:mult>/<string:words>')
def mult(words, mult):
    return words * mult

if __name__=="__main__":
    app.run(debug=True)