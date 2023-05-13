"""
2520 - самое маленькое число, которое делится без остатка
на все числа от 1 до 10.

Какое самое маленькое число делится нацело на все числа от 1 до 20?
"""


def func(N: int) -> int:
    """Поиск минимального числа, которое делится без остатка на все числа
    от 1 до N"""
    num = 0
    while True:
        num += 2
        for i in range(3, N):
            if num * N % i:
                break
        else:
            return num * N


def test() -> None:
    """Тестирование работы алгоритмов."""
    assert func(10) == 2520
    assert func(20) == 232792560


if __name__ == '__main__':
    test()