import unittest

# Функция, которую будем тестировать
from main import two_sum

# Тесты
class TestMath(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0,1])

    def test_add_negative(self):
        self.assertEqual(two_sum([3, 2, 4], 6), [1,2])

    def test_add_zero(self):
        self.assertEqual(two_sum([3, 3], 6), [0, 1])

# Запуск тестов
unittest.main(argv=[''], verbosity=2, exit=False)
