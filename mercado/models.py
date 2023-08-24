from mercado import db

class Item(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nome = db.Column(db.String(length=30),nullable=False,unique=True)
    codigo_barra = db.Column(db.String(length=12),nullable=False,unique=True)
    preco = db.Column(db.Integer,nullable=False)
    descricao = db.Column(db.String(length=1024),nullable=False,unique=True)
    
    def __repr__(self):
        return f'Item: {self.nome}'