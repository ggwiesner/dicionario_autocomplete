# experimento_memoria.py
import tracemalloc
import os
import sys
import json
from src.utils.carregador_dados import carregar_palavras
from src.estruturas.dicionario_hash import DicionarioHash
from src.estruturas.dicionario_avl import DicionarioAVL

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

IDIOMAS_PARA_TESTAR = [
    {'nome': 'Portugues', 'arquivo': 'portugues.txt'},
    {'nome': 'Ingles', 'arquivo': 'ingles.txt'},
    {'nome': 'Alemao', 'arquivo': 'alemao.txt'},
]

# NOVO: Define o nome da pasta de resultados
PASTA_RESULTADOS = "resultados"

def medir_memoria_estrutura(estrutura_classe, palavras: list, **kwargs):
    tracemalloc.start()
    estrutura = estrutura_classe(**kwargs)
    for palavra in palavras:
        estrutura.inserir(palavra)
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak

def run_experimento_memoria():
    resultados = []
    print("--- [MEMÓRIA] Iniciando Teste de Consumo de Memória ---")
    for config_idioma in IDIOMAS_PARA_TESTAR:
        caminho_arquivo = os.path.join('data', config_idioma['arquivo'])
        palavras = carregar_palavras(caminho_arquivo)
        if not palavras: continue
        
        num_palavras = len(palavras)
        print(f"\nAnalisando idioma: {config_idioma['nome']} ({num_palavras:,} palavras)")

        mem_hash = medir_memoria_estrutura(DicionarioHash, palavras, tamanho=num_palavras)
        print(f"  Pico de memória (Hash): {mem_hash / 1024**2:.2f} MB")

        mem_avl = medir_memoria_estrutura(DicionarioAVL, palavras)
        print(f"  Pico de memória (AVL):  {mem_avl / 1024**2:.2f} MB")

        resultados.append({
            'idioma': config_idioma['nome'],
            'num_palavras': num_palavras,
            'mem_hash_mb': mem_hash / 1024**2,
            'mem_avl_mb': mem_avl / 1024**2,
        })
    return resultados

if __name__ == "__main__":
    resultados_finais = run_experimento_memoria()
    if resultados_finais:
        # ALTERAÇÃO: Cria a pasta de resultados se ela não existir
        os.makedirs(PASTA_RESULTADOS, exist_ok=True)
        
        # ALTERAÇÃO: Constrói o caminho completo para o arquivo de saída
        caminho_saida = os.path.join(PASTA_RESULTADOS, "resultados_memoria.json")

        with open(caminho_saida, 'w', encoding='utf-8') as f:
            json.dump(resultados_finais, f, indent=4)
            
        # ALTERAÇÃO: Informa o caminho correto ao usuário
        print(f"\nResultados de memória salvos em '{caminho_saida}'")