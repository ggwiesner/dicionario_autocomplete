# src/estruturas/dicionario_avl.py

class No:
    def __init__(self, chave, valor=""):
        self.chave = chave
        self.valor = valor
        self.esquerda = None
        self.direita = None
        self.altura = 1

class DicionarioAVL:
    """Implementação de um dicionário com Árvore AVL."""
    def __init__(self):
        self.raiz = None

    def inserir(self, chave, valor=""):
        self.raiz = self._inserir_recursivo(self.raiz, chave, valor)

    def _inserir_recursivo(self, no_atual, chave, valor):
        if not no_atual:
            return No(chave, valor)
        elif chave < no_atual.chave:
            no_atual.esquerda = self._inserir_recursivo(no_atual.esquerda, chave, valor)
        else:
            no_atual.direita = self._inserir_recursivo(no_atual.direita, chave, valor)

        no_atual.altura = 1 + max(self._get_altura(no_atual.esquerda), self._get_altura(no_atual.direita))
        balance = self._get_balanceamento(no_atual)

        if balance > 1 and chave < no_atual.esquerda.chave:
            return self._rotacao_direita(no_atual)
        if balance < -1 and chave > no_atual.direita.chave:
            return self._rotacao_esquerda(no_atual)
        if balance > 1 and chave > no_atual.esquerda.chave:
            no_atual.esquerda = self._rotacao_esquerda(no_atual.esquerda)
            return self._rotacao_direita(no_atual)
        if balance < -1 and chave < no_atual.direita.chave:
            no_atual.direita = self._rotacao_direita(no_atual.direita)
            return self._rotacao_esquerda(no_atual)
        return no_atual

    def buscar(self, chave):
        return self._buscar_recursivo(self.raiz, chave)

    def _buscar_recursivo(self, no_atual, chave):
        if not no_atual or no_atual.chave == chave:
            return no_atual.valor if no_atual else None
        if chave < no_atual.chave:
            return self._buscar_recursivo(no_atual.esquerda, chave)
        return self._buscar_recursivo(no_atual.direita, chave)

    def sugerir(self, prefixo):
        sugestoes = []
        no_inicial = self._encontrar_no_inicial(self.raiz, prefixo)
        self._coletar_sugestoes(no_inicial, prefixo, sugestoes)
        return sorted(sugestoes)

    def _encontrar_no_inicial(self, no, prefixo):
        if not no:
            return None
        if no.chave.startswith(prefixo):
            return no
        if prefixo < no.chave:
            return self._encontrar_no_inicial(no.esquerda, prefixo)
        return self._encontrar_no_inicial(no.direita, prefixo)

    def _coletar_sugestoes(self, no, prefixo, sugestoes):
        if not no:
            return
        if no.chave.startswith(prefixo):
            sugestoes.append(no.chave)
            self._coletar_sugestoes(no.esquerda, prefixo, sugestoes)
            self._coletar_sugestoes(no.direita, prefixo, sugestoes)

    def _get_altura(self, no):
        return no.altura if no else 0

    def _get_balanceamento(self, no):
        return self._get_altura(no.esquerda) - self._get_altura(no.direita) if no else 0

    def _rotacao_esquerda(self, z):
        y = z.direita
        T2 = y.esquerda
        y.esquerda = z
        z.direita = T2
        z.altura = 1 + max(self._get_altura(z.esquerda), self._get_altura(z.direita))
        y.altura = 1 + max(self._get_altura(y.esquerda), self._get_altura(y.direita))
        return y

    def _rotacao_direita(self, z):
        y = z.esquerda
        T3 = y.direita
        y.direita = z
        z.esquerda = T3
        z.altura = 1 + max(self._get_altura(z.esquerda), self._get_altura(z.direita))
        y.altura = 1 + max(self._get_altura(y.esquerda), self._get_altura(y.direita))
        return y