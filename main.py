import sqlite3
from flask import Flask
app = Flask(__name__)

DATABASE = 'database.db'


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/estados/<nome>')
def get_capital(nome):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT capital FROM estados WHERE nome = '{}';".format(nome))
    linha = cursor.fetchone();
    conn.close()
    return 'Capital: {}'.format(linha[0])


if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0', use_reloader=False)
