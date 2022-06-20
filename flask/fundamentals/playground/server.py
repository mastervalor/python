from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def main():
    return render_template("play.html", num=3 ,color="blue")

@app.route('/play/<int:num>')
def squares(num):
    return render_template("play.html", num=num, color="blue")

@app.route('/play/<int:num>/<string:color>')
def color(num, color):
    return render_template("play.html", num=num, color=color)

if __name__=="__main__":
    app.run(debug=True)