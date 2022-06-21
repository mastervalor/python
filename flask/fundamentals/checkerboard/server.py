from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html", x=8 ,y=8, tile1 = 'black', tile2 ='red')

@app.route('/<int:x>')
def squares(x):
    return render_template("index.html", x=x, y=8, tile1 = 'black', tile2 ='red')

@app.route('/<int:x>/<int:y>')
def size(x, y):
    return render_template("index.html", x=x, y=y, tile1 = 'black', tile2 ='red')

@app.route('/<int:x>/<int:y>/<string:tile1>')
def color(x, y, tile1):
    return render_template("index.html", x=x, y=y, tile1=tile1,  tile2 ='red')

@app.route('/<int:x>/<int:y>/<string:tile1>/<string:tile2>')
def colors(x, y, tile1, tile2):
    return render_template("index.html", x=x, y=y, tile1=tile1, tile2=tile2)


if __name__=="__main__":
    app.run(debug=True)