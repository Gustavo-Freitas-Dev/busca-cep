from flask import Flask, render_template, request
from viacep import consultar_cep

app = Flask(__name__)

@app.route('/')
def input_cep():
    return render_template('input_cep.html')

@app.route("/result", methods=["POST"])
def result():
    cep = request.form.get("cep")

    if not cep:
        return "CEP não informado", 400

    resultado = consultar_cep(cep)

    if "erro" in resultado:
        return resultado["erro"], 400

    return render_template("result.html", endereco=resultado)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    # app.run(debug=True)
