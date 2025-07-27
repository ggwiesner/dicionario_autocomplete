# tests/test_dicionario_avl.py
import unittest
from src.estruturas.dicionario_avl import DicionarioAVL

class TestDicionarioAVL(unittest.TestCase):
    def setUp(self):
        self.avl = DicionarioAVL()
        palavras = ["banana", "banco", "bola", "abacate", "caju", "casa"]
        for p in palavras:
            self.avl.inserir(p)

    def test_buscar_palavra_existente(self):
        self.assertIsNotNone(self.avl.buscar("bola"))

    def test_buscar_palavra_inexistente(self):
        self.assertIsNone(self.avl.buscar("morango"))

    def test_sugerir_prefixo(self):
        sugestoes = self.avl.sugerir("ba")
        self.assertEqual(sorted(sugestoes), ["banana", "banco"])

    def test_sugerir_prefixo_sem_resultado(self):
        sugestoes = self.avl.sugerir("x")
        self.assertEqual(sugestoes, [])

if __name__ == '__main__':
    unittest.main()