"""Dados controlados de demonstração para o ranking de ações.

Este módulo mantém um conjunto de ativos fictícios que podem ser substituídos por
uma fonte externa futura sem alterar a lógica de cálculo do ranking.
"""

from __future__ import annotations


def _precos_por_crescimento(percentual: float) -> list[float]:
    """Cria 7 preços mensais em ordem cronológica a partir de uma taxa de crescimento."""
    precos = [100.0]

    for _ in range(6):
        precos.append(precos[-1] * (1 + percentual / 100))

    return precos


def obter_dados_demonstracao() -> list[dict[str, object]]:
    """Retorna ativos fictícios usados apenas para demonstração local."""
    return [
        {"ticker": "DEMO_A", "precos": _precos_por_crescimento(10)},
        {"ticker": "DEMO_B", "precos": _precos_por_crescimento(4)},
        {"ticker": "DEMO_C", "precos": _precos_por_crescimento(8)},
        {"ticker": "DEMO_D", "precos": _precos_por_crescimento(1)},
        {
            "ticker": "DEMO_INCOMPLETO",
            "precos": [100.0, 102.0, 104.0, 106.0, 108.0],
        },
        {
            "ticker": "DEMO_INVALIDO",
            "precos": [100.0, 110.0, 0.0, 120.0, 130.0, 140.0, 150.0],
        },
    ]