import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as test_client:
        yield test_client


def test_ranking_exibe_resultados_com_campos_obrigatorios(monkeypatch, client):
    ranking = [
        {
            "ticker": "ALFA",
            "retorno_medio_mensal_percentual": 10.0,
            "tendencia": "POSITIVA",
        },
        {
            "ticker": "BETA",
            "retorno_medio_mensal_percentual": 5.0,
            "tendencia": "POSITIVA",
        },
    ]

    monkeypatch.setattr("app.gerar_ranking", lambda _ativos: ranking)

    response = client.get("/ranking")
    body = response.get_data(as_text=True)

    assert response.status_code == 200

    assert "Posição" in body
    assert "Ticker" in body
    assert "Retorno médio mensal" in body
    assert "Tendência" in body

    assert "ALFA" in body
    assert "10.00%" in body
    assert "POSITIVA" in body
    assert "BETA" in body
    assert "5.00%" in body

    assert ">1<" in body
    assert ">2<" in body


def test_ranking_preserva_ordem_dos_resultados(monkeypatch, client):
    ranking = [
        {
            "ticker": "PRIMEIRO",
            "retorno_medio_mensal_percentual": 8.0,
            "tendencia": "POSITIVA",
        },
        {
            "ticker": "SEGUNDO",
            "retorno_medio_mensal_percentual": 4.0,
            "tendencia": "POSITIVA",
        },
        {
            "ticker": "TERCEIRO",
            "retorno_medio_mensal_percentual": 1.0,
            "tendencia": "POSITIVA",
        },
    ]

    monkeypatch.setattr("app.gerar_ranking", lambda _ativos: ranking)

    response = client.get("/ranking")
    body = response.get_data(as_text=True)

    assert response.status_code == 200

    assert (
        body.index("PRIMEIRO")
        < body.index("SEGUNDO")
        < body.index("TERCEIRO")
    )


def test_ranking_vazio_exibe_mensagem_clara(monkeypatch, client):
    monkeypatch.setattr("app.gerar_ranking", lambda _ativos: [])

    response = client.get("/ranking")
    body = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "Nenhum resultado disponível" in body


def test_ranking_exibe_subconjunto_valido_recebido(monkeypatch, client):
    ranking = [
        {
            "ticker": "VALIDO_A",
            "retorno_medio_mensal_percentual": 10.0,
            "tendencia": "POSITIVA",
        },
        {
            "ticker": "VALIDO_B",
            "retorno_medio_mensal_percentual": 5.0,
            "tendencia": "POSITIVA",
        },
    ]

    monkeypatch.setattr("app.gerar_ranking", lambda _ativos: ranking)

    response = client.get("/ranking")
    body = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "VALIDO_A" in body
    assert "VALIDO_B" in body
    assert body.index("VALIDO_A") < body.index("VALIDO_B")