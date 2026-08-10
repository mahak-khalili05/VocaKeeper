from flask import Flask, render_template, request, redirect
from database import show_words, add_word

app = Flask(__name__)


@app.route("/")
def home():
    words = show_words()
    return render_template("index.html", words=words)


@app.route("/add", methods=["GET", "POST"])
def add():

    if request.method == "POST":

        korean = request.form["korean"]
        persian = request.form["persian"]

        add_word(korean, persian)

        return redirect("/")

    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
