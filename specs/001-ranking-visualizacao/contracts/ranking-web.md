# Contract: Visualização do ranking

## Purpose

Descrever o contrato interno da página web que apresenta o ranking produzido pela lógica de negócio.

## Inputs

- Lista de resultados já calculados e ordenados pela lógica de domínio.
- Cada item da lista contém: `ticker` e `retorno_medio_mensal_percentual`.
- A posição exibida é derivada da ordem do item na lista recebida.

## Output

- Página web com a tabela de ranking exibida em ordem preservada.
- Quando a lista estiver vazia, página com mensagem clara de ausência de resultados.

## Rules

- A interface não recalcula o desempenho.
- A interface não reordena os resultados.
- A interface não cria resultados artificiais.
- A interface exibe somente os resultados recebidos da lógica de domínio.

## Error handling

- Se a lógica de domínio retornar apenas um subconjunto de resultados, a interface deve exibi-lo normalmente, preservando sua ordem.
- Se houver apenas subconjunto válido, a interface deve exibir somente esse subconjunto.
