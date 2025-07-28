# Análise Comparativa: Tabela Hash vs. Árvore AVL em um Dicionário Computacional

Este projeto implementa e analisa o desempenho de duas estruturas de dados fundamentais, a **Tabela Hash** e a **Árvore AVL**, aplicadas a um estudo de caso realístico: um dicionário computacional para correção ortográfica e sugestão de palavras (autocomplete).

O objetivo é comparar de forma prática, através de experimentos computacionais, qual das duas estruturas é mais efetiva para cada uma das funcionalidades propostas, avaliando critérios como tempo de execução e consumo de memória em datasets de larga escala.

## Funcionalidades do Estudo de Caso

A aplicação simula duas funcionalidades centrais de um editor de texto moderno:

1.  **Correção Ortográfica (`buscar`):** Verifica se uma palavra existe no dicionário. Esta é uma tarefa de **busca por chave exata**.
2.  **Autocomplete (`sugerir`):** Dado um prefixo (e.g., "comp"), retorna uma lista de palavras do dicionário que começam com ele. Esta é uma tarefa de **busca por faixa ou prefixo**.

## Estrutura do Projeto

O repositório está organizado da seguinte forma para separar lógica, dados, testes e resultados:

├── data/
│ ├── portugues.txt
│ ├── ingles.txt
│ ├── alemao.txt
│ └── alemao.json
├── src/
│ ├── estruturas/
│ └── utils/
├── tests/
│ ├── test_dicionario_avl.py
│ └── test_dicionario_hash.py
├── resultados/
│ ├── resultados_tempo.json
│ └── resultados_memoria.json
├── graficos/
│ ├── ... (gráficos e tabela em .png)
├── .gitignore
├── requirements.txt
├── main.py
├── experimento_tempo.py
├── experimento_memoria.py
├── gerar_visualizacoes.py
├── converter_json.py
└── README.md

      
## Datasets Utilizados

Os experimentos foram conduzidos com dicionários de três idiomas diferentes para analisar a performance em diversas escalas e com diferentes características linguísticas:
- **Português:** `portugues.txt` (~245 mil palavras)
- **Inglês:** `ingles.txt` (~370 mil palavras)
- **Alemão:** `alemao.txt` (~1.6 milhão de palavras)

### Nota sobre o Dicionário de Alemão
A fonte de dados para o dicionário de alemão foi obtida em formato JSON (`data/alemao.json`). Para padronizar os dados de entrada para os experimentos, foi necessário criar um script utilitário, `converter_json.py`, localizado na raiz do projeto.

Este script lê a lista de palavras do arquivo JSON e a converte para um arquivo de texto simples (`data/alemao.txt`), com uma palavra por linha, que é o formato esperado pela aplicação. Para gerar o arquivo `alemao.txt`, basta executar:
```bash
python converter_json.py

    
Como Executar o Projeto
1. Pré-requisitos

    Python 3.8 ou superior

    Git

2. Instalação e Configuração

É altamente recomendado o uso de um ambiente virtual.
Generated bash

      
# 1. Clone o repositório e entre no diretório
git clone <url-do-seu-repositorio>
cd <nome-do-repositorio>

# 2. Crie e ative um ambiente virtual
python3 -m venv .venv
source .venv/bin/activate  # (Linux/macOS)

# 3. Instale as dependências
pip install -r requirements.txt

    
3. Executando os Scripts

Com o ambiente virtual ativo, o fluxo de trabalho recomendado é:
a) Preparação dos Dados (se necessário)

Se o arquivo data/alemao.txt não existir, gere-o a partir do JSON:
Generated bash

      
python converter_json.py

    
b) Rodando os Experimentos de Performance

Execute ambos os scripts para gerar os arquivos de resultados na pasta resultados/.
Generated bash

      
# Gera resultados/resultados_tempo.json
python experimento_tempo.py

# Gera resultados/resultados_memoria.json
python experimento_memoria.py

    
c) Gerando os Gráficos e a Tabela Final

Após gerar os dados, execute este script para criar as visualizações na pasta graficos/.
Generated bash

      
python gerar_visualizacoes.py

    
d) Outros Scripts

    Demonstração Interativa: python main.py

    Testes Unitários: pytest

O que os Resultados Demonstram

Ao analisar os gráficos e tabelas gerados, as seguintes conclusões se tornam evidentes:

    Tabela Hash:

        Força: Extremamente rápida para buscas exatas (correção ortográfica), com tempo de execução O(1) que não se degrada com o aumento do dicionário.

        Fraqueza: Totalmente ineficiente para sugestões de autocomplete (busca por prefixo), tornando a funcionalidade inviável na prática.

    Árvore AVL:

        Força: Altamente eficiente para sugestões de autocomplete, realizando milhares de operações em uma fração de segundo. É a única escolha viável para essa tarefa.

        Fraqueza: É visivelmente mais lenta que a Tabela Hash para construção e para buscas exatas, embora ainda muito rápida para fins práticos.

    Memória: A Árvore AVL tende a consumir um pouco mais de memória devido à sobrecarga de informações (ponteiros de filho, altura) em cada nó.

Este projeto demonstra na prática o clássico trade-off da engenharia de software: não existe uma "solução perfeita", mas sim a ferramenta certa para o trabalho certo.