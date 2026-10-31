"""Testes automatizados do CommitFlow."""

import tempfile
import unittest
from pathlib import Path

from src.monitor import verificar_arquivos


class TestVerificarArquivos(unittest.TestCase):
    def test_arquivo_existente(self):
        with tempfile.TemporaryDirectory() as pasta:
            arquivo = Path(pasta) / "exemplo.txt"
            arquivo.write_text("teste", encoding="utf-8")

            resultado = verificar_arquivos([str(arquivo)])

            self.assertTrue(resultado["sucesso"])
            self.assertEqual(resultado["encontrados"], 1)
            self.assertEqual(resultado["ausentes"], 0)

    def test_arquivo_ausente(self):
        with tempfile.TemporaryDirectory() as pasta:
            arquivo = Path(pasta) / "inexistente.txt"

            resultado = verificar_arquivos([str(arquivo)])

            self.assertFalse(resultado["sucesso"])
            self.assertEqual(resultado["ausentes"], 1)

    def test_lista_vazia(self):
        resultado = verificar_arquivos([])

        self.assertTrue(resultado["sucesso"])
        self.assertEqual(resultado["total"], 0)


if __name__ == "__main__":
    unittest.main()
