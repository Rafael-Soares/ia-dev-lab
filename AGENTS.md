# AGENTS.md

## Sobre o projeto

O `ia-dev-lab` é um projeto didático desenvolvido para praticar desenvolvimento de software assistido por Inteligência Artificial, versionamento com Git/GitHub, documentação, testes e boas práticas de engenharia de software.

O projeto consiste em uma aplicação web simples para análise de dados do mercado brasileiro de ações. A aplicação deverá consumir uma API pública de dados financeiros, obter informações históricas de ações brasileiras referentes aos últimos seis meses, processar esses dados e apresentar um ranking das ações com melhor desempenho no período.

O projeto possui finalidade exclusivamente educacional. Os resultados apresentados pela aplicação não constituem recomendação de investimento.

O desenvolvimento deve ser incremental, priorizando simplicidade, legibilidade e facilidade de revisão.

## Comandos

- `python hello.py` — executa o arquivo utilizado para validar inicialmente o ambiente Python.
- `python app.py` — executará a aplicação web localmente quando ela estiver implementada.
- `python -m pytest` — executará os testes automatizados quando eles estiverem implementados.

## Convenções de código

- Utilizar Python como linguagem principal do projeto.
- Escrever código simples, legível e de fácil manutenção.
- Utilizar nomes descritivos para funções, variáveis, classes e módulos.
- Preferir funções pequenas e com responsabilidade bem definida.
- Separar a lógica de acesso à API da lógica de processamento dos dados e da camada de apresentação.
- Tratar erros relacionados à comunicação com APIs externas.
- Validar os dados recebidos da API antes de processá-los.
- Criar testes automatizados para funções responsáveis pelos cálculos e processamento dos dados financeiros.
- Evitar duplicação de código.
- Adicionar comentários somente quando eles contribuírem para explicar decisões ou comportamentos que não sejam óbvios pelo próprio código.
- Manter alterações pequenas e fáceis de revisar.
- Antes de criar novos arquivos ou estruturas, verificar se eles são realmente necessários.
- Manter o projeto compatível com uma execução local simples.
- Não assumir uma fórmula para "crescimento médio" sem que a regra de cálculo esteja definida explicitamente no projeto.

## Não fazer

- Não adicionar funcionalidades fora do escopo definido para o projeto.
- Não implementar autenticação ou cadastro de usuários.
- Não adicionar banco de dados sem necessidade comprovada.
- Não adicionar frameworks ou bibliotecas apenas para aumentar a complexidade do projeto.
- Não adicionar dependências sem justificar sua necessidade.
- Não inserir tokens, chaves de API, senhas ou outras credenciais diretamente no código-fonte.
- Não versionar arquivos contendo credenciais ou informações sensíveis.
- Não apagar arquivos existentes sem justificativa.
- Não alterar arquivos que não estejam relacionados à tarefa solicitada.
- Não misturar acesso à API, processamento de dados e apresentação em uma única função extensa.
- Não inventar dados financeiros quando a API não retornar informações.
- Não inventar regras de cálculo financeiro que não tenham sido definidas no projeto.
- Não apresentar os resultados da aplicação como recomendação de compra ou venda de ativos.
- Não aceitar automaticamente código ou alterações produzidas por ferramentas de IA sem revisão humana.