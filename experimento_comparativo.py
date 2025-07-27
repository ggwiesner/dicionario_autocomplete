# experimento_comparativo.py
import time
import random
import string
from src.estruturas.dicionario_hash import DicionarioHash
from src.estruturas.dicionario_avl import DicionarioAVL

def gerar_palavras(n):
    """Gera uma lista de n palavras aleatórias."""
    palavras = []
    for _ in range(n):
        chave = ''.join(random.choices(string.ascii_lowercase, k=random.randint(4, 12)))
        palavras.append(chave)
    return list(set(palavras))

def rodar_experimento():
    num_palavras = 20000
    palavras = gerar_palavras(num_palavras)
    prefixos_teste = ["comp", "data", "struct", "algo", "py", "a", "b"]
    
    print(f"--- Iniciando Experimento com {num_palavras} palavras ---")

    # Tabela Hash
    hash_table = DicionarioHash()
    inicio = time.perf_counter()
    for p in palavras: hash_table.inserir(p)
    tempo_insercao_hash = time.perf_counter() - inicio

    inicio = time.perf_counter()
    for p in palavras: hash_table.buscar(p)
    tempo_busca_hash = time.perf_counter() - inicio

    inicio = time.perf_counter()
    for pre in prefixos_teste: hash_table.sugerir(pre)
    tempo_sugestao_hash = time.perf_counter() - inicio

    # Árvore AVL
    avl_tree = DicionarioAVL()
    inicio = time.perf_counter()
    for p in palavras: avl_tree.inserir(p)
    tempo_insercao_avl = time.perf_counter() - inicio

    inicio = time.perf_counter()
    for p in palavras: avl_tree.buscar(p)
    tempo_busca_avl = time.perf_counter() - inicio

    inicio = time.perf_counter()
    for pre in prefixos_teste: avl_tree.sugerir(pre)
    tempo_sugestao_avl = time.perf_counter() - inicio
    
    print("\n--- RESULTADOS DO EXPERIMENTO (em segundos) ---\n")
    print(f"{'Operação':<18} | {'Tabela Hash':<15} | {'Árvore AVL'}")
    print(f"-"*50)
    print(f"{'Inserção em Massa':<18} | {tempo_insercao_hash:<15.6f} | {tempo_insercao_avl:.6f}")
    print(f"{'Busca em Massa':<18} | {tempo_busca_hash:<15.6f} | {tempo_busca_avl:.6f}")
    print(f"{'Autocomplete Geral':<18} | {tempo_sugestao_hash:<15.6f} | {tempo_sugestao_avl:.6f}")

if __name__ == "__main__":
    rodar_experimento()