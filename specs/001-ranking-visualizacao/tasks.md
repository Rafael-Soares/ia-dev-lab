# Tasks: Ranking e Visualização de Ações Brasileiras

## Phase 1: Testes da lógica de domínio

- [x] T001 [P] [US1] Adicionar em `tests/test_calculos.py` teste para múltiplos ativos válidos e resultado ordenado do maior para o menor retorno médio mensal.

- [x] T002 [P] [US1] Adicionar em `tests/test_calculos.py` teste com ativos válidos, inválidos e incompletos, comprovando que os inválidos são ignorados sem bloquear os válidos.

- [x] T003 [P] [US1] Adicionar em `tests/test_calculos.py` teste em que todos os ativos são inválidos ou incompletos, esperando ranking vazio.

**Checkpoint**: os comportamentos esperados do domínio estão definidos por testes antes da implementação.

---

## Phase 2: Implementação do domínio e dados de demonstração

- [x] T004 [US1] Implementar em `src/market/calculos.py` a geração do ranking, reutilizando `calcular_retorno_medio_mensal` como única fonte da regra de cálculo e tratando individualmente ativos inválidos.

- [x] T005 [US1] Ordenar em `src/market/calculos.py` os resultados válidos do maior para o menor retorno médio mensal, retornando ticker e retorno sem armazenar posição como estado do domínio.

- [ ] T006 [P] Criar `src/market/dados_demo.py` com pequeno conjunto controlado de ativos fictícios para demonstração local, mantendo os dados separados da lógica de negócio.

**Checkpoint**: o domínio gera um ranking ordenado, ignora entradas inválidas e pode ser executado sem fonte externa.

---

## Phase 3: Testes da interface web

- [ ] T007 [P] [US2] Criar `tests/test_app.py` com teste da rota de ranking contendo resultados e verificar posição, ticker e retorno médio mensal em percentual.

- [ ] T008 [P] [US2] Adicionar em `tests/test_app.py` teste comprovando que a interface preserva a ordem da lista produzida pelo domínio.

- [ ] T009 [P] [US2] Adicionar em `tests/test_app.py` teste para ranking vazio, verificando mensagem clara e resposta sem erro não tratado.

- [ ] T010 [P] [US2] Adicionar em `tests/test_app.py` teste para apresentação normal de um subconjunto válido recebido pela interface.

**Checkpoint**: os critérios de aceitação da camada web estão definidos por testes antes da implementação.

---

## Phase 4: Implementação da interface web

- [ ] T011 [US2] Criar ou atualizar `app.py` com rota `/ranking`, obtendo os dados de demonstração e enviando-os à lógica de domínio antes da renderização.

- [ ] T012 [US2] Criar `templates/ranking.html` para exibir posição derivada da ordem da lista, ticker e retorno médio mensal em percentual, sem recalcular ou reordenar resultados.

- [ ] T013 [US2] Implementar em `templates/ranking.html` o estado vazio com mensagem clara quando não houver resultados.

**Checkpoint**: a interface consome o resultado do domínio e não contém regras de negócio.

---

## Phase 5: Verificação e aceitação

- [ ] T014 Executar `python -m pytest` e confirmar aprovação conjunta dos testes existentes e novos.

- [ ] T015 Conferir todos os cenários de aceitação da especificação e realizar a verificação final de conformidade com a constituição, incluindo revisão humana do diff antes da aceitação.