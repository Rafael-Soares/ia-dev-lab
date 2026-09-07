from collections.abc import Mapping, Sequence
from numbers import Real


def classificar_tendencia(retorno_medio_mensal: float) -> str:
    """Classifica a tendência com base no retorno médio mensal."""
    if retorno_medio_mensal > 0:
        return "POSITIVA"
    if retorno_medio_mensal < 0:
        return "NEGATIVA"
    return "NEUTRA"


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
                "tendencia": classificar_tendencia(retorno),
            }
        )

    return sorted(
        resultados,
        key=lambda item: item["retorno_medio_mensal_percentual"],
        reverse=True,
    )


def filtrar_ranking_por_retorno_minimo(
    ranking: Sequence[Mapping[str, float | str]],
    retorno_minimo: float,
) -> list[dict[str, float | str]]:
    """Mantém os ativos que atingem o retorno mínimo, preservando a ordem."""
    return [
        dict(item)
        for item in ranking
        if item["retorno_medio_mensal_percentual"] >= retorno_minimo
    ]


def limitar_ranking(
    ranking: Sequence[dict[str, float | str]],
    quantidade_maxima: int,
) -> list[dict[str, float | str]]:
    """Retorna os primeiros itens do ranking até o limite informado."""
    if quantidade_maxima < 0:
        raise ValueError("A quantidade máxima deve ser maior ou igual a zero.")

    return list(ranking[:quantidade_maxima])