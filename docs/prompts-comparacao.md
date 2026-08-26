# Comparação de Prompts

## Funcionalidade escolhida

Implementação de uma função em Python para calcular a média de crescimento de uma ação nos últimos seis meses.

A funcionalidade será utilizada futuramente no processamento dos dados financeiros da aplicação.

---

## Teste 1 — Prompt fraco

### Modelo utilizado

A versão gratuita do GitHub Copilot setou como modelo AUTO e não me deixou escolher outro modelo pra validar diferentes prompts

### Prompt

> Crie uma função em Python que calcule a média de crescimento de uma ação nos últimos 6 meses.

### Resposta gerada

Vou localizar o módulo de mercado e os testes existentes para alinhar a proposta ao padrão do projeto e verificar como os dados históricos são representados. Como esta sessão está em modo somente leitura, vou apresentar a implementação sugerida sem alterar arquivos.

O módulo `market` e a pasta `tests` ainda estão vazios, e o próprio projeto registra que a fórmula de crescimento ainda não foi definida. Portanto, a decisão essencial é explicitar uma regra mínima e verificável antes de codificar: crescimento percentual total no período, dividido pelo número de intervalos entre observações.

Read skill `python-fact-grounded-coding`

A fórmula ainda não foi definida no projeto, conforme `AGENTS.md`. Uma interpretação simples é calcular a média das variações percentuais entre os preços dos seis meses:

```python
from collections.abc import Sequence


def calcular_media_crescimento(precos: Sequence[float]) -> float:
    """Retorna a média percentual de crescimento entre os preços mensais."""
    if len(precos) != 6:
        raise ValueError("É necessário informar exatamente 6 preços mensais.")

    if any(preco <= 0 for preco in precos):
        raise ValueError("Os preços devem ser maiores que zero.")

    crescimentos = [
        (precos[indice] - precos[indice - 1]) / precos[indice - 1]
        for indice in range(1, len(precos))
    ]

    return sum(crescimentos) / len(crescimentos) * 100
```

Exemplo:

```python
media = calcular_media_crescimento([100, 105, 102, 110, 115, 120])
print(f"{media:.2f}%")
```
### Observações

Com a orientação genérica, o modelo assumiu por necessidade uma premissa de cálculo sem validar com o desenvolvedor. Por outro lado, ele fez validações interessantes como a quantidade de parâmetros recebidos e o valor repassado e, como na própria resposta fica claro, ele procurou no arquivo AGENTS.md se havia alguma orientação sobre como calcular o crescimento. 
---

## Teste 2 — Prompt eficaz

### Modelo utilizado

A versão gratuita do GitHub Copilot setou como modelo AUTO e não me deixou escolher outro modelo pra validar diferentes prompts

### Prompt

Você está trabalhando em um projeto pyrhon que cria uma aplicação web para analisar o desempenho de ações brasileiras no mercado de ações B3. A lógica de cálculo deve permanecer separada da consulta à API e da interface web. Implemente a função python chamada calcular_retorno_medio_mensal que calcule a média dos retornos percentuais mensais de uma ação ao longo de seis meses. 
Entrada: a função deve receber uma sequência contento exatamente 7 preços de fechamento mensal em órdem cronológica. São necessários 7 preços porque eles representam o preço inicial e os seis meses seguintes, permitindo calcular exatamente 6 retornos mensais consecutivos. Para cada período, utilize:
retorno = ((preco_atual/preco_anterior)-1)*100
Depois calcule a média aritmética dos seis retornos obtidos.
Exemplo:
[100, 110, 121, 133.1, 146.41, 161.051, 177.1561]

cada intervalo apresenta crescimento de aproximadamente 10%, portanto o resultado esperado da função é aproximadamente:

10.0

Retrições:
- Utilize Python.
- A função deve ter responsabilidade exclusiva pelo cálculo.
- Não faça chamadas a APIs.
- Não utilize Flask, Jinja2 ou qualquer lógica de interface.
- Não adicione dependências externas.
- Utilize nomes de variáveis descritivos.
- Inclua type hint e uma docstring curta.
- A entrada deve conter exatamente 7 valores.
- Todos os preços devem ser numéricos e maiores que zero.
- Para uma entrada inválida, lance `ValueError` com uma mensagem clara.

### Validação
Após implementar a função:

1. demonstre seu funcionamento utilizando o exemplo fornecido e confirme que o resultado é aproximadamente `10.0`;
2. apresente um exemplo com quantidade incorreta de preços;
3. apresente um exemplo contendo preço igual ou menor que zero;
4. explique brevemente por que 7 preços são necessários para calcular 6 retornos mensais.
5. Não adicione funcionalidades além das solicitadas

### Resposta gerada
Vou localizar o módulo de mercado e os testes existentes para identificar o ponto correto da função e verificar as convenções do projeto. Como esta sessão está em modo somente leitura, depois apresentarei a implementação e a validação sugeridas sem alterar arquivos.

Searched for files matching `**/*.py`, 1 match

O ponto de extensão está confirmado: `market` e `tests` estão vazios, então não há implementação ou teste vizinho para reutilizar. A hipótese local é que a função deve ser criada em um módulo pequeno de cálculo dentro de `market`, sem dependências; a checagem decisiva será executar a fórmula do exemplo e verificar as validações de tamanho e preços. Vou apenas confirmar a organização mínima do projeto antes de descrever o patch.

A função deve ficar em um módulo isolado, por exemplo `src/market/calculos.py`:

```python
from collections.abc import Sequence
from numbers import Real


def calcular_retorno_medio_mensal(precos: Sequence[float]) -> float:
    """Calcula a média dos retornos percentuais de seis meses."""
    if len(precos) != 7:
        raise ValueError("É necessário informar exatamente 7 preços.")

    if any(isinstance(preco, bool) or not isinstance(preco, Real) for preco in precos):
        raise ValueError("Todos os preços devem ser numéricos.")

    if any(preco <= 0 for preco in precos):
        raise ValueError("Todos os preços devem ser maiores que zero.")

    retornos = [
        ((preco_atual / preco_anterior) - 1) * 100
        for preco_anterior, preco_atual in zip(precos, precos[1:])
    ]

    return sum(retornos) / len(retornos)
```

Validação:

```python
precos = [100, 110, 121, 133.1, 146.41, 161.051, 177.1561]
resultado = calcular_retorno_medio_mensal(precos)

print(resultado)  # aproximadamente 10.0

try:
    calcular_retorno_medio_mensal([100, 110, 121])
except ValueError as erro:
    print(erro)  # É necessário informar exatamente 7 preços.

try:
    calcular_retorno_medio_mensal([100, 110, 121, 133.1, 146.41, 0, 177.1561])
except ValueError as erro:
    print(erro)  # Todos os preços devem ser maiores que zero.
```

Sete preços são necessários porque seis retornos usam seis pares consecutivos: preço inicial com o primeiro mês, primeiro mês com o segundo, e assim por diante até o sexto mês.



### Observações

O prompt eficaz eliminou as principais ambiguidades presentes no primeiro teste ao definir explicitamente a fórmula, a quantidade de preços, o número de intervalos e o comportamento esperado para entradas inválidas. A implementação gerada ficou alinhada com a lógica definida para a aplicação e manteve a responsabilidade da função restrita ao cálculo financeiro. O modelo também apresentou as validações solicitadas e explicou corretamente por que sete preços são necessários para calcular seis retornos mensais.

---

## Comparação

O prompt fraco deixou em aberto conceitos importantes, como a definição de crescimento médio e a quantidade de preços necessária, fazendo com que o modelo assumisse essas decisões durante a implementação. Como consequência, foram utilizados seis preços para calcular apenas cinco variações mensais, resultado diferente da regra posteriormente definida para o projeto. No prompt eficaz, o fornecimento de contexto, fórmula, exemplo, restrições e critérios de validação eliminou essas ambiguidades e produziu uma solução mais previsível e alinhada ao requisito. A comparação demonstrou que o contexto do repositório auxilia o modelo, mas uma especificação clara no próprio prompt é essencial para reduzir interpretações e melhorar a qualidade do código gerado.

## Limitação na comparação entre modelos

Durante a realização da atividade foi utilizada a versão gratuita do GitHub Copilot. Nessa configuração, o modelo permaneceu definido como `AUTO`, sem disponibilizar ao usuário a seleção manual de outro modelo para repetir o experimento com uma opção de menor performance.

Por esse motivo, os testes de prompt fraco e prompt eficaz foram realizados sob a mesma configuração automática do GitHub Copilot, e não foi possível executar a comparação adicional entre modelos.