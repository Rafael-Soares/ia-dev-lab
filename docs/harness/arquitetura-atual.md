# Revisão da Arquitetura Atual

## Resumo da arquitetura

O projeto possui uma arquitetura simples, organizada em quatro responsabilidades
principais.

O arquivo `app.py` funciona como ponto de entrada da aplicação Flask e coordena
a rota `/ranking`. Os dados utilizados na demonstração ficam separados em
`src/market/dados_demo.py`, enquanto as regras de negócio estão concentradas em
`src/market/calculos.py`. A apresentação é realizada pelo template
`templates/ranking.html`.

O fluxo principal da aplicação pode ser resumido como:

```text
[Requisição GET /ranking]
        ↓
[Flask - app.py]
        ↓
[Dados - dados_demo.py]
        ↓
[Domínio - calculos.py]
        ↓
[Resultados do ranking]
        ↓
[Jinja2 - ranking.html]
        ↓
[Página HTML]