# trabalho-ia-bayesian

**Aluno/a:** [Camila dos Santos Soares]  
**Disciplina:** Inteligência Artificial (Turma ABI01)  
**Instituição:** Universidade Federal do Amazonas (UFAM) - IComp  
**Professor:** Edjard Mota  

---

## Descrição do Projeto
Este repositório contém a resolução da atividade prática sobre **Redes Bayesianas** aplicada a um sistema de diagnóstico para um farol de bicicleta movido a dínamo.

---

## Resolução da 1ª Questão

### (a) Desenho da Rede Bayesiana de Causalidade
As variáveis do sistema são:
- **Str**: Condição da rua (`dry`, `wet`, `snow_covered`)
- **Flw**: Volante do dínamo desgastado (`t`/`f`)
- **R**: Dínamo deslizante (`t`/`f`)
- **V**: Dínamo mostra a tensão/voltagem (`t`/`f`)
- **B**: Lâmpada ok (`t`/`f`)
- **K**: Cabo ok (`t`/`f`)
- **Li**: Luz ligada (`t`/`f`)

**Estrutura de Arestas (Causalidade):**
- `Str` $\rightarrow$ `R`
- `Flw` $\rightarrow$ `R`
- `R` $\rightarrow$ `V`
- `V` $\rightarrow$ `Li`
- `B` $\rightarrow$ `Li`
- `K` $\rightarrow$ `Li`

---

### (b) e (c) CPTs e Valores Plausíveis
As Tabelas de Probabilidade Condicional (CPTs) modelam as dependências estipuladas no enunciado, respeitando as independências condicionais dadas:
- $P(Str)$ com distribuição para `dry`, `wet` e `snow_covered`.
- $P(R \vert{} Str, Flw)$ modela a probabilidade de deslize consoante o estado da rua e o desgaste do volante.
- $P(V \vert{} R)$ reflete a geração de tensão dependente do deslize (independente de `Str` e `Flw`).
- $P(Li \vert{} V, B, K)$ modela o funcionamento final da luz (independente de `R` dado `V`).

---

### (d) Justificativa da ausência da aresta `(Str, Li)`
A rede bayesiana reflete as relações de causalidade direta. A condição da rua (`Str`) afeta diretamente apenas o deslize do dínamo (`R`), o qual por sua vez afeta a voltagem (`V`), que influencia o estado da luz (`Li`). O caminho entre `Str` e `Li` é estritamente indireto (`Str` $\rightarrow$ `R` $\rightarrow$ `V` $\rightarrow$ `Li`), tornando desnecessária e incorreta a inclusão de uma aresta direta entre `Str` e `Li`.

---

### (e) Cálculo de $P(V \mid Str = \text{snow\_covered})$
Utilizando a regra da probabilidade total e marginalizando em relação à variável intermédia `R`:
$$P(V \mid Str = \text{snow\_covered}) = \sum_{R} P(V \mid R) \cdot P(R \mid Str = \text{snow\_covered}, Flw)$$

O cálculo computacional exato pode ser executado através do script Python disponibilizado neste repositório (`rede_bayesiana.py`).
