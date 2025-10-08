import unittest

# Функция, которую будем тестировать
from main import two_sum

# Тесты
class TestMath(unittest.TestCase):
    def test_1(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0,1])

    def test_2(self):
        self.assertEqual(two_sum([3, 2, 4], 6), [1,2])

    def test_3(self):
        self.assertEqual(two_sum([3, 3], 6), [0, 1])

    def test_4(self):
        self.assertEqual(two_sum([12, -6, 9, -3], 9), [0, 3])

    def test_5(self):
        self.assertEqual(two_sum([13, -26, 0, 5, 22], 27), [3, 4])

    def test_6(self):
        self.assertEqual(two_sum([13, -26, 0, 5, 22], -13), [0, 1])

    def test_7(self):
        self.assertEqual(two_sum([11, 23, 6, -5, 50, 10], 18), [1, 3])

# Запуск тестов
unittest.main(argv=[''], verbosity=2, exit=False)
