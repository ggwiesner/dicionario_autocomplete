# src/utils/carregador_dados.py
def carregar_palavras(caminho_arquivo):
    """Lê um arquivo de texto e retorna uma lista de palavras."""
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            palavras = [linha.strip().lower() for linha in f if linha.strip()]
        return palavras
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado em '{caminho_arquivo}'")
        return []