from .models import Produto, Lote, db

def adicionar_produto(codigo: str, nome: str):
    produto = Produto.query.filter_by(codigo=codigo).first()

    if not produto:
        produto = Produto(codigo=codigo, nome=nome)
        db.session.add(produto)
        db.session.commit()
        return produto
    return None

def buscar_produto(codigo: str):
    return Produto.query.filter_by(codigo=codigo).first()

def adicionar_lote(codigo_produto: str, preco: float, quantidade: int):
    produto = buscar_produto(codigo_produto)
    
    if produto:
        produto.adicionar_lote(preco, quantidade)
        db.session.commit()
        return produto
    return None

def remover_lote(lote_id: int):
    lote = Lote.query.get(lote_id)
    
    if lote:
        db.session.delete(lote)
        db.session.commit()
        return True
    return False

def atualizar_preco_lote(lote_id: int, novo_preco: float):
    lote = Lote.query.get(lote_id)

    if lote:
        lote.preco = novo_preco
        db.session.commit()
        return True
    return False

def listar_produtos():
    return Produto.query.all()

def clear_db():
    db.drop_all()
    db.create_all()
    return{"message": "Banco de dados limpo com sucesso"}


