# Checkpoint Humano — Integração das Branches Experimentais

## Ponto de parada definido

Foi definido como checkpoint humano obrigatório o momento anterior à integração das branches experimentais da Etapa 2 na branch principal da atividade
`feature/harness-arquitetura`.

Nesse ponto, nenhuma integração deveria ser realizada automaticamente sem uma revisão humana dos diffs, do histórico de commits e dos testes produzidos.

## Contexto da revisão

Foram desenvolvidas duas tarefas independentes a partir do mesmo baseline
`13abe96`:

- `experimento/tdd-filtro-retorno`, contendo o ciclo RED → GREEN → REFACTOR,
  investigação do Superpowers e aprimoramento do guardrail;
- `experimento/sem-tdd-limite-ranking`, contendo a implementação deliberadamente
  realizada antes dos testes e a comparação posterior.

A revisão mostrou que ambas alteraram arquivos em comum, principalmente:

- `src/market/calculos.py`;
- `tests/test_calculos.py`;
- `docs/harness/sessao-log.md`.

Por esse motivo, uma integração automática das duas branches poderia causar
conflitos ou perda de alterações relevantes.

## Decisão humana

**Decisão: EDITAR.**

As duas implementações serão aproveitadas, mas a integração será realizada de forma controlada, com revisão manual dos conflitos.

A branch com TDD será integrada primeiro. Em seguida, a branch sem TDD será integrada e eventuais conflitos serão resolvidos preservando as duas funcionalidades e suas respectivas evidências.

Após a integração, a suíte completa de testes deverá ser executada antes da
aceitação final.

## Papel humano assumido

O papel humano neste checkpoint foi o de revisor e integrador.

A revisão não se limitou a aceitar automaticamente o resultado produzido pelos
agentes. Foi necessário verificar o histórico, identificar arquivos alterados em paralelo, avaliar o risco de perda de código e definir uma ordem segura de
integração.

O checkpoint foi mantido justamente para impedir que alterações produzidas em experimentos independentes fossem incorporadas ao projeto sem uma decisão
consciente sobre conflitos, rastreabilidade e preservação dos resultados.