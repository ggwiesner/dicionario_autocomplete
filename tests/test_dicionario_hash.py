# tests/test_dicionario_hash.py
from src.estruturas.dicionario_hash import DicionarioHash

def test_insercao_e_busca():
    d = DicionarioHash(10)
    d.inserir("casa")
    d.inserir("carro")
    assert d.buscar("casa") == True
    assert d.buscar("carro") == True
    assert d.buscar("bicicleta") == False

def test_sugestoes():
    d = DicionarioHash(10)
    palavras = ["casa", "casaco", "carro", "carta"]
    for p in palavras:
        d.inserir(p)
    
    assert sorted(d.sugerir("cas")) == ["casaco", "casa"]
    assert sorted(d.sugerir("car")) == ["carro", "carta"]
    assert d.sugerir("bic") == []