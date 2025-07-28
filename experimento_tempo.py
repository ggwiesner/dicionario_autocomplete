# experimento_tempo.py
import time
import random
import sys
import os
import json
from src.utils.carregador_dados import carregar_palavras
from src.estruturas.dicionario_hash import DicionarioHash
from src.estruturas.dicionario_avl import DicionarioAVL

sys.setrecursionlimit(2000000)
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

IDIOMAS_PARA_TESTAR = [
    {'nome': 'Portugues', 'arquivo': 'portugues.txt'},
    {'nome': 'Ingles', 'arquivo': 'ingles.txt'},
    {'nome': 'Alemao', 'arquivo': 'alemao.txt'},
]

# Parâmetros para os benchmarks de tempo
NUM_BUSCAS = 10000
PREFIXO_TAMANHO = 4

# NOVOS PARÂMETROS para a medição de sugestão
NUM_SUGESTOES_AVL_GRANDE = 1000
NUM_SUGESTOES_HASH_PEQUENO = 10

PASTA_RESULTADOS = "resultados"

def run_benchmark_tempo(config_idioma):
    caminho_arquivo = os.path.join('data', config_idioma['arquivo'])
    palavras = carregar_palavras(caminho_arquivo)
    if not palavras: return None
    
    num_palavras = len(palavras)
    print(f"\n--- [TEMPO] Testando: {config_idioma['nome']} ({num_palavras:,} palavras) ---")
    resultados = {'idioma': config_idioma['nome'], 'num_palavras': num_palavras}

    # --- 1. Construção ---
    start_time = time.perf_counter()
    dicionario_hash = DicionarioHash(tamanho=num_palavras)
    for p in palavras: dicionario_hash.inserir(p)
    resultados['build_hash_time'] = time.perf_counter() - start_time
    
    start_time = time.perf_counter()
    dicionario_avl = DicionarioAVL()
    for p in palavras: dicionario_avl.inserir(p)
    resultados['build_avl_time'] = time.perf_counter() - start_time
    print(f"  Construção - Hash: {resultados['build_hash_time']:.4f}s | AVL: {resultados['build_avl_time']:.4f}s")

    # --- 2. Busca ---
    amostra_busca = random.sample(palavras, NUM_BUSCAS)
    start_time = time.perf_counter()
    for p in amostra_busca: dicionario_hash.buscar(p)
    resultados['search_hash_time'] = time.perf_counter() - start_time

    start_time = time.perf_counter()
    for p in amostra_busca: dicionario_avl.buscar(p)
    resultados['search_avl_time'] = time.perf_counter() - start_time
    print(f"  Busca ({NUM_BUSCAS}x) - Hash: {resultados['search_hash_time']:.4f}s | AVL: {resultados['search_avl_time']:.4f}s")
    
    # --- 3. Sugestão (MEDIÇÕES GRANULARES) ---
    print("[3] Medindo tempo de sugestão em diferentes escalas...")
    # Prepara uma amostra de prefixos grande o suficiente para o maior teste
    amostra_prefixos = [p[:PREFIXO_TAMANHO] for p in random.sample(palavras, NUM_SUGESTOES_AVL_GRANDE)]
    
    # Medição Individual (1x)
    prefixo_individual = amostra_prefixos[0]
    start_time = time.perf_counter()
    dicionario_hash.sugerir(prefixo_individual)
    resultados['suggest_1x_hash_time'] = time.perf_counter() - start_time

    start_time = time.perf_counter()
    dicionario_avl.sugerir(prefixo_individual)
    resultados['suggest_1x_avl_time'] = time.perf_counter() - start_time
    print(f"  Sugestão (1x) - Hash: {resultados['suggest_1x_hash_time']:.6f}s | AVL: {resultados['suggest_1x_avl_time']:.6f}s")

    # Medição Pequena Escala (10x Hash)
    amostra_prefixos_hash = amostra_prefixos[:NUM_SUGESTOES_HASH_PEQUENO]
    start_time = time.perf_counter()
    for prefixo in amostra_prefixos_hash:
        dicionario_hash.sugerir(prefixo)
    resultados['suggest_10x_hash_time'] = time.perf_counter() - start_time
    print(f"  Sugestão ({NUM_SUGESTOES_HASH_PEQUENO}x) - Hash: {resultados['suggest_10x_hash_time']:.4f}s")

    # Medição Grande Escala (1000x AVL)
    start_time = time.perf_counter()
    for prefixo in amostra_prefixos: # Usa a amostra completa de 1000
        dicionario_avl.sugerir(prefixo)
    resultados['suggest_1000x_avl_time'] = time.perf_counter() - start_time
    print(f"  Sugestão ({NUM_SUGESTOES_AVL_GRANDE}x) - AVL: {resultados['suggest_1000x_avl_time']:.4f}s")
    
    return resultados

def print_summary_table_tempo(resultados_finais):
    print("\n\n--- TABELA DE RESULTADOS DE TEMPO ---\n")
    header = (
        "| Idioma      | # Palavras | Build Hash (s) | Build AVL (s) | Search Hash (s) | Search AVL (s) | "
        "Suggest Hash (1x) | Suggest AVL (1x) | Suggest Hash (10x) | Suggest AVL (1000x) |"
    )
    separator = "| :---------- | ---------: | --------------: | -------------: | ---------------: | --------------: | -------------------: | ------------------: | --------------------: | ---------------------: |"
    print(header)
    print(separator)
    for res in resultados_finais:
        num_fmt = f"{res['num_palavras']:,}"
        print(
            f"| {res['idioma']:<11} | {num_fmt:>10} | {res['build_hash_time']:>14.4f} | {res['build_avl_time']:>13.4f} | "
            f"{res['search_hash_time']:>15.4f} | {res['search_avl_time']:>14.4f} | "
            f"{res['suggest_1x_hash_time']:>19.6f} | {res['suggest_1x_avl_time']:>18.6f} | "
            f"{res['suggest_10x_hash_time']:>20.4f} | {res['suggest_1000x_avl_time']:>21.4f} |"
        )

if __name__ == "__main__":
    resultados_finais = []
    for config in IDIOMAS_PARA_TESTAR:
        res = run_benchmark_tempo(config)
        if res: resultados_finais.append(res)
    
    if resultados_finais:
        os.makedirs(PASTA_RESULTADOS, exist_ok=True)
        caminho_saida = os.path.join(PASTA_RESULTADOS, "resultados_tempo.json")
        with open(caminho_saida, 'w', encoding='utf-8') as f:
            json.dump(resultados_finais, f, indent=4)
        print(f"\nResultados de tempo salvos em '{caminho_saida}'")
        print_summary_table_tempo(resultados_finais)