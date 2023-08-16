from flask import Flask, render_template

app = Flask(__name__, static_folder="static")


@app.route("/")
def loginPage():
    return render_template("loginPage.html")


@app.route("/cadastro")
def cadastroPage():
    return render_template("criarConta.html")


if __name__ == "__main__":
    app.run(debug=True)
