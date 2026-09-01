import pytest

from src.market.calculos import (
    calcular_retorno_medio_mensal,
    gerar_ranking_acoes,
)


def _precos_com_crescimento(percentual: float) -> list[float]:
    precos = [100.0]
    for _ in range(6):
        precos.append(precos[-1] * (1 + percentual / 100))
    return precos


def test_retorno_medio_de_seis_meses():
    precos = [100, 110, 121, 133.1, 146.41, 161.051, 177.1561]

    resultado = calcular_retorno_medio_mensal(precos)

    assert resultado == pytest.approx(10.0)


def test_quantidade_incorreta_de_precos():
    with pytest.raises(ValueError, match="exatamente 7 preços"):
        calcular_retorno_medio_mensal([100, 110, 120])


def test_preco_zero():
    with pytest.raises(ValueError, match="maiores que zero"):
        calcular_retorno_medio_mensal(
            [100, 110, 121, 133.1, 146.41, 0, 177.1561]
        )


def test_valor_nao_numerico():
    with pytest.raises(ValueError, match="devem ser numéricos"):
        calcular_retorno_medio_mensal(
            [100, 110, 121, 133.1, 146.41, "160", 177.1561]
        )


def test_gerar_ranking_acoes_com_multiplos_ativos_validos():
    ativos = [
        {"ticker": "AAA", "precos": _precos_com_crescimento(10)},
        {"ticker": "BBB", "precos": _precos_com_crescimento(5)},
        {"ticker": "CCC", "precos": _precos_com_crescimento(2)},
    ]

    resultado = gerar_ranking_acoes(ativos)

    assert [item["ticker"] for item in resultado] == ["AAA", "BBB", "CCC"]
    assert [item["retorno_medio_mensal"] for item in resultado] == pytest.approx(
        [10.0, 5.0, 2.0]
    )


def test_gerar_ranking_acoes_exclui_ativos_invalidos():
    ativos = [
        {"ticker": "AAA", "precos": _precos_com_crescimento(10)},
        {"ticker": "INV", "precos": [100, 110, 121, 133.1, 146.41, 0, 177.1561]},
    ]

    resultado = gerar_ranking_acoes(ativos)

    assert resultado == [{"ticker": "AAA", "retorno_medio_mensal": pytest.approx(10.0)}]


def test_gerar_ranking_acoes_retorna_lista_vazia_quando_nao_ha_ativos_validos():
    ativos = [
        {"ticker": "INV1", "precos": [100, 110, 121, 133.1, 146.41, 0, 177.1561]},
        {"ticker": "INV2", "precos": [100, 110, 120, 130, 140, 150]},
    ]

    assert gerar_ranking_acoes(ativos) == []