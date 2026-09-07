# Comparação entre desenvolvimento com e sem TDD

## Tarefa com TDD

A funcionalidade escolhida foi o filtro do ranking por retorno mínimo.

Antes de qualquer alteração no código de produção, foram criados quatro testes para verificar filtragem pelo limite, igualdade ao limite, preservação da ordem
e ranking vazio.

A primeira execução apresentou 4 falhas porque
`filtrar_ranking_por_retorno_minimo` ainda não existia, caracterizando o
estado RED.

Somente depois disso foi implementado o código mínimo necessário. Os mesmos testes passaram sem precisar ser modificados e a suíte completa chegou a 17 testes aprovados, caracterizando o estado GREEN.

Na etapa REFACTOR, a implementação e os testes foram revisados. Não foi identificada uma refatoração que trouxesse ganho real sem aumentar
desnecessariamente a complexidade, portanto a decisão foi manter o código.

## Tarefa sem TDD

A segunda funcionalidade foi `limitar_ranking`.

Neste caso, o agente recebeu a instrução de implementar primeiro e não criar testes antes. A função foi adicionada ao código de produção e somente a suíte preexistente foi executada, apresentando 13 testes aprovados.

Durante a implementação, o agente considerou espontaneamente comportamentos como limite zero, limite negativo, ranking vazio e limite maior que a quantidade
de itens.

Somente depois da implementação foram criados sete testes específicos para a nova função. Todos passaram na primeira execução e a suíte completa apresentou
20 testes aprovados. Nenhum defeito adicional foi identificado e não foi
necessário alterar a implementação.

## Comparação

Nas duas tarefas, o resultado final foi funcional e os casos de borda avaliados
ficaram cobertos por testes. A principal diferença observada não esteve na quantidade final de testes ou na existência de defeitos, mas no momento em que os testes passaram a orientar o desenvolvimento.

Com TDD, os comportamentos esperados estavam formalizados antes da
implementação e foi possível observar objetivamente a transição RED → GREEN. Isso reduziu a dependência das decisões espontâneas do agente durante a escrita
do código.

Sem TDD, a implementação também foi correta neste experimento, mas os testes
só confirmaram o comportamento depois que as decisões já haviam sido tomadas no código. Nesse cenário, a cobertura inicial dependeu mais da capacidade do agente de antecipar casos de borda.

O experimento indicou que TDD não garante necessariamente uma implementação
mais curta ou mais correta em toda tarefa pequena, mas fornece um controle de processo mais verificável: o comportamento esperado existe como teste antes
do código que procura satisfazê-lo.