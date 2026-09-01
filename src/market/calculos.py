from collections.abc import Sequence
from numbers import Real


def calcular_retorno_medio_mensal(precos: Sequence[float]) -> float:
    """Calcula a média dos retornos percentuais de seis meses."""
    if len(precos) != 7:
        raise ValueError("É necessário informar exatamente 7 preços.")

    if any(isinstance(preco, bool) or not isinstance(preco, Real) for preco in precos):
        raise ValueError("Todos os preços devem ser numéricos.")

    if any(preco <= 0 for preco in precos):
        raise ValueError("Todos os preços devem ser maiores que zero.")

    retornos = [
        ((preco_atual / preco_anterior) - 1) * 100
        for preco_anterior, preco_atual in zip(precos, precos[1:])
    ]

    return sum(retornos) / len(retornos)