from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('ruwiki.html')

@app.route("/add_article", methods=["GET", "POST"])
def add_article():
    if request.method =="GET":
        return render_template("add_article.html")
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)
