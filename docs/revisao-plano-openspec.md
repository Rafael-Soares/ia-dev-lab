# Revisão humana do plano OpenSpec

O plano inicial gerado pelo agente foi revisado antes da implementação. Foram removidas tarefas destinadas apenas a validar as specs, pois essa revisão já havia sido realizada manualmente, e foram alteradas tarefas que poderiam levar à duplicação da lógica de cálculo já existente em `calcular_retorno_medio_mensal`.

Também foi corrigida a separação de responsabilidades entre geração e apresentação: a lógica de ranking passou a produzir um resultado vazio quando nenhum ativo é válido, enquanto a mensagem ao usuário permanece responsabilidade da camada de visualização.

Durante a revisão foi identificada ainda uma lacuna sobre a origem dos dados, já que a integração com uma API externa está fora do escopo desta change. Por isso, foi adotado um provedor local de dados de demonstração, separado da lógica de negócio e substituível futuramente por uma fonte externa.

Por fim, as tarefas de teste foram associadas às funcionalidades implementadas e foi adicionada uma validação final contra os cenários GIVEN / WHEN / THEN das duas capabilities.