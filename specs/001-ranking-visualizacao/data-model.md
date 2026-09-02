# Data Model: Ranking e Visualização de Ações Brasileiras

## Entities

### Ativo

- `ticker`: identificador textual do ativo
- `precos_mensais`: sequência de sete preços de fechamento
- `valido`: indica se a série atende aos critérios de validade

### Série de preços mensais

- `valores`: lista de sete preços de fechamento fornecidos em ordem cronológica
- `quantidade`: deve ser exatamente sete para que o ativo seja elegível
- `regras`: todos os valores devem ser numéricos e maiores que zero

### Resultado do ranking

- `ticker`: identificador do ativo
- `retorno_medio_mensal_percentual`: média aritmética dos seis retornos mensais em percentual

A posição apresentada ao usuário é determinada pela ordem do item na lista
de resultados, não sendo obrigatoriamente armazenada como atributo do domínio.

## Relationships

- Um ativo possui uma série de preços mensais.
- Quando a série é válida, o ativo gera um resultado do ranking.
- O resultado do ranking participa de uma lista ordenada do maior para o menor desempenho.
- A interface apresenta os resultados em ordem já definida pela lógica de negócios, sem reordenação local.

## Validation rules

- A série deve conter exatamente sete elementos.
- Os preços devem ser fornecidos em ordem cronológica.
- Todos os valores devem ser numéricos.
- Todos os valores devem ser maiores que zero.
- Ativos inválidos ou incompletos não devem impedir o processamento dos demais.
- O ranking deve conter somente resultados de ativos válidos.
