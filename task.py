import timeit
import matplotlib.pyplot as plt

# Фиксированный набор данных (без random, так как range детерминирован)
test_data = list(range(10, 301, 10))  # от 10 до 300 включительно, шаг 10


def fact_recursive(n: int) -> int:
    """Рекурсивный факториал."""
    if n == 0:
        return 1
    return n * fact_recursive(n - 1)


def fact_iterative(n: int) -> int:
    """Итеративный (нерекурсивный) факториал."""
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def benchmark(func, n, repeat=7):
    """Измеряет время одного вызова func(n).

    Выполняет `repeat` независимых прогонов, каждый из которых
    состоит из ровно одного вызова функции (number=1).
    Возвращает минимальное время — это стандарт для timeit-бенчмарков.

    Args:
        func: функция для тестирования
        n: аргумент функции
        repeat: сколько раз повторить измерение

    Returns:
        float: минимальное время выполнения в секундах
    """
    # lambda нужна, чтобы замкнуть значение n
    times = timeit.repeat(lambda: func(n), number=1, repeat=repeat)
    return min(times)


def main():
    res_recursive = []
    res_iterative = []

    print("Запуск бенчмарка...")

    for n in test_data:
        print(f"Тестируем n = {n}")
        t_rec = benchmark(fact_recursive, n)
        t_it = benchmark(fact_iterative, n)
        res_recursive.append(t_rec)
        res_iterative.append(t_it)

    # Визуализация
    plt.figure(figsize=(10, 6))
    plt.plot(test_data, res_recursive, label="Рекурсивный", marker='o')
    plt.plot(test_data, res_iterative, label="Итеративный", marker='s')
    plt.xlabel("n")
    plt.ylabel("Время выполнения (милисекунды)")
    plt.title("Сравнение рекурсивного и итеративного вычисления факториала\n(бенчмарк одного вызова)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()