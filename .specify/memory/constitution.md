<!--
Sync Impact Report:
Version change: n/a -> 1.0.0
List of modified principles: n/a -> I. Reutilização antes de duplicação; II. Separação de responsabilidades; III. Desenvolvimento orientado por testes; IV. Escopo mínimo; V. Revisão humana obrigatória; VI. Clareza e simplicidade
Added sections: Escopo e restrições do projeto; Fluxo de trabalho e revisão
Removed sections: none
Follow-up TODOs: none
-->

# ia-dev-lab Constitution

## Core Principles

### I. Reutilização antes de duplicação
A implementação deve reutilizar funções, módulos e componentes existentes sempre que a lógica já estiver atendendo ao requisito. Regras de negócio, cálculos e transformações definidos previamente não devem ser duplicados em novas camadas ou em rotas, templates ou utilitários paralelos.

A reutilização é obrigatória porque reduz inconsistências, preserva comportamentos já validados e mantém o projeto didático focado em práticas sustentáveis de manutenção. Quando houver necessidade de mudança, a correção deve ocorrer no ponto único de origem da regra.

### II. Separação de responsabilidades
Dados, lógica de domínio e apresentação web devem permanecer separados. A camada de interface não deve recalcular, reordenar ou reinterpretar resultados produzidos pela lógica de negócio; ela apenas apresenta os dados e encaminha interações do usuário.

Essa separação é necessária para manter clareza de fluxo, facilitar testes e evitar que decisões de negócio sejam espalhadas por código de apresentação. O cálculo de indicadores e o processamento dos dados devem residir em módulos específicos e ser consumidos pela aplicação web sem duplicação de responsabilidade.

### III. Desenvolvimento orientado por testes
Novas funcionalidades devem possuir testes correspondentes aos critérios de aceitação e os testes existentes devem permanecer aprovados antes da aceitação de mudanças. Cada regra de negócio relevante deve ser validada por um teste automatizado que descreva o comportamento esperado.

A prática de testes não é opcional: ela oferece evidência de que a funcionalidade atende ao escopo e reduz regressões durante a evolução do projeto. O ciclo deve seguir a lógica de verificar primeiro o comportamento esperado e, em seguida, implementar apenas o necessário para atender a esse critério.

### IV. Escopo mínimo
Implementar somente o necessário para atender à especificação do projeto. Não adicionar APIs externas, autenticação, banco de dados, notificações, integrações de terceiros ou outras funcionalidades não solicitadas pelo escopo educacional do laboratório.

O escopo mínimo evita dispersão de esforço, reduz risco de manutenção e preserva a intenção didática do projeto. Qualquer mudança fora do escopo deve ser tratada como requisito separado e explicitamente aprovado antes de ser incluída.

### V. Revisão humana obrigatória
Planos, tarefas e diffs produzidos por agentes de IA devem ser revisados por um humano antes da aceitação. O agente não deve considerar uma implementação finalizada unicamente porque os testes passam ou porque a alteração parece consistente.

A revisão humana é obrigatória porque garante qualidade, contexto e responsabilidade sobre decisões de implementação. Testes automatizados são evidência útil, mas não substituem a validação humana de clareza, intenção e aderência ao projeto.

### VI. Clareza e simplicidade
Preferir soluções pequenas, legíveis e adequadas ao caráter educacional do projeto. A implementação deve priorizar nomes descritivos, funções com responsabilidade bem definida e código fácil de seguir, sem abstrações desnecessárias ou engenharia excessiva.

A simplicidade é uma exigência de manutenção e aprendizado. Em um projeto didático, a qualidade do código depende da legibilidade e da capacidade de explicar o raciocínio de forma direta, sem aumentar complexidade artificialmente.

## Escopo e restrições do projeto

O projeto ia-dev-lab deve permanecer concentrado em desenvolvimento de software com IA, Git/GitHub, documentação e testes, com foco em uma aplicação web simples para análise de dados de mercado financeiro brasileiro.

As seguintes restrições são obrigatórias:

- Python é a linguagem principal do projeto.
- Flask deve ser utilizado para as rotas da aplicação web e Jinja2 para renderização das páginas.
- Dados financeiros externos devem ser tratados como dependência externa controlada e não devem introduzir regras arbitrárias sem definição explícita do projeto.
- O projeto deve evitar armazenamento persistente, autenticação de usuários, integrações complexas e frameworks frontend além do necessário.
- Resultados apresentados devem ser descritos como educacionais e não como recomendação de investimento.
- Alterações devem ser pequenas, rastreáveis e fáceis de revisar em diffs.

## Fluxo de trabalho e revisão

O desenvolvimento deve seguir um fluxo de trabalho baseado em clareza, validação e revisão:

- Requisitos e decisões relevantes devem ser documentados de forma compreensível.
- Mudanças devem ser pequenas e isoladas, com objetivo claro e sem espalhamento de responsabilidades.
- Testes devem ser mantidos como evidência de comportamento esperado e não como substituto para análise humana.
- Antes da aceitação final, o diff deve ser revisado para confirmar que atende ao escopo e não introduziu regressões ou complexidade desnecessária.
- Quando a implementação for auxiliada por agentes de IA, a revisão humana deve verificar a qualidade do código, a aderência à arquitetura e a coerência com as metas educacionais do projeto.

## Governance

A constituição deste projeto prevalece sobre convenções informais, boas práticas não documentadas e decisões executadas sem avaliação do escopo. Alterações na constituição devem ser registradas explicitamente, com justificativa, impacto e revisão humana.

Os critérios de alteração são:

- Mudanças de princípio ou remoção de regras exigem revisão e justificativa formal.
- Novos princípios ou expansões materiais devem atualizar a versão conforme a política semântica de versionamento.
- Ajustes de redação e correções de clareza sem mudança de regra devem ser tratados como correção de manutenção.
- Qualquer mudança relevante deve ser revisada antes da aceitação para verificar compatibilidade com o escopo e com as práticas obrigatórias do projeto.

A política de versionamento segue SemVer:

- MAJOR: remoções ou redefinições incompatíveis de princípios ou regras governamentais.
- MINOR: adição de novo princípio, seção ou expansão material de orientação.
- PATCH: correções de redação, clarificações e refinamentos sem impacto semântico relevante.

A conformidade deve ser avaliada em cada revisão significativa por verificação dos seguintes pontos:

- aderência ao escopo mínimo;
- separação correta de responsabilidades;
- presença e qualidade dos testes relevantes;
- reutilização de código e ausência de duplicação desnecessária;
- revisão humana documentada antes da aceitação final.

**Version**: 1.0.0 | **Ratified**: 2026-09-01 | **Last Amended**: 2026-09-01
