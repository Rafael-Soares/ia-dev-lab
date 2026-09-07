# Research: Ranking e Visualização de Ações Brasileiras

## Decision

O sistema deve calcular o desempenho de cada ativo a partir de uma série de sete preços mensais de fechamento em ordem cronológica. O retorno mensal é medido como a variação percentual entre um mês e o seguinte, e o desempenho do ativo é a média aritmética dos seis retornos mensais consecutivos.

## Rationale

A especificação define claramente que o ranking considera seis variações mensais e que o cálculo utiliza sete preços. Essa regra evita ambiguidade e mantém consistência entre a lógica de domínio e a interface. A média aritmética dos seis retornos mensais é o indicador definido pelo
escopo para representar o desempenho médio mensal do ativo no período.

## Alternatives considered

- Usar a variação do primeiro para o último preço do período: rejeitado porque a especificação exige seis variações mensais consecutivas e um cálculo baseado em retornos mensais.
- Incluir ativos incompletos no ranking: rejeitado porque o escopo exige ignorar ativos inválidos e manter somente os válidos.
- Ordenar a interface diretamente sem preservar a sequência calculada: rejeitado porque a constituição exige separação de responsabilidades e manutenção da ordem produzida pela lógica de negócio.
- Criar um banco de dados ou serviço externo: rejeitado porque o escopo proíbe infraestrutura adicional e o projeto é educacional e mínimo.

## Unknowns resolved

- "O que representa um ativo válido?": um ativo que possui exatamente sete preços mensais válidos em ordem cronológica, todos numéricos e maiores que zero.
- "Como tratar dados inválidos?": ignorá-los sem bloquear o processamento dos ativos válidos.
- "Como a interface deve se comportar sem resultados?": apresentar uma mensagem clara de ausência de resultados e manter a página estável.
