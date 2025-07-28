# converter_json.py
import json
import os

# --- Configuração ---
# Caminho do arquivo JSON de entrada
caminho_entrada_json = os.path.join('data', 'alemao.json') 

# Nome do arquivo TXT de saída
nome_saida_txt = 'alemao.txt'
caminho_saida_txt = os.path.join('data', nome_saida_txt)
# --------------------

def converter_lista_simples():
    """
    Lê um JSON contendo uma lista de palavras e o converte para um arquivo TXT.
    """
    try:
        with open(caminho_entrada_json, 'r', encoding='utf-8') as f_json:
            # Carrega todo o conteúdo do JSON para uma lista Python
            lista_palavras = json.load(f_json)
        
        # Verifica se o conteúdo é realmente uma lista
        if not isinstance(lista_palavras, list):
            print("Erro: O JSON não contém uma lista no nível raiz.")
            return

        with open(caminho_saida_txt, 'w', encoding='utf-8') as f_txt:
            for palavra in lista_palavras:
                # Garante que estamos lidando com strings e escreve no arquivo
                if isinstance(palavra, str):
                    f_txt.write(f"{palavra}\n")
        
        print(f"Sucesso! {len(lista_palavras)} palavras foram convertidas e salvas em '{caminho_saida_txt}'")

    except FileNotFoundError:
        print(f"Erro: Arquivo de entrada '{caminho_entrada_json}' não encontrado.")
    except json.JSONDecodeError:
        print(f"Erro: O arquivo '{caminho_entrada_json}' não é um JSON válido.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    converter_lista_simples()