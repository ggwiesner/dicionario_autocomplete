# main.py
import sys
import os
import time

# Adiciona o caminho raiz para garantir que as importações de 'src' funcionem
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from src.utils.carregador_dados import carregar_palavras
from src.estruturas.dicionario_hash import DicionarioHash
from src.estruturas.dicionario_avl import DicionarioAVL

# Aumenta o limite de recursão para o maior dicionário (Alemão)
sys.setrecursionlimit(2000000)

# Dicionários disponíveis para o usuário
DICIONARIOS = {
    '1': {'nome': 'Portugues', 'arquivo': 'portugues.txt'},
    '2': {'nome': 'Ingles', 'arquivo': 'ingles.txt'},
    '3': {'nome': 'Alemao', 'arquivo': 'alemao.txt'},
}

def interativo():
    """
    Função principal que guia o usuário através da seleção de dicionário
    e estrutura de dados, e então entra no modo interativo.
    """
    # Passo 1: Seleção do Idioma
    print("Bem-vindo ao Dicionário Computacional Interativo!")
    print("Escolha o dicionário para carregar:")
    for key, val in DICIONARIOS.items():
        print(f"  {key}: {val['nome']} ({val['arquivo']})")
    
    escolha_idioma = ''
    while escolha_idioma not in DICIONARIOS:
        escolha_idioma = input("Digite o número do idioma desejado: ")
        if escolha_idioma not in DICIONARIOS:
            print("Opção inválida. Por favor, tente novamente.")

    config_selecionada = DICIONARIOS[escolha_idioma]
    caminho_arquivo = os.path.join('data', config_selecionada['arquivo'])
    print(f"\nCarregando dicionário de {config_selecionada['nome']}... Por favor, aguarde.")
    palavras = carregar_palavras(caminho_arquivo)
    
    if not palavras:
        print("Erro ao carregar o arquivo de dados. Finalizando o programa.")
        return

    num_palavras = len(palavras)
    
    # Passo 2: Seleção da Estrutura de Dados
    escolha_estrutura = ''
    while escolha_estrutura not in ['hash', 'avl']:
        escolha_estrutura = input("Escolha a estrutura de dados a ser usada (hash/avl): ").lower()
        if escolha_estrutura not in ['hash', 'avl']:
            print("Opção inválida. Por favor, digite 'hash' ou 'avl'.")

    # Passo 3: Construção da Estrutura
    if escolha_estrutura == 'avl':
        print(f"Construindo Dicionário AVL com {num_palavras:,} palavras... (Pode levar alguns segundos/minutos)")
        dicionario = DicionarioAVL()
    else: # 'hash'
        print(f"Construindo Dicionário Hash com {num_palavras:,} palavras...")
        dicionario = DicionarioHash(tamanho=num_palavras)

    start_time = time.perf_counter()
    for palavra in palavras:
        dicionario.inserir(palavra)
    build_time = time.perf_counter() - start_time
    print(f"Dicionário construído com sucesso em {build_time:.2f} segundos.\n")

    # Passo 4: Loop Interativo
    print("--- Dicionário Interativo ---")
    print("Digite uma palavra para verificar a ortografia e obter sugestões de autocomplete.")
    # ALTERAÇÃO: Instrução de saída atualizada para usar um número.
    print("Digite '0' para sair do programa.")
    print("-" * 30)

    while True:
        # ALTERAÇÃO: Prompt de entrada mais claro.
        entrada = input("Digite uma palavra ou comando (0 para sair): ").lower().strip()
        
        # ALTERAÇÃO: A condição de saída agora é '0' para permitir a busca pela palavra "sair".
        if entrada == '0':
            print("Saindo do programa. Até mais!")
            break
        
        if not entrada:
            continue

        # Medir e reportar performance da busca
        start_search = time.perf_counter()
        existe = dicionario.buscar(entrada)
        end_search = time.perf_counter()
        
        if existe:
            print(f"✅ A palavra '{entrada}' ESTÁ no dicionário.")
        else:
            print(f"❌ A palavra '{entrada}' NÃO está no dicionário.")
        print(f"   (Busca levou {(end_search - start_search) * 1000:.4f} ms)")
        
        # Medir e reportar performance da sugestão
        start_suggest = time.perf_counter()
        sugestoes = dicionario.sugerir(entrada)
        end_suggest = time.perf_counter()

        if sugestoes:
            print(f"  Sugestões para '{entrada}': {sugestoes[:10]}")
        else:
            print(f"  Nenhuma sugestão encontrada para o prefixo '{entrada}'.")
        print(f"   (Sugestão levou {(end_suggest - start_suggest) * 1000:.4f} ms)")
        print("-" * 30)

if __name__ == "__main__":
    interativo()