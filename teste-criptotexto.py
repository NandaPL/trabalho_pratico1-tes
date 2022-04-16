import unittest
import criptotexto


class TesteCryptotextFuncional(unittest.TestCase):
    def test_cryptotext_01(self):
        result = criptotexto.cryptotext('')
        self.assertEqual(result, 'Entrada inválida')

    def test_cryptotext_02(self):
        result = criptotexto.cryptotext('NoTApasCAL')
        self.assertEqual(result, 'sapo')

    def test_cryptotext_03(self):
        result = criptotexto.cryptotext('56a90ul043')
        self.assertEqual(result, 'lua')

    def test_cryptotext_04(self):
        result = criptotexto.cryptotext('atE QUEa tabELATER MINE')
        self.assertEqual(result, 'batata')

    def test_cryptotext_05(self):
        result = criptotexto.cryptotext('NJNDNSN')
        self.assertEqual(result, 'Sem mensagem oculta')

    def test_cryptotext_06(self):
        result = criptotexto.cryptotext('@gUJniH%&p#pOoHEXhs')
        self.assertEqual(result, 'shopping')

    def test_cryptotext_07(self):
        result = criptotexto.cryptotext('3')
        self.assertEqual(result, 'Entrada inválida')


class TesteCriptotextoEstrutural(unittest.TestCase):
    def test_cryptotext_01(self):
        result = criptotexto.cryptotext('')
        self.assertEqual(result, 'Entrada inválida')

    def test_cryptotext_02(self):
        result = criptotexto.cryptotext('NoTApasCAL')
        self.assertEqual(result, 'sapo')

    def test_cryptotext_03(self):
        result = criptotexto.cryptotext('NJNDNSN')
        self.assertEqual(result, 'Sem mensagem oculta')

    def test_cryptotext_04(self):
        result = criptotexto.cryptotext('3')
        self.assertEqual(result, 'Entrada inválida')
