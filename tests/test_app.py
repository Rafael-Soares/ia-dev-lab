from app import app


def test_ranking_route_responde_com_sucesso_e_exibe_campos_obrigatorios(monkeypatch):
    ranking = [
        {"ticker": "AAA", "retorno_medio_mensal": 10.0},
        {"ticker": "BBB", "retorno_medio_mensal": 5.0},
    ]

    monkeypatch.setattr(
        "app.gerar_ranking_acoes",
        lambda _ativos: ranking,
    )

    response = app.test_client().get("/ranking")
    html = response.get_data(as_text=True)

    assert response.status_code == 200

    assert "Posição" in html
    assert "Ticker" in html
    assert "Retorno médio mensal" in html

    assert "AAA" in html
    assert "10.00%" in html
    assert "BBB" in html
    assert "5.00%" in html

    assert ">1<" in html
    assert ">2<" in html


def test_ranking_route_preserva_ordem_e_exibe_subconjunto_valido(monkeypatch):
    ranking = [
        {"ticker": "AAA", "retorno_medio_mensal": 10.0},
        {"ticker": "BBB", "retorno_medio_mensal": 5.0},
        {"ticker": "CCC", "retorno_medio_mensal": 2.0},
    ]

    monkeypatch.setattr(
        "app.gerar_ranking_acoes",
        lambda _ativos: ranking,
    )

    response = app.test_client().get("/ranking")
    html = response.get_data(as_text=True)

    assert response.status_code == 200

    assert html.index("AAA") < html.index("BBB") < html.index("CCC")

    assert "AAA" in html
    assert "BBB" in html
    assert "CCC" in html


def test_ranking_route_exibe_mensagem_quando_nao_ha_resultados(monkeypatch):
    monkeypatch.setattr(
        "app.gerar_ranking_acoes",
        lambda _ativos: [],
    )

    response = app.test_client().get("/ranking")
    html = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "Nenhum resultado disponível no ranking no momento." in html