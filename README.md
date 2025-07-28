# Análise Comparativa: Tabela Hash vs. Árvore AVL em um Dicionário Computacional

Este projeto implementa e analisa o desempenho de duas estruturas de dados fundamentais, Tabela Hash e Árvore AVL, aplicadas a um estudo de caso realístico: um dicionário para correção ortográfica e sugestão de palavras (autocomplete).

O objetivo é comparar de forma teórica e prática (através de experimentos computacionais) qual das duas estruturas é mais efetiva para cada uma das funcionalidades propostas, avaliando critérios como complexidade de tempo, tempo de execução e facilidade de implementação.


## Estudo de Caso: Dicionário e Autocomplete

A aplicação simula duas funcionalidades centrais de um editor de texto moderno:

1.  **Correção Ortográfica (`buscar`):** Verifica se uma palavra digitada existe no dicionário. Esta é uma operação de busca por chave exata.
2.  **Autocomplete (`sugerir`):** Dado um prefixo (e.g., "comp"), sugere uma lista de palavras do dicionário que começam com esse prefixo. Esta é uma operação de busca por faixa ou prefixo.

## Análise Teórica Esperada

| Estrutura de Dados | Correção Ortográfica (Busca Exata) | Autocomplete (Busca por Prefixo) |
| :----------------- | :--------------------------------: | :--------------------------------: |
| **Tabela Hash**    | **O(1)** (caso médio)              | **O(N)** (ineficiente)             |
| **Árvore AVL**     | **O(log n)**                       | **O(log n + k)** (eficiente)¹      |

¹ Onde `n` é o número total de palavras e `k` é o número de palavras encontradas com o prefixo. A busca pelo prefixo inicial é `O(log n)`, e a coleta dos resultados é proporcional a `k`.

A hipótese é que a Tabela Hash será superior para a correção ortográfica, enquanto a Árvore AVL será dramaticamente superior para a funcionalidade de autocomplete.

## Como Executar o Projeto

### Pré-requisitos

-   Python 3.8 ou superior
-   Um arquivo de texto com uma lista de palavras (uma por linha) salvo como `data/palavras.txt`. Você pode encontrar um bom dataset de palavras em português [aqui](https://www.ufrgs.br/cinti/dicionarios-e-corpus-textuais/dicionario-para-corretores-ortograficos/).

### Instalação

1.  Clone o repositório:
    ```bash
    git clone <url-do-seu-repositorio>
    cd <nome-do-repositorio>
    ```

2.  Instale as dependências (para rodar os testes):
    ```bash
    pip install -r requirements.txt
    ```

### Executando os Testes Unitários

Para verificar a corretude das implementações:
```bash
pytest