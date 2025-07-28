# src/estruturas/dicionario_avl.py
import sys

sys.setrecursionlimit(2000000)

class NodeAVL:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class DicionarioAVL:
    def __init__(self):
        self.root = None

    def inserir(self, palavra: str):
        self.root = self._inserir_recursivo(self.root, palavra)
        
    def buscar(self, palavra: str) -> bool:
        return self._buscar_recursivo(self.root, palavra) is not None

    def sugerir(self, prefixo: str) -> list[str]:
        """Gera sugestões de forma eficiente usando a ordem da árvore."""
        sugestoes = []
        self._sugerir_recursivo(self.root, prefixo, sugestoes)
        return sugestoes


    def _getHeight(self, node):
        return node.height if node else 0

    def _getBalance(self, node):
        return self._getHeight(node.left) - self._getHeight(node.right) if node else 0

    def _rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self._getHeight(z.left), self._getHeight(z.right))
        y.height = 1 + max(self._getHeight(y.left), self._getHeight(y.right))
        return y

    def _leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._getHeight(z.left), self._getHeight(z.right))
        y.height = 1 + max(self._getHeight(y.left), self._getHeight(y.right))
        return y

    # --- Métodos Recursivos da Aplicação ---
    def _inserir_recursivo(self, root, key):
        if not root:
            return NodeAVL(key)
        if key < root.key:
            root.left = self._inserir_recursivo(root.left, key)
        elif key > root.key:
            root.right = self._inserir_recursivo(root.right, key)
        else: # Chave já existe
            return root

        root.height = 1 + max(self._getHeight(root.left), self._getHeight(root.right))
        balance = self._getBalance(root)

        if balance > 1 and key < root.left.key:
            return self._rightRotate(root)
        if balance < -1 and key > root.right.key:
            return self._leftRotate(root)
        if balance > 1 and key > root.left.key:
            root.left = self._leftRotate(root.left)
            return self._rightRotate(root)
        if balance < -1 and key < root.right.key:
            root.right = self._rightRotate(root.right)
            return self._leftRotate(root)
        
        return root

    def _buscar_recursivo(self, root, key):
        if not root or root.key == key:
            return root
        if key < root.key:
            return self._buscar_recursivo(root.left, key)
        return self._buscar_recursivo(root.right, key)
        
    def _sugerir_recursivo(self, node, prefixo, sugestoes):
        if not node:
            return

        # Se a chave atual é maior que o prefixo, vá para a esquerda
        if prefixo < node.key:
            self._sugerir_recursivo(node.left, prefixo, sugestoes)

        # Se a chave atual começa com o prefixo, adicione-a e verifique ambas as sub-árvores
        if node.key.startswith(prefixo):
            sugestoes.append(node.key)
        
        # Se a chave atual é menor que o prefixo, só precisamos olhar para a direita
        if prefixo > node.key:
            self._sugerir_recursivo(node.right, prefixo, sugestoes)
        # Se a chave atual começa com o prefixo, também olhamos para a direita
        elif node.key.startswith(prefixo):
             self._sugerir_recursivo(node.right, prefixo, sugestoes)