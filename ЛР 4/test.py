import unittest

# Функция, которую будем тестировать
from bin1 import gen_bin_tree

# Тесты
class TestMath(unittest.TestCase):
    def test_1(self):
        self.assertEqual(gen_bin_tree(4, 7), {'7': {'left leaf': {'21': {'left leaf': {'63': {'left leaf': {'189': {}}, 'right leaf': {'59': {}}}}, 'right leaf': {'17': {'left leaf': {'51': {}}, 'right leaf': {'13': {}}}}}}, 'right leaf': {'3': {'left leaf': {'9': {'left leaf': {'27': {}}, 'right leaf': {'5': {}}}}, 'right leaf': {'-1': {'left leaf': {'-3': {}}, 'right leaf': {'-5': {}}}}}}}})

    def test_2(self):
        self.assertEqual(gen_bin_tree(0,7), {})

    def test_3(self):
        self.assertEqual(gen_bin_tree(1, 7), {'7': {}})

    def test_4(self):
        self.assertEqual(gen_bin_tree(5, 3), {'3': {'left leaf': {'9': {'left leaf': {'27': {'left leaf': {'81': {'left leaf': {'243': {}}, 'right leaf': {'77': {}}}}, 'right leaf': {'23': {'left leaf': {'69': {}}, 'right leaf': {'19': {}}}}}}, 'right leaf': {'5': {'left leaf': {'15': {'left leaf': {'45': {}}, 'right leaf': {'11': {}}}}, 'right leaf': {'1': {'left leaf': {'3': {}}, 'right leaf': {'-3': {}}}}}}}}, 'right leaf': {'-1': {'left leaf': {'-3': {'left leaf': {'-9': {'left leaf': {'-27': {}}, 'right leaf': {'-13': {}}}}, 'right leaf': {'-7': {'left leaf': {'-21': {}}, 'right leaf': {'-11': {}}}}}}, 'right leaf': {'-5': {'left leaf': {'-15': {'left leaf': {'-45': {}}, 'right leaf': {'-19': {}}}}, 'right leaf': {'-9': {'left leaf': {'-27': {}}, 'right leaf': {'-13': {}}}}}}}}}})

    def test_5(self):
        self.assertEqual(gen_bin_tree(2, 10), {'10': {'left leaf': {'30': {}}, 'right leaf': {'6': {}}}})

    def test_6(self):
        self.assertEqual(gen_bin_tree(3, 4), {'4': {'left leaf': {'12': {'left leaf': {'36': {}}, 'right leaf': {'8': {}}}}, 'right leaf': {'0': {'left leaf': {'0': {}}, 'right leaf': {'-4': {}}}}}})

# Запуск тестов
unittest.main(argv=[''], verbosity=2, exit=False)