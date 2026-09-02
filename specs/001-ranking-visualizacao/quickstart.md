# Quickstart: Validação do Ranking e da Visualização

## Objetivo

Validar, sem implementar código novo nesta etapa, que a lógica de ranking e a página de visualização atendem aos critérios de aceitação da especificação.

## Pré-requisitos

- Ambiente Python configurado.
- Dependências do projeto instaladas.
- Projeto com a lógica de cálculo e a interface web já disponíveis no escopo de desenvolvimento.

## Cenários de validação

1. Ranking com dados completos
   - Preparar um conjunto de ativos com sete preços válidos cada.
   - Verificar que todos os ativos válidos aparecem no ranking.
   - Confirmar que a ordem é decrescente pelo desempenho médio mensal.

2. Dados inválidos e incompletos
   - Incluir ativos com menos de sete preços, valores não numéricos, zeros ou negativos.
   - Verificar que esses ativos são ignorados.
   - Confirmar que os ativos válidos continuam no resultado.

3. Resultado vazio
   - Usar apenas ativos inválidos ou incompletos.
   - Confirmar que a saída final é vazia e que não há resultados artificiais.

4. Interface web com resultado
   - Carregar a página de ranking com dados válidos.
   - Verificar que aparece posição, ticker e retorno médio mensal em percentual.
   - Confirmar que a ordem visual coincide com a ordem do ranking.

5. Interface web sem resultado
   - Carregar a página com conjunto vazio ou inválido.
   - Confirmar que há mensagem clara de ausência de resultados.
   - Confirmar que não há erro não tratado.

## Critério de sucesso

A funcionalidade é considerada pronta para a próxima etapa quando todos os cenários acima forem comprovados e a regra de negócio estiver separada da camada de apresentação.
