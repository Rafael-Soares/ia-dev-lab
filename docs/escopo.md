# Escopo da Atividade SDD

## Projeto

Será utilizado o projeto `ia-dev-lab`, iniciado na atividade anterior. O projeto consiste em uma aplicação web didática para análise de ações brasileiras.

## Funcionalidade 1 — Ranking de ações brasileiras

Desenvolver uma funcionalidade capaz de gerar um ranking de ações brasileiras com base no desempenho apresentado nos últimos seis meses.

### Cenários iniciais

- geração do ranking quando existem dados suficientes para os ativos analisados;
- tratamento de situações em que um ou mais ativos não possuem dados suficientes para análise.

## Funcionalidade 2 — Visualização do ranking

Desenvolver uma página web que permita ao usuário visualizar o ranking gerado pela aplicação.

### Cenários iniciais

- exibição do ranking quando existem resultados disponíveis;
- apresentação adequada da interface quando nenhum resultado puder ser exibido.

## Justificativa para uso de SDD

As funcionalidades escolhidas são adequadas ao Spec-Driven Development porque envolvem regras de negócio, diferentes cenários de uso e situações de borda que precisam ser definidas antes da implementação. O desenvolvimento também deverá envolver diferentes partes da aplicação, como processamento de dados, testes, backend e interface web. Uma especificação prévia permitirá reduzir decisões implícitas do agente de IA e estabelecer critérios objetivos para avaliar se a implementação atende ao comportamento desejado. Além disso, o mesmo escopo permitirá comparar como diferentes ferramentas de SDD estruturam e executam uma mesma necessidade.

## User Story Inicial

Como usuário interessado em acompanhar o desempenho recente de ações brasileiras,
quero visualizar um ranking das ações analisadas com base em seu desempenho nos últimos seis meses,
para que eu possa comparar de forma simples quais ativos apresentaram os melhores resultados no período.

O sistema deve ser capaz de gerar o ranking mesmo quando nem todos os ativos possuírem dados suficientes para análise e deve informar de forma clara quando não houver resultados disponíveis.