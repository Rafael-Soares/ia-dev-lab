# ia-dev-lab

Projeto didático desenvolvido para praticar desenvolvimento de software assistido por Inteligência Artificial, Git/GitHub, testes e documentação.

## Sobre o projeto

Aplicação web simples para análise de ações brasileiras.

O sistema consultará uma API pública de dados financeiros, obterá dados históricos dos últimos seis meses e apresentará um ranking das ações com melhor desempenho no período.

O desempenho será calculado pela média aritmética dos seis retornos mensais consecutivos, utilizando sete preços de fechamento mensal.

Os resultados possuem finalidade exclusivamente educacional e não constituem recomendação de investimento.

## Tecnologias

* Python
* Flask
* Jinja2
* HTML e CSS
* pytest
* Git e GitHub
* Visual Studio Code
* GitHub Copilot

A API financeira será definida durante o desenvolvimento.

## Estrutura

```text
ia-dev-lab/
├── .github/
│   └── instructions/
├── docs/
│   └── adr/
├── src/
│   └── market/
├── static/
│   └── css/
├── templates/
├── tests/
├── AGENTS.md
├── hello.py
└── README.md
```

## Instalação

```bash
git clone <URL-DO-REPOSITORIO>
cd ia-dev-lab
```

As dependências serão adicionadas conforme a evolução do projeto.

## Comandos

Validar o ambiente:

```bash
python hello.py
```

Executar os testes:

```bash
python -m pytest
```

Executar a aplicação web, quando implementada:

```bash
python app.py
```

## Status

Projeto em desenvolvimento.
