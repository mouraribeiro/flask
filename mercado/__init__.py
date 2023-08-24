from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///mercado.db'
app.config["SECRET_KEY"] = 'f9f81254da3d1952951a8e63'
db.init_app(app)




from mercado import routes