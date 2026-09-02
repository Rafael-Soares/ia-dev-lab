import pytest

from src.market import calculos


def test_retorno_medio_de_seis_meses():
    precos = [100, 110, 121, 133.1, 146.41, 161.051, 177.1561]

    resultado = calculos.calcular_retorno_medio_mensal(precos)

    assert resultado == pytest.approx(10.0)


def test_quantidade_incorreta_de_precos():
    with pytest.raises(ValueError, match="exatamente 7 preços"):
        calculos.calcular_retorno_medio_mensal([100, 110, 120])


def test_preco_zero():
    with pytest.raises(ValueError, match="maiores que zero"):
        calculos.calcular_retorno_medio_mensal(
            [100, 110, 121, 133.1, 146.41, 0, 177.1561]
        )


def test_valor_nao_numerico():
    with pytest.raises(ValueError, match="devem ser numéricos"):
        calculos.calcular_retorno_medio_mensal(
            [100, 110, 121, 133.1, 146.41, "160", 177.1561]
        )


def test_ranking_multiplos_ativos_validos():
    ativos = {
        "ALFA": [100, 110, 121, 133.1, 146.41, 161.051, 177.1561],
        "BETA": [100, 105, 110.25, 115.7625, 121.550625, 127.62815625, 134.0095640625],
        "GAMA": [100, 95, 90.25, 85.7375, 81.450625, 77.37809375, 73.5091890625],
    }

    ranking = calculos.gerar_ranking(ativos)

    assert [item["ticker"] for item in ranking] == ["ALFA", "BETA", "GAMA"]
    assert [
        item["retorno_medio_mensal_percentual"] for item in ranking
    ] == pytest.approx([10.0, 5.0, -5.0])


def test_ranking_ignora_ativos_invalidos_e_incompletos():
    ativos = {
        "VALIDO_A": [100, 110, 121, 133.1, 146.41, 161.051, 177.1561],
        "INVALIDO_NULO": [100, 105, None, 115, 121, 130, 140],
        "INCOMPLETO": [100, 105, 110, 115],
        "VALIDO_B": [
            90,
            94.5,
            99.225,
            104.18625,
            109.3955625,
            114.865340625,
            120.60860765625,
        ],
    }

    ranking = calculos.gerar_ranking(ativos)

    assert [item["ticker"] for item in ranking] == ["VALIDO_A", "VALIDO_B"]


def test_ranking_vazio_quando_todos_ativos_invalidos():
    ativos = {
        "A": [100, 101, 102, 103, 104, 105],
        "B": [50, 0, 55, 60, 65, 70, 75],
        "C": [100, "110", 121, 133.1, 146.41, 161.051, 177.1561],
    }

    ranking = calculos.gerar_ranking(ativos)

    assert ranking == []