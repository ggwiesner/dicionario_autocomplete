# src/estruturas/dicionario_hash.py

class DicionarioHash:
    def __init__(self, tamanho: int):
        if tamanho < 1:
            raise ValueError("O tamanho da tabela hash deve ser pelo menos 1.")
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(self.tamanho)]

    def _hash(self, palavra: str) -> int:
        # Função de hash simples e eficaz para strings
        hash_val = 0
        for char in palavra:
            hash_val = (hash_val * 31 + ord(char)) % self.tamanho
        return hash_val

    def inserir(self, palavra: str):
        """Insere uma palavra na tabela hash."""
        indice = self._hash(palavra)
        # Evita duplicatas na lista de colisões
        if palavra not in self.tabela[indice]:
            self.tabela[indice].append(palavra)

    def buscar(self, palavra: str) -> bool:
        """Verifica se uma palavra existe. (Correção Ortográfica)"""
        indice = self._hash(palavra)
        return palavra in self.tabela[indice]

    def sugerir(self, prefixo: str) -> list[str]:
        """
        Gera sugestões de autocomplete.
        NOTE: Esta operação é INEFICIENTE na tabela hash.
        Requer varrer TODA a estrutura de dados.
        """
        sugestoes = []
        for bucket in self.tabela:
            for palavra in bucket:
                if palavra.startswith(prefixo):
                    sugestoes.append(palavra)
        return sorted(sugestoes) # Ordena para consistência na saída