# Projeto: Dicionário com Autocomplete

Este projeto implementa e compara duas estruturas de dados (Tabela Hash e Árvore AVL) para a criação de um dicionário com funcionalidade de autocomplete.

## Estrutura do Projeto

- `data/`: Contém os arquivos de dados, como listas de palavras.
- `src/`: Contém o código-fonte principal.
  - `estruturas/`: Implementações das estruturas de dados (Tabela Hash e Árvore AVL).
  - `utils/`: Funções utilitárias, como o carregamento de dados.
- `tests/`: Contém os testes unitários para garantir a corretude do código.
- `main.py`: Ponto de entrada principal para interagir com o dicionário via terminal.
- `experimento_comparativo.py`: Script para rodar um teste de performance e comparar as duas estruturas.

## Como Executar

1.  **Executar a aplicação principal (interativa):**
    ```sh
    python main.py
    ```

2.  **Executar o experimento de performance:**
    ```sh
    python experimento_comparativo.py
    ```

3.  **Executar os testes:**
    ```sh
    python -m unittest discover tests
    ```