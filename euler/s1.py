"""
Если выписать все натуральные числа меньше 10,
кратные 3 или 5, то получим 3, 5, 6 и 9.
Сумма этих чисел равна 23.

Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
"""


def multiples(num: int) -> int:
    """Сумма чисел < num, кратные 3 или 5."""
    return sum(i for i in range(1, num) if not i % 3 or not i % 5)


def test() -> None:
    """Тестирование работы алгоритмов."""
    assert multiples(10) == 23
    assert multiples(1000) == 233168


if __name__ == '__main__':
    test()
