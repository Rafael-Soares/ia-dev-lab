# Diagrama C4 — Versão 2

```mermaid
C4Container
    Person(user, "Usuário", "Pessoa que acessa o ranking de ações")

    System_Boundary(system, "ia-dev-lab") {
        Container(
            web,
            "Aplicação Web Flask",
            "Python, Flask e Jinja2",
            "Entrada e roteamento em app.py; dados locais em memória; cálculo do ranking em calculos.py; renderização de ranking.html"
        )
    }

    Rel(user, web, "Acessa o ranking", "HTTP")