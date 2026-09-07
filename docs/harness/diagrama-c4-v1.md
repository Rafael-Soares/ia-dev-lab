# Diagrama C4 — Versão 1

```mermaid
flowchart LR
    Usuario(("Usuário"))

    subgraph Aplicacao["Aplicação atual"]
        Flask["Aplicação Web Flask (app.py)"]
        Dados["Fonte de dados de demonstração (src/market/dados_demo.py)"]
        Dominio["Módulo de domínio (src/market/calculos.py)"]
        Template["Template Jinja2 (templates/ranking.html)"]
    end

    Usuario -->|"requisição HTTP"| Flask
    Flask -->|"obtém dados"| Dados
    Dados -->|"dados de demonstração"| Flask
    Flask -->|"aplica lógica de ranking"| Dominio
    Dominio -->|"ranking processado"| Flask
    Flask -->|"renderiza"| Template
    Template -->|"resposta HTML"| Usuario

    