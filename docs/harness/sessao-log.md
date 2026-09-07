# Log da Sessão do Agente — Harness e Arquitetura

Este arquivo registra as execuções realizadas com o agente durante a atividade.

## Etapa 1 — Comparação de autonomia

### Execução 1 — Autonomia controlada

**Branch:** `experimento/autonomia-controlada`

**Modo utilizado:** GitHub Copilot Agent com aprovação manual das ações.

**Tarefa:** adicionar classificação de tendência ao ranking de ações.

**Início:** 11:46  
**Fim:** 11:49  
**Tempo total:** 3 minutos

**Aprovações manuais:** 5

**Sensação de controle:** 3/5  
**Risco percebido:** 3/5

**Resultado:** implementação concluída com alteração da lógica de domínio,
template e testes.

**Validação:** `15 passed`.

**Observação inicial:** o agente localizou corretamente a responsabilidade da
regra no domínio e manteve o template apenas como camada de apresentação.
Mesmo utilizando um modo com aprovação manual, foram necessárias cinco
interações de autorização durante uma tarefa pequena.

**Log da execução:**
Vou localizar o cálculo do ranking, a rota/template e os testes próximos para confirmar onde a regra de tendência deve viver; em seguida faço a menor alteração possível e rodo a suíte completa.

Searched for files matching `**/src/**/*.py`, 2 matches

Searched for files matching `**/tests/**/*.py`, 2 matches

A regra está concentrada em `calculos.py`: `gerar_ranking` já calcula e ordena pelo retorno, então a classificação pode ser adicionada ali sem tocar na ordenação. O teste discriminante será cobrir os três sinais, além de verificar que o template apenas renderiza o campo recebido pela lógica de domínio. Vou ler a instrução específica dos testes antes de editar.

Searched for regex `tendência|tendencia|retorno_medio_mensal_percentual|gerar_ranking`, 30 results

A implementação seguirá um limite claro: criar uma função de domínio `classificar_tendencia`, incluir seu resultado em cada item de `gerar_ranking`, e adicionar a célula/coluna no template. Também vou ajustar os dados dos testes de rota para refletirem o contrato completo, preservando o teste de estado vazio e a ordem recebida.

Aplicar Patch

Generating patch (113 lines) in , , , 

A alteração foi aplicada nos quatro pontos necessários: domínio, template e testes unitários/de rota. Agora vou executar imediatamente a suíte pytest, que é a checagem mais direta para confirmar regra, ordenação, renderização e estado vazio.

Ran terminal command: python -m pytest

A suíte completa passou: 15 testes, incluindo os novos casos de tendência. Vou fazer uma verificação final de diagnóstico e de diff para confirmar que não há erro sintático/lint evidente nem alterações fora do escopo antes de encerrar.

Ran terminal command: git diff --check

Ran terminal command: git diff -- src/market/calculos.py templates/ranking.html tests/test_calculos.py tests/test_app.py

Checked , , , no problems found

Implementação concluída.

Alterações:
- Regra de domínio em `calculos.py`: `POSITIVA`, `NEGATIVA` ou `NEUTRA`.
- Nova coluna `Tendência` em `ranking.html`.
- Testes atualizados em `test_calculos.py` e `test_app.py`.

Validação:
- `python -m pytest`: **15 testes aprovados**
- Diagnósticos sem erros.
- `git diff --check` sem problemas.

Decisão técnica: a classificação é calculada em `gerar_ranking`, mantendo o template responsável apenas pela apresentação. Nenhum commit foi criado.

### Execução 2 — Autonomia alta

**Branch:** `experimento/autonomia-alta`

**Modo utilizado:** GitHub Copilot Agent com maior autonomia e aprovação automática das ações permitidas.

**Tarefa:** adicionar classificação de tendência ao ranking de ações.

**Início:** 12:07  
**Fim:** 12:12  
**Tempo total:** 5 minutos

**Aprovações manuais:** 1

**Sensação de controle:** 1/5  
**Risco percebido:** 3/5

**Resultado:** implementação concluída com alterações na lógica de domínio,
template e testes.

**Validação:** `13 passed`.

**Observação inicial:** o número de aprovações manuais caiu de cinco para uma,
mas a sensação de controle também diminuiu. A execução apresentou tentativas
de edição que falharam e foram refeitas automaticamente pelo agente.

**Log da execução:**
Lendo , linhas 1 para 220
Completed with input: {
  "path": "C:\\Users\\rafae\\OneDrive\\Área de Trabalho\\ia-dev-lab\\.github\\instructions\\tests.instructions.md",
  "view_range": [
    1,
    220
  ]
}

Procurando por `ranking|/ranking|retorno médio|monthly return|avg.*return|tendencia|trend`

Lendo , linhas 1 para 200
Completed with input: {
  "path": "C:\\Users\\rafae\\OneDrive\\Área de Trabalho\\ia-dev-lab",
  "view_range": [
    1,
    200
  ]
}

Lendo , linhas 1 para 220
Completed with input: {
  "path": "C:\\Users\\rafae\\OneDrive\\Área de Trabalho\\ia-dev-lab\\tests\\test_calculos.py",
  "view_range": [
    1,
    220
  ]
}

Procurando por `gerar_ranking|ranking|retorno_medio_mensal|retorno_medio_men|template|/ranking`

Lendo , linhas 1 para 260
Completed with input: {
  "path": "C:\\Users\\rafae\\OneDrive\\Área de Trabalho\\ia-dev-lab\\src\\market\\calculos.py",
  "view_range": [
    1,
    260
  ]
}

Lendo , linhas 1 para 260
Completed with input: {
  "path": "C:\\Users\\rafae\\OneDrive\\Área de Trabalho\\ia-dev-lab\\app.py",
  "view_range": [
    1,
    260
  ]
}

Lendo , linhas 1 para 220
Completed with input: {
  "path": "C:\\Users\\rafae\\OneDrive\\Área de Trabalho\\ia-dev-lab\\templates\\ranking.html",
  "view_range": [
    1,
    220
  ]
}

Lendo , linhas 1 para 220
Completed with input: {
  "path": "C:\\Users\\rafae\\OneDrive\\Área de Trabalho\\ia-dev-lab\\src\\market\\dados_demo.py",
  "view_range": [
    1,
    220
  ]
}

Procurando por `ranking\)|/ranking|render_template\(|Tendência|retorno_medio_mensal_percentua...`

Lendo , linhas 1 para 220
Completed with input: {
  "path": "C:\\Users\\rafae\\OneDrive\\Área de Trabalho\\ia-dev-lab\\tests\\test_app.py",
  "view_range": [
    1,
    220
  ]
}

"Editar Arquivo" falhou
Completed with input: {
  "path": "C:\\Users\\rafae\\OneDrive\\Área de Trabalho\\ia-dev-lab\\src\\market\\calculos.py",
  "old_str": "from collections.abc import Mapping, Sequence\nfrom numbers import Real\n\n\ndef calcular_retorno_medio_mensal(precos: Sequence[float]) -> float:\n    \"\"\"Calcula a média dos retornos percentuais de seis meses.\"\"\"\n    if len(precos) != 7:\n        raise ValueError(\"É necessário informar exatamente 7 preços.\")\n\n    if any(isinstance(preco, bool) or not isinstance(preco, Real) for preco in precos):\n        raise ValueError(\"Todos os preços devem ser numéricos.\")\n\n    if any(preco <= 0 for preco in precos):\n        raise ValueError(\"Todos os preços devem ser maiores que zero.\")\n\n    retornos = [\n        ((preco_atual / preco_anterior) - 1) * 100\n        for preco_anterior, preco_atual in zip(precos, precos[1:])\n    ]\n\n    return sum(retornos) / len(retornos)\n\n\ndef gerar_ranking(ativos: Mapping[str, Sequence[float]]) -> list[dict[str, float | str]]:\n    \"\"\"Gera o ranking dos ativos válidos em ordem decrescente de desempenho.\"\"\"\n    resultados = []\n\n    for ticker, precos in ativos.items():\n        try:\n            retorno = calcular_retorno_medio_mensal(precos)\n        except ValueError:\n            continue\n\n        resultados.append(\n            {\n                \"ticker\": ticker,\n                \"retorno_medio_mensal_percentual\": retorno,\n            }\n        )\n\n    return sorted(\n        resultados,\n        key=lambda item: item[\"retorno_medio_mensal_percentual\"],\n        reverse=True,\n    )\n",
  "new_str": "from collections.abc import Mapping, Sequence\nfrom numbers import Real\n\n\ndef classificar_tendencia(retorno_medio_mensal: float) -> str:\n    \"\"\"Classifica a tendência com base no retorno médio mensal.\"\"\"\n    if retorno_medio_mensal > 0:\n        return \"POSITIVA\"\n    if retorno_medio_mensal < 0:\n        return \"NEGATIVA\"\n    return \"NEUTRA\"\n\n\ndef calcular_retorno_medio_mensal(precos: Sequence[float]) -> float:\n    \"\"\"Calcula a média dos retornos percentuais de seis meses.\"\"\"\n    if len(precos) != 7:\n        raise ValueError(\"É necessário informar exatamente 7 preços.\")\n\n    if any(isinstance(preco, bool) or not isinstance(preco, Real) for preco in precos):\n        raise ValueError(\"Todos os preços devem ser numéricos.\")\n\n    if any(preco <= 0 for preco in precos):\n        raise ValueError(\"Todos os preços devem ser maiores que zero.\")\n\n    retornos = [\n        ((preco_atual / preco_anterior) - 1) * 100\n        for preco_anterior, preco_atual in zip(precos, precos[1:])\n    ]\n\n    return sum(retornos) / len(retornos)\n\n\ndef gerar_ranking(ativos: Mapping[str, Sequence[float]]) -> list[dict[str, float | str]]:\n    \"\"\"Gera o ranking dos ativos válidos em ordem decrescente de desempenho.\"\"\"\n    resultados = []\n\n    for ticker, precos in ativos.items():\n        try:\n            retorno = calcular_retorno_medio_mensal(precos)\n        except ValueError:\n            continue\n\n        resultados.append(\n            {\n                \"ticker\": ticker,\n                \"retorno_medio_mensal_percentual\": retorno,\n                \"tendencia\": classificar_tendencia(retorno),\n            }\n        )\n\n    return sorted(\n        resultados,\n        key=lambda item: item[\"retorno_medio_mensal_percentual\"],\n        reverse=True,\n    )\n"
}

Editando 

Editando 

Editando 

Editando 

Editando 

Editando 

Editando 

"Editar Arquivo" falhou
Completed with input: {
  "path": "C:\\Users\\rafae\\OneDrive\\Área de Trabalho\\ia-dev-lab\\tests\\test_app.py",
  "old_str": "def test_ranking_exibe_subconjunto_valido_recebido(monkeypatch, client):\n    ranking = [\n        {\n            \"ticker\": \"VALIDO_A\",\n            \"retorno_medio_mensal_percentual\": 10.0,\n        },\n        {\n            \"ticker\": \"VALIDO_B\",\n            \"retorno_medio_mensal_percentual\": 5.0,\n        },\n    ]\n\n    monkeypatch.setattr(\"app.gerar_ranking\", lambda _ativos: ranking)\n\n    response = client.get(\"/ranking\")\n    body = response.get_data(as_text=True)\n\n    assert response.status_code == 200\n    assert \"VALIDO_A\" in body\n    assert \"VALIDO_B\" in body\n    assert body.index(\"VALIDO_A\") < body.index(\"VALIDO_B\")\n",
  "new_str": "def test_ranking_exibe_subconjunto_valido_recebido(monkeypatch, client):\n    ranking = [\n        {\n            \"ticker\": \"VALIDO_A\",\n            \"retorno_medio_mensal_percentual\": 10.0,\n            \"tendencia\": \"POSITIVA\",\n        },\n        {\n            \"ticker\": \"VALIDO_B\",\n            \"retorno_medio_mensal_percentual\": 5.0,\n            \"tendencia\": \"POSITIVA\",\n        },\n    ]\n\n    monkeypatch.setattr(\"app.gerar_ranking\", lambda _ativos: ranking)\n\n    response = client.get(\"/ranking\")\n    body = response.get_data(as_text=True)\n\n    assert response.status_code == 200\n    assert \"VALIDO_A\" in body\n    assert \"VALIDO_B\" in body\n    assert body.index(\"VALIDO_A\") < body.index(\"VALIDO_B\")\n"
}

Lendo , linhas 1 para 180
Completed with input: {
  "path": "C:\\Users\\rafae\\OneDrive\\Área de Trabalho\\ia-dev-lab\\tests\\test_app.py",
  "view_range": [
    1,
    180
  ]
}

"Editar Arquivo" falhou
Completed with input: {
  "path": "C:\\Users\\rafae\\OneDrive\\Área de Trabalho\\ia-dev-lab\\tests\\test_app.py",
  "old_str": "def test_ranking_exibe_subconjunto_valido_recebido(monkeypatch, client):\n    ranking = [\n        {\n            \"ticker\": \"VALIDO_A\",\n            \"retorno_medio_mensal_percentual\": 10.0,\n        },\n        {\n            \"ticker\": \"VALIDO_B\",\n            \"retorno_medio_mensal_percentual\": 5.0,\n        },\n    ]\n\n    monkeypatch.setattr(\"app.gerar_ranking\", lambda _ativos: ranking)\n\n    response = client.get(\"/ranking\")\n    body = response.get_data(as_text=True)\n\n    assert response.status_code == 200\n    assert \"VALIDO_A\" in body\n    assert \"VALIDO_B\" in body\n    assert body.index(\"VALIDO_A\") < body.index(\"VALIDO_B\")\n",
  "new_str": "def test_ranking_exibe_subconjunto_valido_recebido(monkeypatch, client):\n    ranking = [\n        {\n            \"ticker\": \"VALIDO_A\",\n            \"retorno_medio_mensal_percentual\": 10.0,\n            \"tendencia\": \"POSITIVA\",\n        },\n        {\n            \"ticker\": \"VALIDO_B\",\n            \"retorno_medio_mensal_percentual\": 5.0,\n            \"tendencia\": \"POSITIVA\",\n        },\n    ]\n\n    monkeypatch.setattr(\"app.gerar_ranking\", lambda _ativos: ranking)\n\n    response = client.get(\"/ranking\")\n    body = response.get_data(as_text=True)\n\n    assert response.status_code == 200\n    assert \"VALIDO_A\" in body\n    assert \"VALIDO_B\" in body\n    assert body.index(\"VALIDO_A\") < body.index(\"VALIDO_B\")\n"
}

Editando 

Editando 

Lendo , linhas 1 para 220
Completed with input: {
  "path": "C:\\Users\\rafae\\OneDrive\\Área de Trabalho\\ia-dev-lab\\src\\market\\calculos.py",
  "view_range": [
    1,
    220
  ]
}

Lendo , linhas 1 para 120
Completed with input: {
  "path": "C:\\Users\\rafae\\OneDrive\\Área de Trabalho\\ia-dev-lab\\templates\\ranking.html",
  "view_range": [
    1,
    120
  ]
}

Lendo , linhas 1 para 180
Completed with input: {
  "path": "C:\\Users\\rafae\\OneDrive\\Área de Trabalho\\ia-dev-lab\\tests\\test_app.py",
  "view_range": [
    1,
    180
  ]
}

Lendo , linhas 1 para 180
Completed with input: {
  "path": "C:\\Users\\rafae\\OneDrive\\Área de Trabalho\\ia-dev-lab\\tests\\test_calculos.py",
  "view_range": [
    1,
    180
  ]
}

Ran terminal command: python -m pytest -q

Ran terminal command: git --no-pager diff --stat

Tarefa concluída e parada para revisão humana.

- Arquivos alterados:
  - [src/market/calculos.py](C:/Users/rafae/OneDrive/Área de Trabalho/ia-dev-lab/src/market/calculos.py) — adicionei a lógica de domínio `classificar_tendencia`, e o `gerar_ranking` agora inclui o campo `tendencia` em cada item do ranking.
  - [templates/ranking.html](C:/Users/rafae/OneDrive/Área de Trabalho/ia-dev-lab/templates/ranking.html) — incluo a nova coluna `Tendência` e renderizo o valor vindo do domínio, sem recalcular no template.
  - [tests/test_calculos.py](C:/Users/rafae/OneDrive/Área de Trabalho/ia-dev-lab/tests/test_calculos.py) — atualizei e ampliados os testes para cobrir tendência positiva, negativa, neutra e o ranking.
  - [tests/test_app.py](C:/Users/rafae/OneDrive/Área de Trabalho/ia-dev-lab/tests/test_app.py) — validez da rota `/ranking` com a nova coluna e preservação do estado vazio/ordenação.

- Testes executados:
  - `python -m pytest -q`
  - Resultado: `13 passed in 0.69s`

- Decisões técnicas:
  - A classificação foi definida na camada de domínio, não no template.
  - Regra aplicada: `> 0 => "POSITIVA"`, `< 0 => "NEGATIVA"`, `== 0 => "NEUTRA"`.
  - Mantive a ordenação do ranking por retorno médio mensal e o comportamento do estado vazio sem alterações relevantes.
  - Não adicionei dependências externas e não fiz commit.

## Etapa 2 — TDD como Guardrail

### Ciclo TDD — Estado RED

**Branch:** `experimento/tdd-filtro-retorno`

**Baseline:** `13abe96`

**Funcionalidade:** filtro do ranking por retorno mínimo.

A primeira solicitação ao agente foi limitada à criação dos testes, sem
autorização para modificar código de produção.

Foram criados quatro cenários:

- remoção de ativos abaixo do limite;
- inclusão do ativo exatamente igual ao limite;
- preservação da ordem original;
- comportamento com ranking vazio.

A execução dos testes entrou em estado RED porque a função
`filtrar_ranking_por_retorno_minimo` ainda não existia. Nenhum código de
produção foi alterado antes desta execução.

**Evidência:** `docs/harness/tdd-red.log`

### Ciclo TDD — Estado GREEN

Após registrar os testes em estado RED, foi solicitado ao agente que
implementasse apenas o código mínimo necessário para fazê-los passar.

Foi adicionada a função `filtrar_ranking_por_retorno_minimo` em
`src/market/calculos.py`.

Nenhum teste existente foi alterado durante a implementação.

**Testes de domínio:** 13 aprovados.  
**Suíte completa:** 17 aprovados.

O estado GREEN foi atingido mantendo os mesmos testes que haviam sido
registrados previamente no estado RED.

**Evidência:** `docs/harness/tdd-green.log`

### Interação entre TDD e o guardrail

Ao tentar registrar o estado GREEN em um commit separado, o guardrail criado
na Etapa 1 bloqueou inicialmente a implementação porque não havia alteração
em `tests/` no mesmo commit.

Entretanto, os testes haviam sido criados propositalmente no commit anterior,
seguindo o ciclo TDD. A verificação do histórico confirmou que o commit
`226cbbb` continha `tests/test_calculos.py`.

Esse comportamento mostrou uma limitação da primeira versão do controle:
ela verificava somente os arquivos preparados para o commit atual e não
considerava um fluxo RED → GREEN registrado em commits separados.

O hook foi então ajustado para permitir um modo explícito `TDD_GREEN=1`.
Nesse modo, o controle somente permite uma alteração de produção sem testes
no mesmo commit quando o commit anterior contém alterações em `tests/` e
quando a suíte completa é executada com sucesso.

O novo comportamento foi testado na implementação do filtro por retorno
mínimo. A suíte apresentou `17 passed` e somente depois disso o hook permitiu
o commit GREEN.

Evidências:
- `docs/harness/tdd-guardrail-bloqueio.log`
- `docs/harness/tdd-guardrail-green.log`
- `docs/harness/tdd-green.log`