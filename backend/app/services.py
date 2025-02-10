def validar_codigo_produto(codigo: str) -> bool:
    """Verifica se o código do produto é válido (exemplo: apenas números e letras)."""
    return codigo.isalnum()

def calcular_valor_total_lotes(lotes) -> float:
    """Calcula o valor total do estoque de um produto com base nos lotes cadastrados."""
    return sum(lote.preco * lote.quantidade for lote in lotes)
