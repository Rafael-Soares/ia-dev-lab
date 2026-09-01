## Why

O projeto precisa permitir que o usuário compare rapidamente o desempenho recente de ações brasileiras em um único ranking. Hoje o escopo do laboratório menciona análise de ações e visualização de resultados, mas ainda não formaliza como esse ranking será gerado nem como o sistema deve responder quando há dados incompletos ou quando não há resultados disponíveis.

## What Changes

- Introduzir um ranking de ações brasileiras com base no desempenho observado nos últimos seis meses.
- Permitir que o usuário visualize o ranking gerado pela aplicação em interface web.
- Tratar cenários em que um ou mais ativos não possuem dados suficientes para análise.
- Exibir uma resposta clara quando nenhum resultado estiver disponível.
- Manter o escopo restrito à geração e à apresentação do ranking, sem recomendar investimento.

## Capabilities

### New Capabilities

- ranking-acoes: geração de um ranking de ações brasileiras com base no desempenho dos últimos seis meses, incluindo o tratamento de ativos com dados insuficientes.

- visualizacao-ranking: apresentação do ranking ao usuário, incluindo o comportamento da interface quando houver resultados disponíveis e quando nenhum resultado puder ser apresentado.

### Modified Capabilities
- Nenhuma.

## Impact

- Lógica de processamento de dados financeiros em `src/market/`.
- Rotas e renderização web da aplicação Flask.
- Templates e apresentação da página de ranking.
- Cenários de teste para cálculo e visualização, incluindo ativos incompletos e ausência de resultados.
