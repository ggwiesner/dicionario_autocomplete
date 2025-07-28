# main.py
from src.utils.carregador_dados import carregar_palavras
from src.estruturas.dicionario_hash import DicionarioHash
from src.estruturas.dicionario_avl import DicionarioAVL
import sys

# Definir o limite de recursão também no modo interativo
sys.setrecursionlimit(300000)

def interativo():
    palavras = carregar_palavras('data/palavras.txt')
    if not palavras:
        return

    num_palavras = len(palavras)
    escolha = input("Escolha a estrutura de dados (hash/avl): ").lower()

    if escolha == 'avl':
        print("Construindo Dicionário AVL...")
        dicionario = DicionarioAVL()
    else:
        print("Construindo Dicionário Hash...")
        # ALTERAÇÃO AQUI: Passar o tamanho correto para a tabela hash.
        dicionario = DicionarioHash(tamanho=num_palavras)

    # O resto do arquivo permanece igual...
    for palavra in palavras:
        dicionario.inserir(palavra)
    
    print("Dicionário pronto!\n")
    # ...