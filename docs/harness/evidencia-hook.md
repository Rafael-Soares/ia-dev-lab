# Evidência do Guardrail

## Risco escolhido

Foi definido como risco do projeto a possibilidade de uma alteração no código da aplicação ser commitada sem qualquer atualização dos testes relacionados.

Como o projeto possui regras de domínio para cálculo e ranking, além de uma interface Flask, uma alteração aparentemente pequena pode modificar o comportamento existente sem que isso seja percebido imediatamente.

## Controle implementado

Foi criado um hook Git do tipo `pre-commit`, armazenado em `.githooks/pre-commit`.

O hook verifica os arquivos preparados para commit. Se houver alteração em `src/`, `app.py`, `templates/` ou `static/` e não existir nenhuma alteração
em `tests/`, o commit é interrompido.

O objetivo não é garantir automaticamente a qualidade do teste, mas impedir que mudanças no código da aplicação sejam commitadas sem que os testes sejam
ao menos considerados e atualizados.

## Teste do bloqueio

Para validar o funcionamento do guardrail, foi realizada propositalmente uma
alteração temporária no arquivo `app.py`, sem qualquer modificação nos testes.

O arquivo foi adicionado à área de stage e foi executada uma tentativa de
commit com a mensagem `Teste proposital do guardrail`.

O hook identificou que havia uma alteração em código da aplicação sem
alteração correspondente em `tests/` e interrompeu o commit, apresentando a
mensagem:

> COMMIT BLOQUEADO PELO GUARDRAIL

O `git log` foi verificado logo após a tentativa e confirmou que o commit não
foi criado. Em seguida, a modificação temporária em `app.py` foi descartada,
mantendo apenas o log da execução como evidência.

O teste confirmou que o controle implementado não funciona apenas como uma
orientação ao agente: ele atua diretamente no fluxo do Git e impede a ação
quando a condição de risco é identificada.

## Resultado

**Decisão:** guardrail aprovado.

O controle cumpriu o objetivo proposto ao impedir uma alteração de código da
aplicação de ser commitada sem que os testes fossem considerados. O arquivo
`docs/harness/hook-bloqueio.log` preserva a saída real produzida durante o
teste.