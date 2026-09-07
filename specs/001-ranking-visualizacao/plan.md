# Implementation Plan: Ranking e Visualização de Ações Brasileiras

**Branch**: `001-ranking-visualizacao` | **Date**: 2026-09-01 | **Spec**: [specs/001-ranking-visualizacao/spec.md](../spec.md)

**Input**: Feature specification from `/specs/001-ranking-visualizacao/spec.md`

## Summary

A funcionalidade será implementada como uma solução mínima em Python para gerar um ranking de ações brasileiras a partir de seis variações mensais consecutivas e exibir esse ranking em interface web. A regra de negócio central será tratada em módulo de cálculo separado, com validação de ativos, filtragem de registros inválidos e ordenação do resultado final. A camada de apresentação receberá apenas os resultados já processados e não recalculará nem reordenará a lista.

## Technical Context

**Language/Version**: Python 3.x (compatível com o projeto atual e com pytest)

**Primary Dependencies**: Flask, Jinja2, pytest

**Storage**: Nenhum armazenamento persistente; dados em memória para a execução da funcionalidade

**Testing**: pytest, com foco em testes unitários da lógica de cálculo e de comportamento da interface web

**Target Platform**: Aplicação web local, executada em ambiente Python

**Project Type**: Web application

**Performance Goals**: Processar pequenas coleções de ativos em memória sem overhead adicional; manter resposta imediata para listas de dezenas de ativos

**Constraints**: Sem API externa, sem banco de dados, sem autenticação, sem recomendação de investimento; escopo educacional e mínimo

**Scale/Scope**: Apenas o cálculo do ranking e a renderização da página de resultados, com foco em regras de negócio e apresentação

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- PASS: Reutilização antes de duplicação — a lógica de cálculo deve ser consolidada em um módulo único e reaproveitada pela interface e pelos testes.
- PASS: Separação de responsabilidades — dados, regra de negócio e apresentação permanecem em camadas distintas.
- PASS: Desenvolvimento orientado por testes — os critérios de aceitação serão convertidos em testes automatizados antes ou junto à implementação.
- PASS: Escopo mínimo — apenas a geração do ranking e a visualização web entram no escopo.
- PASS: Revisão humana obrigatória — qualquer alteração relevante deve ser revisada antes da aceitação.
- PASS: Clareza e simplicidade — a solução será pequena, compreensível e adaptada ao tipo de projeto.

## Project Structure

### Documentation (this feature)

```text
specs/001-ranking-visualizacao/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output
├── spec.md              # Feature specification
├── checklists/
│   └── requirements.md
└── tasks.md             # Phase 2 output, not created in this step
```

### Source Code (repository root)

```text
src/
├── market/
│   └── calculos.py

tests/
├── test_calculos.py
└── test_app.py
```

**Structure Decision**: A solução será mantida em um único módulo de cálculo em `src/market/calculos.py`, com a camada web usando o Flask já previsto no projeto e mantendo a lógica de negócio separada da apresentação. Os testes ficarão em `tests/` e cobrirão cálculo, filtragem de dados inválidos e visão do ranking quando houver ou não resultados.
### Fonte de dados para demonstração

Como integrações externas estão fora do escopo, a funcionalidade utilizará
um pequeno provedor local de dados controlados para permitir a execução da
aplicação e a demonstração dos estados com resultados, resultados parciais
e ausência de resultados.

Esse provedor deve permanecer separado da lógica de cálculo, permitindo
substituição futura por outra fonte de dados sem alterar as regras de negócio.
### Riscos e decisões de revisão humana

- Garantir que a implementação reutilize a função de cálculo existente em vez
  de duplicar a fórmula do retorno mensal.

- Garantir que o provedor de dados de demonstração permaneça separado da lógica
  de negócio e possa ser substituído futuramente.

- Verificar, antes da aceitação, que a camada web não recalcula, filtra ou
  reordena os resultados produzidos pelo domínio.
## Complexity Tracking

> No violations identified against the project constitution. The design stays within the minimum viable scope and does not introduce new persistence, auth, or external service dependencies.

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| None | N/A | N/A |


