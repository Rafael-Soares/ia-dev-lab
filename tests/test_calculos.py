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


def test_classificar_tendencia_baseada_no_retorno_medio_mensal():
    assert calculos.classificar_tendencia(10.0) == "POSITIVA"
    assert calculos.classificar_tendencia(-5.0) == "NEGATIVA"
    assert calculos.classificar_tendencia(0.0) == "NEUTRA"


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
    assert [item["tendencia"] for item in ranking] == ["POSITIVA", "POSITIVA", "NEGATIVA"]


def test_ranking_com_tendencia_neutra():
    ativos = {"NEUTRA": [100, 100, 100, 100, 100, 100, 100]}

    ranking = calculos.gerar_ranking(ativos)

    assert ranking == [{"ticker": "NEUTRA", "retorno_medio_mensal_percentual": 0.0, "tendencia": "NEUTRA"}]


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


def test_limitar_ranking_retorna_primeiros_itens_ate_limite():
    ranking = [{"ticker": "A"}, {"ticker": "B"}, {"ticker": "C"}]

    resultado = calculos.limitar_ranking(ranking, 2)

    assert resultado == [{"ticker": "A"}, {"ticker": "B"}]


def test_limitar_ranking_preserva_ordem_original():
    ranking = [{"ticker": "C"}, {"ticker": "A"}, {"ticker": "B"}]

    resultado = calculos.limitar_ranking(ranking, 3)

    assert [item["ticker"] for item in resultado] == ["C", "A", "B"]


def test_limitar_ranking_com_limite_zero_retorna_lista_vazia():
    ranking = [{"ticker": "A"}]

    resultado = calculos.limitar_ranking(ranking, 0)

    assert resultado == []


def test_limitar_ranking_com_limite_negativo_gera_value_error():
    with pytest.raises(ValueError, match="maior ou igual a zero"):
        calculos.limitar_ranking([], -1)


def test_limitar_ranking_com_limite_maior_que_ranking_retorna_todos():
    ranking = [{"ticker": "A"}, {"ticker": "B"}]

    resultado = calculos.limitar_ranking(ranking, 5)

    assert resultado == ranking


def test_limitar_ranking_vazio_retorna_lista_vazia():
    resultado = calculos.limitar_ranking([], 3)

    assert resultado == []


def test_limitar_ranking_nao_modifica_lista_original():
    ranking = [{"ticker": "A"}, {"ticker": "B"}, {"ticker": "C"}]
    ranking_original = ranking.copy()

    resultado = calculos.limitar_ranking(ranking, 2)

    assert ranking == ranking_original
    assert resultado is not ranking