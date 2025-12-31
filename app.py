from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def input_cep():
    return render_template('input_cep.html')

if __name__ == '__main__':
    app.run(debug=True)