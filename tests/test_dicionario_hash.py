# tests/test_dicionario_hash.py
import pytest
from src.estruturas.dicionario_hash import DicionarioHash

# Fixture para criar um dicionário pequeno e populado para os testes
@pytest.fixture
def dicionario_pequeno():
    d = DicionarioHash(tamanho=10) # Tamanho pequeno para forçar colisões
    palavras = ["casa", "carro", "casaco", "gato", "garfo"]
    for p in palavras:
        d.inserir(p)
    return d

# --- Testes de Funcionalidade Básica ---

def test_insercao_e_busca_simples(dicionario_pequeno):
    """Testa se palavras inseridas podem ser encontradas."""
    assert dicionario_pequeno.buscar("casa") == True
    assert dicionario_pequeno.buscar("garfo") == True

def test_busca_palavra_inexistente(dicionario_pequeno):
    """Testa se a busca por uma palavra que não existe retorna False."""
    assert dicionario_pequeno.buscar("bicicleta") == False
    assert dicionario_pequeno.buscar("cas") == False # Prefixo não é a palavra

# --- Testes de Casos Limites (Edge Cases) ---

def test_dicionario_vazio():
    """Testa o comportamento de um dicionário recém-criado."""
    d_vazio = DicionarioHash(tamanho=10)
    assert d_vazio.buscar("qualquercoisa") == False
    assert d_vazio.sugerir("a") == []

def test_insercao_duplicada(dicionario_pequeno):
    """Testa se inserir a mesma palavra duas vezes não causa erro nem duplicatas."""
    # O comportamento esperado é que a palavra exista, mas não seja duplicada na lista do bucket.
    # Primeiro, verificamos o estado antes
    indice = dicionario_pequeno._hash("casa")
    num_antes = len(dicionario_pequeno.tabela[indice])
    
    # Insere novamente
    dicionario_pequeno.inserir("casa")
    
    num_depois = len(dicionario_pequeno.tabela[indice])
    
    # O número de elementos no bucket não deve mudar
    assert num_antes == num_depois
    assert dicionario_pequeno.buscar("casa") == True

# --- Testes da Funcionalidade de Sugestão ---

def test_sugestao_com_resultados(dicionario_pequeno):
    """Testa se a sugestão retorna a lista correta de palavras."""
    # A ordem pode variar, então comparamos conjuntos (sets)
    assert set(dicionario_pequeno.sugerir("cas")) == {"casa", "casaco"}
    assert set(dicionario_pequeno.sugerir("ga")) == {"gato", "garfo"}

def test_sugestao_sem_resultados(dicionario_pequeno):
    """Testa o caso de um prefixo que não corresponde a nenhuma palavra."""
    assert dicionario_pequeno.sugerir("xyz") == []

def test_sugestao_prefixo_completo(dicionario_pequeno):
    """Testa se um prefixo que é uma palavra completa ainda retorna sugestões."""
    assert set(dicionario_pequeno.sugerir("casa")) == {"casa", "casaco"}