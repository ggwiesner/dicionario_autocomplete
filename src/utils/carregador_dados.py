# src/utils/carregador_dados.py
import os

def carregar_palavras(caminho_arquivo: str) -> list[str]:
    """
    Lê um arquivo de texto e retorna uma lista de palavras.
    Normaliza as palavras para minúsculas e remove espaços em branco.
    """
    if not os.path.exists(caminho_arquivo):
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return []
        
    print(f"Carregando palavras de '{caminho_arquivo}'...")
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        palavras = [linha.strip().lower() for linha in f]
    print(f"{len(palavras)} palavras carregadas.")
    return palavras