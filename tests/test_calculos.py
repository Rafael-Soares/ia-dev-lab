import pytest

from src.market.calculos import calcular_retorno_medio_mensal


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