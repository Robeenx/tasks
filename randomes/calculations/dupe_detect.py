"""
Цель:
По мере роста числа опубликованных ката на Codewars растет и вероятность
того, что недавно опубликованная ката будет дубликатом уже существующей.
Это наиболее распространено среди более простых белых ката (7 или 8 кю).
Обеспокоенные постоянно растущим числом дубликатов, вы решили начать
работу над автоматизированным процессом,который отфильтровывает дубликаты
ката начального уровня.

Ваша цель — написать функцию, которая будет находить дубликаты в списке
недавно опубликованных ката. Ваша функция будет служить предварительным
фильтром; он должен идентифицировать наиболее очевидные дубликаты в
списке, передавая аргументы решениям авторов и сравнивая результаты.

Вход:
Ваша функция получит массив функций.  Эти функции являются авторскими
решениями для их недавно опубликованных ката.

Выход:
Ваша функция должна возвращать двумерный массив.  Каждый подмассив будет
состоять из значений индексов функций, дублирующих друг друга. Массив
будет отсортирован в порядке возрастания на основе значения индекса
первого дубликата, который появляется для соответствующей группы.
Если дубликатов нет, вернуть пустой массив.

Технические детали:
Каждая функция принимает только один аргумент — целочисленное значение в
диапазоне от 0 до 255 включительно.
Все функции являются чистыми функциями, поэтому не будет экземпляров функций,
которые включают методы Date или что-то в этом роде.
Максимальная длина массива 50
Ввод всегда будет действительным.
"""

from functools import reduce
from operator import add


def dupe_detect(functions: callable) -> list:
    """Поиск дубликатов функций имеющих одинаковую задачу."""
    temp = {}
    for i, func in enumerate(functions):
        data = tuple(map(func, range(255)))
        temp[data] = temp.get(data, []) + [i]

    return [v for v in temp.values() if len(v) > 1]


def test() -> None:
    """Тестирование работы алгоритмов."""

    numbers = range(10)

    kata_list = [
        lambda x: x * 2,
        lambda x: x ** 2,
        lambda x: x + 20,
        lambda x: x / 1024,
        lambda x: x * x,
        lambda x: pow(x, 2),
        lambda x: x % 2,
        lambda x: x * 2 ** 4,
        lambda x: x << 4,
        lambda x: tuple(e + x for e in numbers),
        lambda x: tuple(e * x for e in numbers),
        lambda x: tuple(map(x.__add__, numbers)),
        lambda x: reduce(add, numbers, x),
        lambda x: tuple(filter(x.__lt__, numbers)),
        lambda x: tuple(e for e in numbers if not e <= x),
    ]

    test_cases = [
        (kata_list[:9], [[1, 4, 5], [7, 8]]),
        (kata_list[9:], [[0, 2], [4, 5]]),
        (kata_list[8:11], []),
        (kata_list, [[1, 4, 5], [7, 8], [9, 11], [13, 14]]),
    ]

    for functions, expected in test_cases:
        assert dupe_detect(functions) == expected


if __name__ == '__main__':
    test()
