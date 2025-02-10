from . import db

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(50), unique=True, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    lotes = db.relationship('Lote', backref='produto', lazy=True)

    def adicionar_lote(self, preco, quantidade):
        novo_lote = Lote(preco=preco, quantidade=quantidade, produto_id=self.id)
        db.session.add(novo_lote)

    def remover_lote(self, lote_id):
        lote = Lote.query.get(lote_id)
        if lote:
            db.session.delete(lote)

    def atualizar_preco_lote(self, lote_id, novo_preco):
        lote = Lote.query.get(lote_id)
        if lote:
            lote.preco = novo_preco

class Lote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    preco = db.Column(db.Float, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'), nullable=False)
