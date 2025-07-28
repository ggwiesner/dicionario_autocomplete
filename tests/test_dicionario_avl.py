# tests/test_dicionario_avl.py
import pytest
from src.estruturas.dicionario_avl import DicionarioAVL

@pytest.fixture
def dicionario_pequeno():
    d = DicionarioAVL()
    palavras = ["gato", "casa", "carro", "zebra", "flor", "dado"]
    for p in palavras:
        d.inserir(p)
    return d

# --- Testes de Funcionalidade Básica (semelhantes aos da Hash) ---

def test_insercao_e_busca_simples(dicionario_pequeno):
    assert dicionario_pequeno.buscar("gato") == True
    assert dicionario_pequeno.buscar("dado") == True

def test_busca_palavra_inexistente(dicionario_pequeno):
    assert dicionario_pequeno.buscar("bicicleta") == False

# --- Testes de Casos Limites ---

def test_dicionario_vazio():
    d_vazio = DicionarioAVL()
    assert d_vazio.buscar("qualquercoisa") == False
    assert d_vazio.sugerir("a") == []
    assert d_vazio.root is None

def test_insercao_duplicada(dicionario_pequeno):
    # Uma forma de testar é verificar se a árvore não muda (p. ex., altura da raiz)
    altura_antes = dicionario_pequeno.root.height
    dicionario_pequeno.inserir("gato") # Inserir duplicata
    altura_depois = dicionario_pequeno.root.height
    assert altura_antes == altura_depois
    assert dicionario_pequeno.buscar("gato") == True

# --- TESTES CRUCIAIS: GARANTINDO O BALANCEAMENTO DA AVL ---
# Estes testes verificam se as rotações estão sendo feitas corretamente.

def test_rotacao_simples_direita_LL():
    """Testa o caso de desbalanceamento Esquerda-Esquerda (LL)."""
    avl = DicionarioAVL()
    avl.inserir("c")
    avl.inserir("b")
    # A inserção a seguir deve causar uma rotação à direita
    avl.inserir("a")
    
    # O nó 'b' deve se tornar a raiz
    assert avl.root.key == "b"
    # 'a' e 'c' devem ser seus filhos
    assert avl.root.left.key == "a"
    assert avl.root.right.key == "c"
    # A altura da raiz deve ser 2
    assert avl.root.height == 2

def test_rotacao_simples_esquerda_RR():
    """Testa o caso de desbalanceamento Direita-Direita (RR)."""
    avl = DicionarioAVL()
    avl.inserir("a")
    avl.inserir("b")
    # A inserção a seguir deve causar uma rotação à esquerda
    avl.inserir("c")
    
    assert avl.root.key == "b"
    assert avl.root.left.key == "a"
    assert avl.root.right.key == "c"
    assert avl.root.height == 2

def test_rotacao_dupla_esquerda_direita_LR():
    """Testa o caso de desbalanceamento Esquerda-Direita (LR)."""
    avl = DicionarioAVL()
    avl.inserir("c")
    avl.inserir("a")
    # A inserção a seguir deve causar uma rotação dupla
    avl.inserir("b")
    
    assert avl.root.key == "b"
    assert avl.root.left.key == "a"
    assert avl.root.right.key == "c"
    assert avl.root.height == 2
    
def test_rotacao_dupla_direita_esquerda_RL():
    """Testa o caso de desbalanceamento Direita-Esquerda (RL)."""
    avl = DicionarioAVL()
    avl.inserir("a")
    avl.inserir("c")
    # A inserção a seguir deve causar uma rotação dupla
    avl.inserir("b")
    
    assert avl.root.key == "b"
    assert avl.root.left.key == "a"
    assert avl.root.right.key == "c"
    assert avl.root.height == 2

# --- Testes da Funcionalidade de Sugestão ---

def test_sugestao_avl(dicionario_pequeno):
    # palavras inseridas: ["gato", "casa", "carro", "zebra", "flor", "dado"]
    assert set(dicionario_pequeno.sugerir("ca")) == {"casa", "carro"}
    assert set(dicionario_pequeno.sugerir("da")) == {"dado"}
    assert dicionario_pequeno.sugerir("xyz") == []