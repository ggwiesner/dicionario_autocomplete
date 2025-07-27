# src/estruturas/dicionario_hash.py

class DicionarioHash:
    """Implementação de um dicionário com Tabela Hash."""
    def __init__(self):
        self.tabela = {}

    def inserir(self, palavra, definicao=""):
        self.tabela[palavra] = definicao

    def buscar(self, palavra):
        return self.tabela.get(palavra)

    def sugerir(self, prefixo):
        """Ineficiente: varre todas as chaves. Complexidade O(n)."""
        sugestoes = [palavra for palavra in self.tabela if palavra.startswith(prefixo)]
        return sorted(sugestoes)