# Feature Specification: Ranking e Visualização de Ações Brasileiras

**Feature Branch**: `[001-ranking-visualizacao]`

**Created**: 2026-09-01

**Status**: Draft

**Input**: User description: "Crie a especificação funcional para as duas funcionalidades descritas em docs/escopo.md."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Gerar ranking de desempenho dos últimos seis meses (Priority: P1)

Como usuário interessado em acompanhar o desempenho recente de ações brasileiras, quero visualizar um ranking baseado nos últimos seis meses de dados, para comparar rapidamente quais ativos tiveram melhor desempenho no período.

**Why this priority**: Este é o núcleo do valor do produto. Sem um ranking confiável e ordenado, a funcionalidade principal não atende ao objetivo do projeto.

**Independent Test**: Pode ser validado com um conjunto de ativos com dados completos e incompletos, confirmando que apenas os ativos válidos participam do cálculo e que o resultado final aparece em ordem decrescente de desempenho.

**Acceptance Scenarios**:

1. **Given** um conjunto de ativos com sete preços mensais de fechamento válidos em ordem cronológica, **When** o sistema calcula o ranking, **Then** ele deve produzir um retorno médio mensal para cada ativo e ordená-los do maior para o menor desempenho.
2. **Given** um ativo com menos de sete preços mensais, preços nulos, valores não numéricos ou valores menores ou iguais a zero, **When** o sistema processa os dados, **Then** esse ativo deve ser considerado inválido e ignorado sem impedir o processamento dos ativos válidos.
3. **Given** somente alguns ativos do conjunto possuem dados válidos, **When** o sistema gera o ranking, **Then** deve incluir apenas esse subconjunto válido e exibi-lo normalmente, sem erro ou bloqueio.

---

### User Story 2 - Visualizar o ranking em interface web (Priority: P1)

Como usuário, quero ver o ranking em uma tela clara e ordenada, para compreender rapidamente a posição de cada ativo e o percentual de desempenho alcançado.

**Why this priority**: A funcionalidade de visualização é a forma pela qual o usuário consome o resultado. Sem uma apresentação clara, o cálculo não é acessível de forma útil.

**Independent Test**: Pode ser validado por meio da apresentação da página com resultados e pela mesma tela em estado vazio, verificando que a ordem seja preservada e que a mensagem de ausência de resultado seja clara.

**Acceptance Scenarios**:

1. **Given** há resultados válidos disponíveis, **When** a página do ranking é exibida, **Then** ela deve mostrar a posição, o ticker e o retorno médio mensal como percentual, preservando a ordem estabelecida pelo ranking.
2. **Given** não há ativos válidos para análise, **When** a página do ranking é carregada, **Then** ela deve apresentar uma mensagem clara informando que nenhum resultado está disponível, sem erro não tratado.
3. **Given** apenas parte dos ativos é válida, **When** a página do ranking é carregada, **Then** ela deve exibir somente os ativos válidos em sua ordem correta.

---

### User Story 3 - Tratar dados incompletos ou inválidos sem interromper o processamento (Priority: P2)

Como usuário, quero que o sistema trate dados incompletos ou inválidos de forma resiliente, para que os ativos válidos continuem sendo avaliados mesmo quando alguns registros não puderem ser usados.

**Why this priority**: Esse cenário reforça a confiabilidade do sistema e evita que um conjunto parcialmente ruim gere falha total na análise.

**Independent Test**: Pode ser validado com uma entrada contendo ativos válidos e inválidos, confirmando que os inválidos não geram resultados artificiais e que os válidos seguem sendo processados normalmente.

**Acceptance Scenarios**:

1. **Given** um conjunto de ativos contendo registros inválidos, incompletos e válidos, **When** o cálculo do ranking é executado, **Then** os registros inválidos devem ser ignorados e os dados válidos devem continuar sendo processados.
2. **Given** todos os ativos disponíveis forem inválidos ou incompletos, **When** o sistema gera o resultado, **Then** deve retornar uma lista vazia sem criar posições ou ativos artificiais.

### Edge Cases

- O que acontece quando um ativo possui menos de sete preços mensais válidos?
- Como o sistema lida com preços iguais a zero, negativos, não numéricos?
- O que acontece quando o conjunto de dados está totalmente vazio ou quando todos os ativos são inválidos?
- Como a interface se comporta quando não há resultados disponíveis?
- Como a ordem dos ativos deve ser preservada quando há empate ou quando a ordenação final depende do cálculo do desempenho?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: O sistema MUST calcular seis retornos mensais consecutivos a partir dos sete preços mensais de fechamento de cada ativo válido, utilizando para cada período a fórmula `((preço_atual / preço_anterior) - 1) * 100`.

- **FR-002**: O sistema MUST considerar um ativo válido somente quando ele possuir exatamente sete preços mensais de fechamento, fornecidos em ordem cronológica.

- **FR-003**: O sistema MUST rejeitar ativos cujo conjunto contenha mais ou menos de sete preços mensais.

- **FR-004**: O sistema MUST validar que todos os preços de fechamento sejam numéricos e maiores que zero antes de considerar o ativo elegível para o ranking.
- **FR-005**: O sistema MUST ignorar ativos inválidos ou incompletos sem bloquear o processamento dos ativos válidos restantes.
- **FR-006**: O sistema MUST calcular o desempenho do ativo como a média aritmética dos seis retornos mensais consecutivos e representá-lo em percentual.
- **FR-007**: O sistema MUST ordenar o ranking do maior para o menor desempenho médio mensal.
- **FR-008**: O sistema MUST preservar a ordem produzida pelo ranking na apresentação visual.
- **FR-009**: O sistema MUST retornar uma lista vazia quando nenhum ativo for válido, sem criar resultados artificiais ou posições simuladas.
- **FR-010**: A interface MUST apresentar posição, ticker e retorno médio mensal como percentual para cada linha do ranking.
- **FR-011**: A interface MUST apresentar uma mensagem clara quando não houver resultados disponíveis, sem erro não tratado.
- **FR-012**: A interface MUST exibir apenas o subconjunto de ativos válidos quando parte dos ativos não puder ser processada.
- **FR-013**: O sistema MUST manter o comportamento consistente para múltiplos ativos válidos e inválidos no mesmo conjunto de dados.

### Key Entities *(include if feature involves data)*

- **Ativo**: representa uma ação analisada, identificada por seu ticker e por uma série de preços mensais de fechamento.
- **Série de preços mensais**: conjunto de valores de fechamento de um ativo em ordem cronológica, usado para calcular o retorno médio mensal.
- **Resultado do ranking**: resultado associado a um ativo válido, contendo seu ticker e retorno médio mensal. A posição apresentada ao usuário decorre da ordem desse resultado no ranking.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: O sistema classifica corretamente todos os ativos válidos em ordem decrescente de desempenho sempre que houver pelo menos um conjunto completo de dados elegíveis.
- **SC-002**: O sistema ignora 100% dos ativos inválidos ou incompletos sem impedir a análise dos ativos válidos que compartilham o mesmo conjunto de dados.
- **SC-003**: Quando nenhum ativo for válido, a interface mostra uma mensagem clara e o resultado final permanece vazio, sem registros fictícios.
- **SC-004**: A interface apresenta o ranking com posição, ticker e retorno médio mensal em percentual de forma consistente ao longo de cada execução.
- **SC-005**: Quando apenas parte dos ativos é válida, o resultado exibido corresponde exatamente ao subconjunto válido e mantém a ordem correta do ranking.
- **SC-006**: O usuário consegue identificar claramente, no mínimo, o melhor e o pior desempenho dentre os ativos exibidos no ranking.

## Assumptions

- O projeto trata o ranking como uma funcionalidade didática e educacional, sem finalidade de recomendação de investimento.
- Os dados de entrada podem conter registros incompletos ou inconsistentes e devem ser processados de forma resiliente.
- A lógica de negócio deve decidir a elegibilidade dos ativos antes da apresentação, evitando que a interface reinterprete ou recalcule os resultados.
- A experiência de usuário deve priorizar clareza, ordem e eventualmente mensagens informativas quando não houver dados válidos.
