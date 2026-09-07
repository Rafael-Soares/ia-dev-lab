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

A preencher após a execução proposital da ação bloqueada.