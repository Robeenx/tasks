"""
Удалите в целочисленном массиве все положительные числа,
которые являются палиндромами
"""


def func(lst: list) -> list:
    """Создает новый целочисленный массив на основе данного,
    в котором удалены все положительные числа, являющиеся
    палиндромами"""
    return [i for i in lst if i % 2 or (s := str(i)) != s[::-1]]


def test() -> None:
    """Тестирование работы алгоритмов."""
    assert func([252, 343, 231, 482]) == [343, 231, 482]


if __name__ == '__main__':
    test()