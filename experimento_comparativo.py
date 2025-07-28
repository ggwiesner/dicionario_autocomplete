# experimento_comparativo.py
import time
import random
import sys
from src.utils.carregador_dados import carregar_palavras
from src.estruturas.dicionario_hash import DicionarioHash
from src.estruturas.dicionario_avl import DicionarioAVL

# Aumenta o limite de recursão da AVL para lidar com o grande dataset
sys.setrecursionlimit(300000)

# --- Configurações do Experimento ---
CAMINHO_ARQUIVO = 'data/palavras.txt'
NUM_BUSCAS = 10000  # Aumentado para ter uma média mais estável
NUM_SUGESTOES = 2000 # Aumentado para a AVL
PREFIXO_TAMANHO = 4  # Um prefixo um pouco maior para ser mais seletivo

# --- Execução do Experimento ---
def run():
    palavras = carregar_palavras(CAMINHO_ARQUIVO)
    if not palavras:
        return
    
    num_palavras_total = len(palavras)
    print(f"\n--- INICIANDO EXPERIMENTO COM {num_palavras_total} PALAVRAS ---")

    # --- 1. Tempo de Construção ---
    print("\n[1] MEDINDO TEMPO DE CONSTRUÇÃO (INSERÇÃO)...")
    
    # Tabela Hash
    start_time = time.perf_counter()
    # Passamos o tamanho exato para ter um fator de carga ideal
    dicionario_hash = DicionarioHash(tamanho=num_palavras_total) 
    for palavra in palavras:
        dicionario_hash.inserir(palavra)
    tempo_hash_build = time.perf_counter() - start_time
    print(f"  Tabela Hash: {tempo_hash_build:.6f} segundos")

    # Árvore AVL
    start_time = time.perf_counter()
    dicionario_avl = DicionarioAVL()
    for palavra in palavras:
        dicionario_avl.inserir(palavra)
    tempo_avl_build = time.perf_counter() - start_time
    print(f"  Árvore AVL:  {tempo_avl_build:.6f} segundos")

    # --- 2. Tempo de Busca (Correção Ortográfica) ---
    print(f"\n[2] MEDINDO TEMPO DE BUSCA PARA {NUM_BUSCAS} PALAVRAS...")
    amostra_busca = random.sample(palavras, NUM_BUSCAS)

    # Tabela Hash
    start_time = time.perf_counter()
    for palavra in amostra_busca:
        dicionario_hash.buscar(palavra)
    tempo_hash_search = time.perf_counter() - start_time
    print(f"  Tabela Hash: {tempo_hash_search:.6f} segundos")

    # Árvore AVL
    start_time = time.perf_counter()
    for palavra in amostra_busca:
        dicionario_avl.buscar(palavra)
    tempo_avl_search = time.perf_counter() - start_time
    print(f"  Árvore AVL:  {tempo_avl_search:.6f} segundos")

    # --- 3. Tempo de Sugestão (Autocomplete) ---
    print(f"\n[3] MEDINDO TEMPO DE SUGESTÃO PARA PREFIXOS...")
    amostra_prefixos = [p[:PREFIXO_TAMANHO] for p in random.sample(palavras, NUM_SUGESTOES)]
    
    # Árvore AVL (executa com o número normal de sugestões)
    print(f"  Testando Árvore AVL com {NUM_SUGESTOES} prefixos...")
    start_time = time.perf_counter()
    for prefixo in amostra_prefixos:
        dicionario_avl.sugerir(prefixo)
    tempo_avl_suggest = time.perf_counter() - start_time
    print(f"  -> Árvore AVL: {tempo_avl_suggest:.6f} segundos")

    # Tabela Hash (executa com um número BEM MENOR de sugestões para não travar)
    NUM_SUGESTOES_HASH = 5 # Apenas 5 para demonstrar a lentidão
    amostra_prefixos_hash = amostra_prefixos[:NUM_SUGESTOES_HASH]
    print(f"  Testando Tabela Hash com {NUM_SUGESTOES_HASH} prefixos (operação lenta)...")
    start_time = time.perf_counter()
    for prefixo in amostra_prefixos_hash:
        dicionario_hash.sugerir(prefixo)
    tempo_hash_suggest_parcial = time.perf_counter() - start_time
    
    # Extrapolação para estimar o tempo total
    tempo_estimado_hash_total = (tempo_hash_suggest_parcial / NUM_SUGESTOES_HASH) * NUM_SUGESTOES
    print(f"  -> Tabela Hash: {tempo_hash_suggest_parcial:.6f} segundos para {NUM_SUGESTOES_HASH} prefixos.")
    print(f"     (Tempo estimado para {NUM_SUGESTOES} prefixos: ~{tempo_estimado_hash_total:.2f} segundos)")


    print("\n--- FIM DO EXPERIMENTO ---")

if __name__ == "__main__":
    run()