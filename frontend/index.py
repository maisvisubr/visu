from flask import Flask, render_template, request, jsonify, make_response
import requests

app = Flask(__name__, static_folder="static")


@app.route("/")
def loginPage():
    return render_template("loginPage.html")


@app.route("/cadastro")
def cadastroPage():
    return render_template("criarConta.html")


@app.route("/pagina_principal")
def paginaPrincipal():
    return render_template("index.html")


@app.route("/verificar_cadastro", methods=["POST"])
def verificarCadastro():
    dadosForm = request.json

    payload = {
        "login": dadosForm["loginInput"],
        "senha": dadosForm["passwordInput"],
        "qtd_moedas": 0.0
    }

    response = requests.post("https://visu-zeta.vercel.app/cadastrar", json=payload).json()

    if bool(response["success"]):
        return make_response(jsonify({"msg": response["msg"]}), 200)

    return make_response(jsonify({"msg": response["msg"]}), 400)


if __name__ == "__main__":
    app.run(debug=True)
