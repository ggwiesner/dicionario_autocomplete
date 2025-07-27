# tests/test_dicionario_hash.py

import unittest
from src.estruturas.dicionario_hash import DicionarioHash

class TestDicionarioHash(unittest.TestCase):

    def setUp(self):
        """Este método é executado antes de cada teste."""
        self.hash_dict = DicionarioHash()
        palavras = ["banana", "banco", "bola", "abacate", "caju", "casa"]
        for p in palavras:
            self.hash_dict.inserir(p, f"Definição de {p}")

    def test_inserir_e_buscar_palavra_existente(self):
        """Testa se uma palavra inserida pode ser encontrada."""
        self.hash_dict.inserir("teste", "Definição de teste")
        self.assertEqual(self.hash_dict.buscar("teste"), "Definição de teste")

    def test_buscar_palavra_inexistente(self):
        """Testa se a busca por uma palavra que não existe retorna None."""
        self.assertIsNone(self.hash_dict.buscar("morango"))

    def test_sugerir_com_prefixo_valido(self):
        """Testa a função de autocomplete para um prefixo que tem correspondências."""
        sugestoes = self.hash_dict.sugerir("ca")
        # O resultado deve ser uma lista ordenada
        self.assertEqual(sugestoes, ["caju", "casa"])

    def test_sugerir_com_prefixo_sem_correspondencia(self):
        """Testa a função de autocomplete para um prefixo que não tem correspondências."""
        sugestoes = self.hash_dict.sugerir("xyz")
        self.assertEqual(sugestoes, [])

    def test_sugerir_com_prefixo_que_corresponde_a_palavra_inteira(self):
        """Testa se a palavra completa é sugerida se o prefixo for igual a ela."""
        sugestoes = self.hash_dict.sugerir("bola")
        self.assertEqual(sugestoes, ["bola"])

if __name__ == '__main__':
    unittest.main()