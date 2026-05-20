# Algoritmos de Backtracking: N-Rainhas e Soma dos Subconjuntos

**Repositório:** [github.com/gabriellrmartins/backtracking-algorithms](https://github.com/gabriellrmartins/backtracking-algorithms)  
**Aluno:** Gabriel Levasseur Rocha Martins  
**Instituição:** PUCRS  

Este repositório contém a implementação em Python das soluções utilizando a estratégia de Backtracking para os problemas das N-Rainhas e da Soma dos Subconjuntos, juntamente com a análise da classe de complexidade (Big O) e medições de desempenho.

## 1. Análise de Complexidade

A estratégia de Backtracking realiza uma busca em profundidade no espaço de estados do problema, podando (interrompendo) caminhos que comprovadamente não levam a uma solução válida.

### A. Problema das N-Rainhas (N-Queens)
* **Complexidade de Tempo:** $\mathcal{O}(N!)$
  * No pior caso, o algoritmo tenta alocar rainhas em todas as permutações possíveis. A poda de linhas, colunas e diagonais melhora drasticamente o desempenho prático comparado à força bruta pura de $\mathcal{O}(N^N)$, mas o limite superior assintótico continua sendo fatorial. A busca pela primeira solução compartilha a mesma classe no pior caso, embora termine muito mais cedo no caso médio.
* **Complexidade de Espaço:** $\mathcal{O}(N)$
  * O espaço em memória é dominado pela profundidade da pilha de recursão, que atinge o limite máximo de $N$ chamadas, somado ao array unidimensional de tamanho $N$ que armazena a posição das rainhas.

### B. Problema da Soma dos Subconjuntos (Subset Sum)
* **Complexidade de Tempo:** $\mathcal{O}(2^N)$
  * A árvore de estado possui ramificação binária, decidindo em cada nível se o elemento atual será incluído ou não no subconjunto. A ordenação prévia do conjunto adiciona um custo inicial de $\mathcal{O}(N \log N)$, mas o termo exponencial é dominante no limite superior do pior caso.
* **Complexidade de Espaço:** $\mathcal{O}(N)$
  * O espaço auxiliar necessário corresponde à profundidade máxima da árvore de recursão, que é de $N$ níveis, além do espaço alocado para rastrear a combinação atual dos elementos.

---

## 2. Resultados das Medições

*Configurações da Execução: Implementação em Python 3.x utilizando `time.perf_counter` para alta precisão na aferição do tempo.*

### Tabela 1: N-Rainhas
| Tamanho do Tabuleiro (N) | Objetivo | Soluções Encontradas | Iterações (Nós Visitados) | Tempo de Execução |
| :--- | :--- | :--- | :--- | :--- |
| **8** | Primeira Solução | 1 | 114 | 0.18 ms |
| **8** | Todas as Soluções | 92 | 2.057 | 3.28 ms |
| **12** | Primeira Solução | 1 | 262 | 0.74 ms |
| **12** | Todas as Soluções | 14.200 | 856.189 | 2.426,34 ms (2.43 s) |

### Tabela 2: Soma dos Subconjuntos
*Nota: Para $N=25$, foi gerado um array com números inteiros de 1 a 100 com uma semente fixa, e o alvo foi definido como um terço da soma total do array.*

| Tamanho do Conjunto (N) | Objetivo | Soluções Encontradas | Iterações (Nós Visitados) | Tempo de Execução |
| :--- | :--- | :--- | :--- | :--- |
| **15** | Primeira Solução | 1 | 26 | 0.01 ms |
| **15** | Todas as Soluções | 70 | 1.833 | 0.27 ms |
| **25** | Primeira Solução | 1 | 92 | 0.01 ms |
| **25** | Todas as Soluções | 40.613 | 3.105.349 | 416.77 ms |

## 3. Como Executar
Basta rodar o arquivo Python principal para que o algoritmo execute todas as permutações e gere o benchmark diretamente no terminal:
```bash
python3 solucoes_backtracking.py
```
