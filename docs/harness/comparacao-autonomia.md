## Execução 2 — Autonomia alta

- **Tempo:** 5 minutos
- **Aprovações manuais:** 1
- **Sensação de controle:** 1/5
- **Risco percebido:** 3/5
- **Testes ao final:** 13 aprovados
- **Resultado:** tarefa concluída, com menor necessidade de intervenção manual.

## Comparação final

As duas execuções partiram do mesmo commit e receberam exatamente a mesma
tarefa, alterando apenas o nível de autonomia concedido ao agente.

No modo de autonomia controlada, a tarefa foi concluída em 3 minutos e exigiu
5 aprovações manuais. A sensação de controle foi avaliada em 3/5 e o risco
percebido em 3/5. No modo de autonomia alta, a tarefa levou 5 minutos, exigiu
apenas 1 aprovação manual, mas a sensação de controle caiu para 1/5. O risco
percebido permaneceu em 3/5.

A comparação dos diffs mostrou que os dois modos chegaram praticamente à mesma
implementação no código de produção. A principal diferença apareceu nos testes.
Na execução controlada, os três resultados possíveis da classificação de
tendência foram parametrizados e aparecem como casos de teste separados. Na
execução com maior autonomia, os mesmos três comportamentos foram verificados
dentro de uma única função. Por isso, a primeira execução terminou com 15 testes
aprovados e a segunda com 13, sem que essa diferença represente necessariamente
menor cobertura dos requisitos.

Também foi observado que a maior autonomia não tornou a tarefa mais rápida.
Durante a segunda execução ocorreram tentativas de edição que falharam e foram
refeitas automaticamente pelo agente. Em contrapartida, a quantidade de
intervenções humanas caiu de cinco para uma.

Neste experimento, aumentar a autonomia reduziu a necessidade de interação
manual, mas também reduziu de forma significativa a sensação de controle. Como
o resultado funcional foi praticamente o mesmo, o principal efeito percebido
do aumento de autonomia esteve na forma como o processo foi conduzido, e não na
arquitetura final da solução.