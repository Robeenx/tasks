"""
Удалите в целочисленном массиве все положительные числа,
которые являются палиндромами
"""


def lst_wout_pos_pal(lst: list) -> list:
    """Создает новый целочисленный массив на основе данного,
    в котором удаляются все положительные числа, являющиеся
    палиндромами."""
    return [i for i in lst if i % 2 or (s := str(i)) != s[::-1]]


def test() -> None:
    """Тестирование работы алгоритмов."""
    lst1 = [252, 343, 231, 482]
    lst2 = lst_wout_pos_pal(lst1)
    lst3 = [343, 231, 482]

    assert lst2 == lst3


if __name__ == '__main__':
    test()
