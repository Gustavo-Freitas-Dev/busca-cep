from flask import Flask, render_template, request
from viacep import consultar_cep

app = Flask(__name__)

@app.route('/')
def input_cep():
    return render_template('input_cep.html')

@app.route("/result", methods=["POST"])
def result():
    cep = request.form.get("cep")
    resultado = consultar_cep(cep)

    if "erro" in resultado:
        return resultado["erro"], 400

    return resultado  # ou render_template(...)


if __name__ == '__main__':
    app.run(debug=True)