from flask import Flask, render_template, request, redirect, url_for
from src.gastos import adicionar_gasto, listar_gastos, total_gastos, remover_gasto
from src.services import buscar_cotacao

app = Flask(__name__, template_folder="../templates")


@app.route("/")
def index():
    gastos = listar_gastos()
    total = total_gastos()
    cotacao = buscar_cotacao()
    return render_template("index.html", gastos=gastos, total=total, cotacao=cotacao)


@app.route("/adicionar", methods=["POST"])
def adicionar():
    try:
        descricao = request.form["descricao"]
        valor = float(request.form["valor"])
        categoria = request.form["categoria"]
        adicionar_gasto(descricao, valor, categoria)
    except ValueError:
        pass
    return redirect(url_for("index"))


@app.route("/remover/<int:indice>")
def remover(indice):
    try:
        remover_gasto(indice)
    except IndexError:
        pass
    return redirect(url_for("index"))


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)