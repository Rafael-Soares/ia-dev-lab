"""Dados locais de demonstração para o ranking de ações.

Este módulo mantém um conjunto controlado de ativos fictícios para uso em
exemplos e testes de interface. Os dados são intencionalmente separados da
lógica de domínio para manter a regra de negócio isolada em calculos.py.
"""

DADOS_DEMO: dict[str, list[float]] = {
    "DEMO_A": [100.0, 110.0, 121.0, 133.1, 146.41, 161.051, 177.1561],
    "DEMO_B": [
        100.0,
        105.0,
        110.25,
        115.7625,
        121.550625,
        127.62815625,
        134.0095640625,
    ],
    "DEMO_C": [
        100.0,
        95.0,
        90.25,
        85.7375,
        81.450625,
        77.37809375,
        73.5091890625,
    ],
    "DEMO_INVALIDO": [100.0, 105.0, 0.0, 115.0, 121.0, 130.0, 140.0],
    "DEMO_INCOMPLETO": [100.0, 105.0, 110.0, 115.0],
}


def get_dados_demo() -> dict[str, list[float]]:
    """Retorna uma cópia dos dados de demonstração."""
    return {
        ticker: list(precos)
        for ticker, precos in DADOS_DEMO.items()
    }