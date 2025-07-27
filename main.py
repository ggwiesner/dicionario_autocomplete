# main.py
import time
from src.estruturas.dicionario_hash import DicionarioHash
from src.estruturas.dicionario_avl import DicionarioAVL
from src.utils.carregador_dados import carregar_palavras

def menu():
    print("\n--- Dicionário Interativo ---")
    implementacao = input("Escolha a implementação ('hash' ou 'avl'): ").lower()

    if implementacao == 'hash':
        dicionario = DicionarioHash()
    elif implementacao == 'avl':
        dicionario = DicionarioAVL()
    else:
        print("Opção inválida. Saindo.")
        return

    palavras = carregar_palavras('data/palavras.txt')
    if not palavras:
        return
        
    for p in palavras:
        dicionario.inserir(p)
    print(f"{len(palavras)} palavras carregadas na implementação '{implementacao}'.")

    while True:
        print("\n[1] Buscar uma palavra")
        print("[2] Obter sugestões (autocomplete)")
        print("[3] Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            palavra = input("Digite a palavra para buscar: ")
            resultado = dicionario.buscar(palavra)
            if resultado is not None:
                print(f"Palavra '{palavra}' encontrada.")
            else:
                print(f"Palavra '{palavra}' não encontrada.")
        
        elif opcao == '2':
            prefixo = input("Digite um prefixo: ")
            inicio = time.perf_counter()
            sugestoes = dicionario.sugerir(prefixo)
            fim = time.perf_counter()
            print(f"\nSugestões para '{prefixo}': {sugestoes}")
            print(f"Tempo da busca: {(fim - inicio) * 1000:.4f} ms")

        elif opcao == '3':
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()