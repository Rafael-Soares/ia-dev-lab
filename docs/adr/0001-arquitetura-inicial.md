# ADR 0001 — Arquitetura inicial da aplicação

## Status

Aceito.

## Contexto

O projeto consiste em uma aplicação web simples que consultará dados históricos de ações brasileiras em uma API pública, processará essas informações e apresentará um ranking das ações com melhor desempenho nos últimos seis meses.

Por possuir finalidade didática, a aplicação deve utilizar uma arquitetura simples, de fácil desenvolvimento, manutenção e compreensão.

## Decisão

A aplicação utilizará:

* **Python** como linguagem principal;
* **Flask** como framework web;
* **Jinja2** para geração das páginas HTML;
* **HTML e CSS** para construção da interface;
* **pytest** para testes automatizados;
* uma **API pública de dados financeiros**, a ser definida durante a implementação.

A aplicação seguirá uma separação simples entre:

1. obtenção dos dados financeiros;
2. processamento e cálculo dos indicadores;
3. apresentação dos resultados na interface web.

## Justificativa

Python foi escolhido pela simplicidade e pelo bom suporte ao consumo e processamento de dados.

Flask foi escolhido por ser um framework web leve e adequado ao pequeno escopo do projeto.

Jinja2 permitirá gerar páginas HTML dinamicamente utilizando os dados processados pelo backend, sem a necessidade de adicionar um framework frontend mais complexo.

## Consequências

* A aplicação poderá ser desenvolvida inteiramente com Python no backend.
* A interface permanecerá simples, utilizando renderização no servidor.
* Não será necessário utilizar frameworks frontend como React ou Vue.
* A lógica de acesso à API e os cálculos deverão permanecer separados da camada de apresentação.
* Novas bibliotecas deverão ser adicionadas somente quando necessárias.
* A escolha da API financeira será registrada posteriormente.
