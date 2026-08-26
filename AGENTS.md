# AGENTS.md

## Sobre o projeto

O `ia-dev-lab` é um projeto didático desenvolvido para praticar desenvolvimento de software assistido por Inteligência Artificial, Git/GitHub, documentação e testes.

O projeto consiste em uma aplicação web simples para análise de dados do mercado brasileiro de ações. A aplicação consultará uma API pública de dados financeiros, processará dados históricos dos últimos seis meses e apresentará um ranking das ações com melhor desempenho.

A aplicação utiliza:

* Python como linguagem principal;
* Flask como framework web;
* Jinja2 para renderização das páginas HTML;
* HTML e CSS para a interface;
* pytest para testes automatizados.

A API financeira ainda será definida.

O projeto possui finalidade exclusivamente educacional. Os resultados apresentados não constituem recomendação de investimento.

## Comandos

* `python hello.py` — valida o ambiente Python.
* `python app.py` — executará a aplicação Flask quando implementada.
* `python -m pytest` — executa os testes automatizados.

## Convenções de código

* Utilizar Python como linguagem principal.
* Escrever código simples, legível e de fácil manutenção.
* Utilizar nomes descritivos para funções, variáveis, classes e módulos.
* Preferir funções pequenas e com responsabilidade bem definida.
* Separar acesso à API, processamento dos dados e apresentação.
* Utilizar Flask para as rotas da aplicação web.
* Utilizar Jinja2 para renderizar os dados nas páginas HTML.
* Manter templates HTML separados da lógica de processamento.
* Manter arquivos CSS e outros recursos estáticos separados dos templates.
* Tratar erros relacionados à comunicação com APIs externas.
* Validar os dados recebidos antes do processamento.
* Criar testes para funções responsáveis por cálculos e processamento financeiro.
* Evitar duplicação de código.
* Manter alterações produzidas por IA pequenas e fáceis de revisar.
* Não assumir uma fórmula para crescimento médio enquanto a regra não estiver definida explicitamente.

## Não fazer

* Não adicionar funcionalidades fora do escopo do projeto.
* Não implementar autenticação ou cadastro de usuários.
* Não adicionar banco de dados sem necessidade.
* Não adicionar dependências sem justificativa.
* Não adicionar frameworks frontend complexos sem uma nova decisão arquitetural.
* Não inserir chaves de API, tokens ou credenciais diretamente no código.
* Não versionar informações sensíveis.
* Não apagar arquivos existentes sem justificativa.
* Não alterar arquivos não relacionados à tarefa solicitada.
* Não misturar acesso à API, processamento dos dados e apresentação em uma única função extensa.
* Não inventar dados financeiros quando a API não retornar informações.
* Não inventar regras de cálculo financeiro não definidas pelo projeto.
* Não apresentar resultados como recomendação de investimento.
* Não aceitar automaticamente código produzido por IA sem revisão humana.
