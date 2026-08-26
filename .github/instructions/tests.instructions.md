---
applyTo: "tests/**/*.py"
---

# Instruções para testes

- Utilize pytest para os testes automatizados.
- Escreva nomes de testes descritivos que indiquem claramente o comportamento verificado.
- Cada teste deve validar um comportamento específico.
- Prefira testes simples e independentes.
- Não faça chamadas reais à API financeira durante testes unitários.
- Utilize dados controlados ou mocks quando for necessário simular respostas da API.
- Inclua testes para situações válidas e casos de erro relevantes.
- Para funções de cálculo financeiro, utilize valores conhecidos que permitam verificar facilmente o resultado esperado.