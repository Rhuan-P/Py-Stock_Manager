from flask import Blueprint, request, jsonify
from .controllers import (
    adicionar_produto, buscar_produto, adicionar_lote, remover_lote, 
    atualizar_preco_lote, listar_produtos
)

bp = Blueprint('product', __name__, url_prefix='/api')

@bp.route('/produtos', methods=['POST'])
def criar_produto():
    data = request.get_json()
    produto = adicionar_produto(data['codigo'], data['nome'])

    if produto:
        return jsonify({"message": "Produto adicionado com sucesso"}), 201
    return jsonify({"message": "Produto já existe"}), 400

@bp.route('/produtos', methods=['GET'])
def listar_todos_produtos():
    produtos = listar_produtos()
    return jsonify([{"codigo": p.codigo, "nome": p.nome} for p in produtos])

@bp.route('/produto/<codigo>', methods=['GET'])
def obter_produto(codigo):
    produto = buscar_produto(codigo)
    
    if produto:
        return jsonify({
            "codigo": produto.codigo,
            "nome": produto.nome,
            "lotes": [{"id": l.id, "preco": l.preco, "quantidade": l.quantidade} for l in produto.lotes]
        })
    return jsonify({"message": "Produto não encontrado"}), 404

@bp.route('/produto/<codigo>/lote', methods=['POST'])
def criar_lote(codigo):
    data = request.get_json()
    produto = adicionar_lote(codigo, data['preco'], data['quantidade'])

    if produto:
        return jsonify({"message": "Lote adicionado com sucesso"}), 201
    return jsonify({"message": "Produto não encontrado"}), 404

@bp.route('/lote/<int:lote_id>', methods=['DELETE'])
def excluir_lote(lote_id):
    if remover_lote(lote_id):
        return jsonify({"message": "Lote removido com sucesso"}), 200
    return jsonify({"message": "Lote não encontrado"}), 404

@bp.route('/lote/<int:lote_id>', methods=['PUT'])
def atualizar_preco_lote_route(lote_id):
    data = request.get_json()
    if atualizar_preco_lote(lote_id, data['preco']):
        return jsonify({"message": "Preço atualizado"}), 200
    return jsonify({"message": "Lote não encontrado"}), 404
