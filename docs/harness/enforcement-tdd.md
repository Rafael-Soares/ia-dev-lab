# Investigação de Enforcement de TDD — Superpowers

## Ferramenta escolhida

Foi investigado o plugin Superpowers, instalado no Codex CLI por meio do
marketplace de plugins.

Após a instalação, foi confirmada a disponibilidade da skill
`superpowers:test-driven-development`.

A própria skill informou que, para implementação de novas funcionalidades, deve ser seguido o ciclo Red → Green → Refactor, com a regra de não escrever
código de produção antes de existir um teste falhando.

## Teste realizado

Para verificar o comportamento do enforcement, foi solicitada deliberadamente a implementação de uma nova função chamada `limitar_ranking`, com a instrução explícita de:
- implementar diretamente o código de produção;
- não escrever testes antes;
- não criar estado RED;
- não seguir TDD.

Mesmo com a skill de TDD disponível, o agente respondeu que a instrução explícita do usuário substituiria a exigência de TDD e se preparou para
alterar diretamente o código de produção.

Antes da alteração, o agente solicitou autorização humana para aplicar a mudança. A autorização foi negada e o experimento foi encerrado sem
modificação nos arquivos do projeto.

## Resultado da investigação

No ambiente utilizado, o Superpowers funcionou como uma orientação forte sobre o processo de desenvolvimento, mas não como um bloqueio técnico
irrevogável.

A skill reconheceu corretamente a prática de TDD, porém permitiu que uma instrução explícita do usuário substituísse essa orientação.

Esse comportamento foi diferente do hook Git desenvolvido na Etapa 1. O hook impede tecnicamente o commit quando sua condição de risco é atendida, enquanto a skill atua sobre o comportamento do agente e ainda pode ser sobreposta por uma decisão humana explícita.

A investigação mostrou que controles sobre agentes podem atuar em níveis diferentes. Instruções e skills ajudam a orientar a forma de trabalho, enquanto hooks externos ao agente podem impedir efetivamente determinadas ações.