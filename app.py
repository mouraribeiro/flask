from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///mercado.db'
db.init_app(app)

@app.route('/')
def page_home():
    return render_template("home.html")


@app.route('/produtos')
def page_produtos():
    itens = [
        {'id': 1, 'nome': 'Celular', 'cod_barra': '254872', 'preco': 1200},
        {'id': 2, 'nome': 'Impressora', 'cod_barra': '254873', 'preco': 1500},
        {'id': 3, 'nome': 'Notebook', 'cod_barra': '254874', 'preco': 1600},
        {'id': 4, 'nome': 'Tablet', 'cod_barra': '254875', 'preco': 1800},
    ]
    return render_template("products.html", itens=itens)

