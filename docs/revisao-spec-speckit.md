# Revisão Humana da Especificação — SpecKit

A especificação inicial produzida pelo SpecKit foi revisada antes da etapa de planejamento.

Durante a revisão foram identificados três pontos principais:

1. A regra de cálculo do desempenho mencionava seis variações mensais e retorno médio, mas não definia explicitamente a fórmula do retorno mensal nem que o resultado utilizava a média aritmética. A regra foi detalhada para evitar interpretações diferentes na implementação.

2. A especificação exigia rejeição de preços fora de ordem cronológica, embora a entrada definida contivesse apenas uma sequência de preços sem informação temporal que permitisse verificar essa condição. A ordem cronológica passou a ser tratada como pré-condição dos dados de entrada.

3. Um edge case mencionava empate entre ativos sem definir o comportamento esperado. Como essa regra não fazia parte do escopo original, o cenário foi removido em vez de introduzir uma decisão arbitrária.

Também foi esclarecido que a posição exibida no ranking decorre da ordem dos resultados, não sendo necessariamente um atributo armazenado pela lógica de domínio.

A revisão humana buscou reduzir ambiguidades antes da geração do plano e impedir que decisões não especificadas fossem transferidas automaticamente para o agente de implementação.