import unittest

# Функция, которую будем тестировать
from binary import gen_bin_tree

# Тесты
class TestMath(unittest.TestCase):
    def test_1(self):
        self.assertEqual(gen_bin_tree(4, 7), {'7': {'left leaf': {'21': {'left leaf': {'63': {'left leaf': {'189': {'left leaf': {'567': {}}, 'right leaf': {'185': {}}}}, 'right leaf': {'59': {'left leaf': {'177': {}}, 'right leaf': {'55': {}}}}}}, 'right leaf': {'17': {'left leaf': {'51': {'left leaf': {'153': {}}, 'right leaf': {'47': {}}}}, 'right leaf': {'13': {'left leaf': {'39': {}}, 'right leaf': {'9': {}}}}}}}}, 'right leaf': {'3': {'left leaf': {'9': {'left leaf': {'27': {'left leaf': {'81': {}}, 'right leaf': {'23': {}}}}, 'right leaf': {'5': {'left leaf': {'15': {}}, 'right leaf': {'1': {}}}}}}, 'right leaf': {'-1': {'left leaf': {'-3': {'left leaf': {'-9': {}}, 'right leaf': {'-7': {}}}}, 'right leaf': {'-5': {'left leaf': {'-15': {}}, 'right leaf': {'-9': {}}}}}}}}}}
)

    def test_2(self):
        self.assertEqual(gen_bin_tree(0,7), {'7': {}})

    def test_3(self):
        self.assertEqual(gen_bin_tree(1, 7), {'7': {'left leaf': {'21': {}}, 'right leaf': {'3': {}}}})

    def test_4(self):
        self.assertEqual(gen_bin_tree(5, 3), {'3': {'left leaf': {'9': {'left leaf': {'27': {'left leaf': {'81': {'left leaf': {'243': {'left leaf': {'729': {}}, 'right leaf': {'239': {}}}}, 'right leaf': {'77': {'left leaf': {'231': {}}, 'right leaf': {'73': {}}}}}}, 'right leaf': {'23': {'left leaf': {'69': {'left leaf': {'207': {}}, 'right leaf': {'65': {}}}}, 'right leaf': {'19': {'left leaf': {'57': {}}, 'right leaf': {'15': {}}}}}}}}, 'right leaf': {'5': {'left leaf': {'15': {'left leaf': {'45': {'left leaf': {'135': {}}, 'right leaf': {'41': {}}}}, 'right leaf': {'11': {'left leaf': {'33': {}}, 'right leaf': {'7': {}}}}}}, 'right leaf': {'1': {'left leaf': {'3': {'left leaf': {'9': {}}, 'right leaf': {'-1': {}}}}, 'right leaf': {'-3': {'left leaf': {'-9': {}}, 'right leaf': {'-7': {}}}}}}}}}}, 'right leaf': {'-1': {'left leaf': {'-3': {'left leaf': {'-9': {'left leaf': {'-27': {'left leaf': {'-81': {}}, 'right leaf': {'-31': {}}}}, 'right leaf': {'-13': {'left leaf': {'-39': {}}, 'right leaf': {'-17': {}}}}}}, 'right leaf': {'-7': {'left leaf': {'-21': {'left leaf': {'-63': {}}, 'right leaf': {'-25': {}}}}, 'right leaf': {'-11': {'left leaf': {'-33': {}}, 'right leaf': {'-15': {}}}}}}}}, 'right leaf': {'-5': {'left leaf': {'-15': {'left leaf': {'-45': {'left leaf': {'-135': {}}, 'right leaf': {'-49': {}}}}, 'right leaf': {'-19': {'left leaf': {'-57': {}}, 'right leaf': {'-23': {}}}}}}, 'right leaf': {'-9': {'left leaf': {'-27': {'left leaf': {'-81': {}}, 'right leaf': {'-31': {}}}}, 'right leaf': {'-13': {'left leaf': {'-39': {}}, 'right leaf': {'-17': {}}}}}}}}}}}})

    def test_5(self):
        self.assertEqual(gen_bin_tree(2, 10), {'10': {'left leaf': {'30': {'left leaf': {'90': {}}, 'right leaf': {'26': {}}}}, 'right leaf': {'6': {'left leaf': {'18': {}}, 'right leaf': {'2': {}}}}}}
)

    def test_6(self):
        self.assertEqual(gen_bin_tree(-1, 4), {})

# Запуск тестов
unittest.main(argv=[''], verbosity=2, exit=False)
