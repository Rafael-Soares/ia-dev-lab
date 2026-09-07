# ADR 0002 — Manter a arquitetura simples no estágio atual

## Status

Aceito

## Contexto

O projeto `ia-dev-lab` cresceu ao longo das atividades com novas regras de
domínio, testes, controles de desenvolvimento e uma interface web para
visualização do ranking.

A revisão arquitetural identificou uma separação clara entre a entrada Flask,
os dados de demonstração, a lógica de domínio, o template e os testes.

Também foram encontrados alguns pontos de acoplamento. O arquivo `app.py`
depende diretamente das funções de obtenção dos dados e geração do ranking,
enquanto o template e os testes conhecem as chaves dos dicionários produzidos
pelo domínio, como `ticker`, `retorno_medio_mensal_percentual` e `tendencia`.

Apesar desses pontos, o projeto ainda possui pequeno porte, uma única interface
web e não utiliza banco de dados ou integração com API financeira externa.

## Motivadores da decisão

- manter o projeto simples e adequado ao seu tamanho atual;
- evitar abstrações criadas apenas para antecipar necessidades futuras;
- preservar a boa testabilidade das funções de domínio;
- manter clara a separação já existente entre dados, domínio e apresentação;
- permitir reavaliação caso o sistema passe a integrar fontes externas ou
  novas interfaces.

## Opções consideradas

### 1. Manter a arquitetura atual

Continuar utilizando `app.py` como coordenador da aplicação, `dados_demo.py`
como fonte de dados e `calculos.py` para as regras de domínio.

### 2. Criar uma camada de serviço

Adicionar uma nova camada entre Flask, fonte de dados e domínio para coordenar
a geração, filtragem e limitação do ranking.

### 3. Criar estruturas e interfaces adicionais

Substituir os dicionários atuais por DTOs ou outras estruturas explícitas e
criar interfaces para as fontes de dados.

## Decisão

Foi decidido **manter a arquitetura atual sem extrair novos serviços ou
adicionar novas camadas neste momento**.

A complexidade atual não justifica a criação de uma camada de serviço,
repositórios ou outras abstrações adicionais.

O contrato baseado em dicionários entre domínio e apresentação continuará
sendo utilizado enquanto o projeto permanecer pequeno e com uma única
interface.

## Consequências positivas

- menor complexidade estrutural;
- menos arquivos e abstrações para manter;
- continuidade do modelo que já possui testes;
- domínio permanece independente de Flask e Jinja2;
- desenvolvimento de novas funcionalidades pequenas continua simples.

## Consequências negativas

- o template permanece dependente das chaves produzidas pelo domínio;
- `app.py` continua diretamente ligado ao provedor de dados e à geração do
  ranking;
- mudanças no formato dos resultados podem exigir alterações simultâneas em
  domínio, template e testes.

## Quando reconsiderar esta decisão

A decisão deverá ser revista caso ocorra uma ou mais das seguintes situações:

- integração com uma API financeira real;
- inclusão de banco de dados ou persistência;
- existência de mais de uma interface consumindo o domínio;
- aumento significativo das regras de ranking;
- crescimento do número de campos compartilhados entre domínio e apresentação.

Nesse cenário, poderá fazer sentido introduzir uma camada de coordenação e um
contrato de dados mais explícito.