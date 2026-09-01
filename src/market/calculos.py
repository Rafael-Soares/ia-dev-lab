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


def gerar_ranking_acoes(ativos: Sequence[dict[str, object]]) -> list[dict[str, object]]:
    """Gera o ranking de ativos válidos com base no retorno médio mensal."""
    ranking: list[dict[str, object]] = []

    for ativo in ativos:
        ticker = ativo.get("ticker")
        precos = ativo.get("precos")

        if not isinstance(ticker, str) or not isinstance(precos, Sequence):
            continue

        try:
            retorno_medio = calcular_retorno_medio_mensal(precos)
        except ValueError:
            continue

        ranking.append(
            {
                "ticker": ticker,
                "retorno_medio_mensal": retorno_medio,
            }
        )

    ranking.sort(key=lambda item: item["retorno_medio_mensal"], reverse=True)
    return ranking