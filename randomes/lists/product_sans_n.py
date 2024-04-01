
"""
Это адаптация проблемы, с которой я столкнулся на LeetCode.

Учитывая массив чисел, ваша задача — вернуть новый массив,
в котором каждый индекс ( new_array[i]) равно произведению исходного массива,
за исключением числа по этому индексу ( array[i]).

Две вещи, которые следует иметь в виду:

    Нули будут проникать в некоторые из предоставленных вам массивов.
    Решения O(n²) не пройдут.

Все входные массивы будут действительными массивами ненулевой длины. 
"""


from operator import mul
from functools import reduce


def product_sans_n(nums: list[int]) -> list[int]:
    """
    Произведение чисел массива, исключающее значение текущего элемента.
    """
    return [reduce(mul, nums[:i] + nums[i+1:]) for i in range(len(nums))]


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ([1, 1, 1], [1, 1, 1]),
        ([0, -99, 0], [0, 0, 0]),
        ([9, 0, -2], [0, -18, 0]),
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([2, 3, 4, 5], [60, 40, 30, 24]),
        ([-8, 1, 5, 13, -1], [-65, 520, 104, 40, -520]),
        ([3, 14, 9, 11, 11], [15246, 3267, 5082, 4158, 4158]),
        ([4, 7, 3, 6, 2, 11, 14, 4, 7, 5], [5433120, 3104640, 7244160,
                                            3622080, 10866240, 1975680, 1552320, 5433120, 3104640, 4346496]),
    )
    for key, val in data:
        assert product_sans_n(key) == val


if __name__ == '__main__':
    test()