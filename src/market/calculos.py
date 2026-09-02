from collections.abc import Mapping, Sequence
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


def gerar_ranking(ativos: Mapping[str, Sequence[float]]) -> list[dict[str, float | str]]:
    """Gera o ranking dos ativos válidos em ordem decrescente de desempenho."""
    resultados = []

    for ticker, precos in ativos.items():
        try:
            retorno = calcular_retorno_medio_mensal(precos)
        except ValueError:
            continue

        resultados.append(
            {
                "ticker": ticker,
                "retorno_medio_mensal_percentual": retorno,
            }
        )

    return sorted(
        resultados,
        key=lambda item: item["retorno_medio_mensal_percentual"],
        reverse=True,
    )