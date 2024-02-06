"""
В этой Ката вам будет предоставлен массив чисел, в котором два числа встречаются один раз,
а остальные встречаются только дважды. Вашей задачей будет вернуть сумму чисел, которые
встречаются только один раз.

Например, repeats([4,5,7,5,4,8]) = 15потому что только цифры 7и 8происходят один раз, и их
сумма равна 15. Каждое второе число встречается дважды.
"""

from collections import Counter


def repeats(arr: list) -> int:
    """
    Сумма чисел из списка, встерчеющихся только 1 раз.
    """
    return sum(x for x, i in Counter(arr).items() if i == 1)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ([4, 5, 7, 5, 4, 8], 15),
        ([9, 10, 19, 13, 19, 13], 19),
        ([16, 0, 11, 4, 8, 16, 0, 11], 12),
        ([5, 17, 18, 11, 13, 18, 11, 13], 22),
        ([5, 10, 19, 13, 10, 13], 24),
    )
    for key, val in data:
        assert repeats(key) == val


if __name__ == '__main__':
    test()
