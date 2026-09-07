# Investigação de Dívida Técnica com Análise Estática

## Ferramenta utilizada

Foi utilizada a ferramenta Ruff, versão 0.16.6, para realizar uma análise estática do código Python do projeto.

A análise foi executada com:

`python -m ruff check .`

Nenhuma correção automática foi aplicada, permitindo registrar o estado real do código antes de qualquer alteração.

## Resultado

O Ruff encontrou um único apontamento:

`RUF007 — Prefer itertools.pairwise() over zip() when iterating over successive pairs`

O aviso ocorre em `src/market/calculos.py`, no trecho responsável por percorrer
pares consecutivos de preços:

`zip(precos, precos[1:])`

O código atual funciona corretamente, mas utiliza um padrão mais indireto para representar a intenção de percorrer valores consecutivos.

## Sinal de dívida técnica identificado

O ponto foi classificado como uma dívida técnica de baixa gravidade relacionada à legibilidade e manutenibilidade.

A expressão `zip(precos, precos[1:])` exige que o leitor reconheça que duas sequências deslocadas estão sendo combinadas para formar pares consecutivos.

A função `itertools.pairwise()` representa essa intenção diretamente, tornando o código mais explícito e evitando também a criação do slice `precos[1:]`.

## Mitigação proposta

A mitigação proposta é substituir:

`zip(precos, precos[1:])`

por:

`pairwise(precos)`

com a importação:

`from itertools import pairwise`

A alteração deverá ser acompanhada pela execução da suíte de testes existente
para confirmar que o cálculo dos retornos permanece inalterado.

## Aprendizado

A análise mostrou que ferramentas de análise estática não servem apenas para localizar erros funcionais. Elas também conseguem apontar construções válidas,
mas menos claras ou menos idiomáticas.

Neste projeto, o resultado foi pequeno — apenas um apontamento —, mas permitiu identificar uma melhoria concreta de manutenção sem depender apenas de revisão
manual.

**Evidência:** `docs/harness/ruff-inicial.log`