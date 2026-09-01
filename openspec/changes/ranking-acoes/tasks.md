## 1. Geração do ranking

- [ ] 1.1 Implementar a lógica de geração do ranking em `src/market/`, reutilizando `calcular_retorno_medio_mensal` como única fonte para o cálculo do desempenho de cada ativo válido.

- [ ] 1.2 Tratar individualmente ativos incompletos ou inválidos, excluindo aqueles que não atendem aos requisitos da spec sem interromper o processamento dos ativos válidos.

- [ ] 1.3 Ordenar os ativos válidos do maior para o menor desempenho e produzir um resultado contendo as informações necessárias para a visualização, incluindo ticker e retorno médio mensal.

- [ ] 1.4 Retornar um ranking vazio quando nenhum ativo analisado for válido, sem incluir resultados inválidos ou artificiais.

- [ ] 1.5 Criar testes unitários para geração do ranking, cobrindo múltiplos ativos válidos, ordenação, combinação de ativos válidos e inválidos e ausência total de ativos válidos.

## 2. Dados de demonstração

- [ ] 2.1 Criar um provedor local simples de dados de demonstração com preços mensais controlados para permitir a execução da funcionalidade sem integração com uma API externa.

- [ ] 2.2 Manter os dados de demonstração separados da lógica de cálculo e do ranking, permitindo sua substituição futura por uma fonte externa.

## 3. Visualização do ranking

- [ ] 3.1 Criar ou atualizar a aplicação Flask para disponibilizar uma rota de visualização do ranking utilizando a camada de processamento definida na capability `ranking-acoes`.

- [ ] 3.2 Criar o template Jinja2 da página de ranking exibindo, para cada resultado, posição, ticker e retorno médio mensal como percentual.

- [ ] 3.3 Preservar na interface a mesma ordem recebida da lógica de ranking.

- [ ] 3.4 Implementar o estado vazio da página, exibindo uma mensagem clara quando o ranking não possuir resultados e evitando erros não tratados.

- [ ] 3.5 Garantir que um ranking contendo apenas o subconjunto válido dos ativos continue sendo exibido normalmente.

## 4. Testes e validação

- [ ] 4.1 Criar testes da camada web para verificar a apresentação dos campos obrigatórios e a ordem dos resultados.

- [ ] 4.2 Criar teste para o estado vazio, verificando a mensagem apresentada e a ausência de erro não tratado.

- [ ] 4.3 Executar `python -m pytest` e confirmar que os testes existentes e os novos testes são aprovados.

- [ ] 4.4 Conferir a implementação final contra os cenários GIVEN / WHEN / THEN das capabilities `ranking-acoes` e `visualizacao-ranking`.