# Comparação entre as versões do diagrama C4

Foram geradas duas representações da arquitetura atual do projeto.

## Versão 1

A primeira versão utilizou um `flowchart` Mermaid e representou separadamente
a aplicação Flask, o módulo de domínio, a fonte de dados de demonstração e o
template Jinja2.

Essa abordagem facilitou a visualização do fluxo interno da aplicação e mostrou
com clareza quais arquivos participam de cada etapa do processamento.

Entretanto, essa representação pode sugerir que `calculos.py`,
`dados_demo.py` e `ranking.html` são unidades arquiteturais independentes,
quando na prática todos fazem parte da mesma aplicação executável.

## Versão 2

A segunda versão utilizou a notação `C4Container` e considerou como contêiner
somente a aplicação web Flask.

Os módulos de cálculo, dados e apresentação foram descritos como
responsabilidades internas desse contêiner, evitando representá-los como
serviços separados.

Essa versão possui menos detalhes internos, mas comunica de maneira mais
precisa a arquitetura no nível C4 de Contêiner.

## Comparação

A primeira versão é mais útil para compreender o fluxo interno do código,
pois evidencia como Flask, dados, domínio e template se relacionam.

A segunda versão é mais adequada para representar a arquitetura no nível C4
solicitado, porque considera um contêiner como uma unidade executável ou
implantável e evita tratar arquivos internos como contêineres independentes.

## Decisão

**A Versão 2 foi escolhida como representação principal da arquitetura.**

A Versão 1 será preservada como evidência da primeira abordagem e também pode
ser útil como visão complementar da organização interna.

A comparação mostrou que adicionar mais detalhes ao diagrama nem sempre melhora
a comunicação arquitetural. Para o nível C4 de Contêiner, uma representação
mais simples transmitiu com maior precisão como o sistema é realmente
executado.