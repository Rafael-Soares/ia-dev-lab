# Comparação entre OpenSpec e SpecKit

## 1. Objetivo da comparação

As duas abordagens de Spec-Driven Development foram aplicadas ao mesmo
problema: geração de um ranking de ações com base no desempenho médio mensal
dos últimos seis meses e sua apresentação em uma interface web.

As implementações foram desenvolvidas em branches independentes, partindo
da mesma base do projeto, permitindo comparar não apenas os artefatos
documentais gerados, mas também o processo de desenvolvimento, a arquitetura
resultante e o papel da revisão humana.

---

## 2. Artefatos produzidos

### OpenSpec

O OpenSpec organizou o trabalho principalmente em torno de um change
denominado `ranking-acoes`.

Os principais artefatos produzidos foram:

- `proposal.md`;
- `design.md`;
- capability `ranking-acoes`;
- capability `visualizacao-ranking`;
- `tasks.md`;
- configuração própria do OpenSpec.

Também foram produzidos documentos adicionais de revisão humana,
registrando alterações no plano, revisão de diffs e checkpoint humano.

### SpecKit

O SpecKit produziu um conjunto mais amplo de artefatos antes da implementação:

- `constitution.md`;
- `spec.md`;
- `requirements.md`;
- `plan.md`;
- `research.md`;
- `data-model.md`;
- contrato da interface web;
- `quickstart.md`;
- `tasks.md`.

A abordagem também criou infraestrutura própria em `.specify/`, incluindo
scripts, templates e workflows.

---

## 3. Organização do processo SDD

### OpenSpec

O fluxo utilizado foi aproximadamente:

1. definição do escopo;
2. criação da proposta;
3. definição das capabilities;
4. elaboração do design;
5. geração do plano de tarefas;
6. revisão humana das tarefas;
7. implementação incremental;
8. revisão dos diffs;
9. testes;
10. validação dos cenários;
11. checkpoint humano.

A abordagem mostrou-se relativamente direta, concentrando os artefatos
relacionados à mudança em um único diretório.

### SpecKit

O fluxo utilizado foi:

1. definição do escopo;
2. definição da constituição do projeto;
3. geração da especificação;
4. revisão humana da especificação;
5. elaboração do plano técnico;
6. geração de research, data model, contrato e quickstart;
7. geração do plano de tarefas;
8. revisão e redução humana do backlog;
9. criação dos testes antes da implementação;
10. ciclo RED → GREEN para o domínio;
11. ciclo RED → GREEN para a interface;
12. execução da suíte completa;
13. auditoria final da especificação e da constituição.

O SpecKit introduziu uma camada adicional de governança por meio da
Constitution, utilizada como referência para decisões posteriores.

---

## 4. Revisão humana

A revisão humana foi necessária nas duas abordagens, porém ocorreu em
momentos diferentes e com naturezas distintas.

### OpenSpec

Durante a execução foram identificados:

- antecipação de tarefas pelo agente;
- implementação de funcionalidades antes do momento previsto no plano;
- utilização inicial de tickers reais em dados descritos como fictícios;
- teste web que inicialmente não comprovava adequadamente a responsabilidade
  da camada de domínio;
- necessidade de revisar a correspondência entre tasks e implementação.

Algumas alterações produzidas pelo agente foram mantidas porque estavam
corretas, mesmo tendo sido realizadas antes da tarefa prevista.

### SpecKit

Durante a revisão foram identificados:

- ausência inicial da fórmula matemática completa na especificação;
- tentativa de tratar ordem cronológica como algo verificável mesmo sem datas;
- atributo `posição` inicialmente modelado como estado do domínio;
- backlog inicial excessivamente fragmentado, com 25 tarefas;
- proposta de criação de um helper de validação que poderia duplicar lógica;
- testes inicialmente escritos com problemas de contrato e isolamento;
- necessidade de separar claramente testes de domínio e testes da interface.

O backlog foi reduzido de 25 para 15 tarefas antes da implementação.

---

## 5. Desenvolvimento orientado por testes


Essa seção é sustentada diretamente pelo diff. O OpenSpec usa `Sequence[dict]`, enquanto o SpecKit usa `Mapping[str, Sequence[float]]`, e até os nomes dos campos de saída diferem. :contentReference[oaicite:0]{index=0}

Nos dados de demonstração também há uma diferença clara: o OpenSpec gera séries por uma função auxiliar, enquanto o SpecKit usa um dicionário explícito e retorna uma cópia. :contentReference[oaicite:1]{index=1}

Na web, o OpenSpec acrescentou CSS e execução direta por `python app.py`, enquanto o SpecKit ficou mais mínimo. :contentReference[oaicite:2]{index=2} O template SpecKit também usa explicitamente `retorno_medio_mensal_percentual`, enquanto o OpenSpec usava `retorno_medio_mensal`. :contentReference[oaicite:3]{index=3}

E a diferença nos testes ficou bastante concreta: o SpecKit separou ordem, estado vazio e subconjunto válido em testes web distintos e usou uma fixture `client`, enquanto o OpenSpec terminou com uma organização mais compacta. :contentReference[oaicite:4]{index=4}

### Minha conclusão comparativa

Para **este projeto pequeno**, eu colocaria a conclusão assim:

> O OpenSpec apresentou melhor relação entre formalização e simplicidade, produzindo menos artefatos intermediários e permitindo chegar mais rapidamente à implementação. O SpecKit forneceu maior rastreabilidade e governança, principalmente por meio da Constitution, dos artefatos de planejamento e dos ciclos TDD explícitos, mas exigiu maior esforço de revisão e simplificação para evitar excesso de documentação e fragmentação de tarefas. Em ambas as abordagens, a revisão humana foi indispensável para corrigir ambiguidades, controlar escopo e verificar se testes e código realmente comprovavam os requisitos.

Isso não declara uma ferramenta “melhor” universalmente; relaciona o resultado ao tamanho e contexto do experimento.

### OpenSpec

Os testes foram implementados durante a evolução da funcionalidade e usados
para validar os comportamentos definidos nas capabilities.

### SpecKit

Foram registrados dois ciclos completos de TDD.

#### Domínio

RED:

- 4 testes existentes passavam;
- 3 novos testes falhavam porque `gerar_ranking` ainda não existia.

Após a implementação:

- 7 testes de domínio passaram.

#### Interface

RED:

- os testes web não podiam ser coletados porque `app.py` ainda não existia.

Após a implementação da rota e do template:

- 4 testes web passaram;
- os 7 testes de domínio permaneceram aprovados.

A suíte final apresentou:

`11 passed`

Esse histórico tornou explícita a relação entre especificação, teste e
implementação.

---

## 6. Arquitetura resultante

As duas abordagens convergiram para uma arquitetura semelhante:

dados
→ lógica de domínio
→ aplicação Flask
→ template Jinja2

Em ambas, a camada de apresentação não realiza o cálculo do desempenho e
não deve reordenar os resultados.

Apesar dessa convergência, ocorreram diferenças na API de domínio.

### OpenSpec

A implementação utilizou uma coleção de objetos contendo informações como
`ticker` e `precos`.

### SpecKit

A implementação resultante utilizou um mapping no formato:

`ticker → sequência de preços`

e criou a função:

`gerar_ranking(ativos)`

O resultado contém:

- ticker;
- retorno médio mensal percentual.

A posição não é armazenada no domínio e é derivada pela interface.

Essa diferença mostra que especificações funcionalmente equivalentes podem
produzir contratos internos diferentes dependendo das decisões realizadas
durante o processo SDD.

---

## 7. Pontos positivos

### OpenSpec

- estrutura relativamente simples;
- fácil associação entre change, design, capabilities e tarefas;
- menor quantidade de artefatos intermediários;
- fluxo direto entre especificação e implementação;
- capabilities facilitaram a separação entre ranking e visualização.

### SpecKit

- Constitution tornou explícitos princípios arquiteturais e de qualidade;
- maior rastreabilidade entre requisitos, plano, modelo, contrato e tarefas;
- melhor suporte ao planejamento antes da implementação;
- favoreceu a execução explícita do TDD;
- checkpoints e critérios de qualidade ficaram mais formalizados;
- permitiu identificar inconsistências antes do código ser produzido.

---

## 8. Pontos negativos

### OpenSpec

- parte das decisões precisou ser refinada manualmente durante o processo;
- o agente antecipou tarefas em alguns momentos;
- menor formalização de princípios globais do projeto;
- maior dependência da revisão humana para controlar os limites entre tarefas.

### SpecKit

- maior volume de arquivos e infraestrutura;
- planejamento inicial excessivamente detalhado para uma feature pequena;
- backlog original com 25 tarefas apresentou fragmentação artificial;
- alguns artefatos repetiam decisões já registradas em outros documentos;
- processo mais pesado para funcionalidades pequenas.

---

## 9. Comparação geral

O OpenSpec apresentou um fluxo mais enxuto e orientado diretamente à mudança,
enquanto o SpecKit apresentou um fluxo mais estruturado e orientado à
governança do desenvolvimento.

O OpenSpec foi mais eficiente para transformar rapidamente uma mudança
especificada em tarefas e implementação. O SpecKit, por outro lado,
forneceu maior rastreabilidade e criou mecanismos adicionais para controlar
decisões arquiteturais, testes e qualidade.

Nos dois casos, a revisão humana permaneceu necessária. Nenhuma das
ferramentas eliminou a necessidade de verificar requisitos, tarefas, testes
e diffs produzidos pelo agente.

A principal diferença observada não foi simplesmente a qualidade final do
código, mas a forma como cada abordagem estruturou o caminho entre requisito
e implementação.

## 10. Diferenças concretas na implementação

A comparação direta entre as duas branches mostrou que OpenSpec e SpecKit
produziram soluções funcionalmente equivalentes, porém com contratos internos
diferentes.

### Estrutura de entrada do domínio

No OpenSpec, a função de ranking recebe uma sequência de objetos:

```python
[
    {"ticker": "AAA", "precos": [...]},
    {"ticker": "BBB", "precos": [...]},
]