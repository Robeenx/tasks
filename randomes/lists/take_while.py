"""
Вот еще один важный момент для функционального программиста. У вас есть
последовательность значений и некоторый предикат для этих значений.
Вы хотите получить самый длинный префикс элементов, чтобы предикат
был истинным для каждого элемента. Мы назовем это takeWhileфункция.
Он принимает два аргумента. Первый — это последовательность значений,
а второй — функция-предикат. Функция не меняет значение исходной
последовательности.

Пример:

sequence : [2,4,6,8,1,2,5,4,3,2]
predicate: is an even number
result   : [2,4,6,8]

Ваша задача — реализовать функцию takeWhile.
"""


from typing import Callable


def take_while(arr: list[int], pred_fun: Callable) -> list[int]:
    """
    Из заданного списка создание предикат значений.
    """
    return next((arr[:i] for i, x in enumerate(arr) if not pred_fun(x)), arr)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    is_even = lambda x: not x % 2

    data = [
        (([], is_even), []),
        (([2,6,4,10,1,5,4,3], is_even), [2,6,4,10]),
        (([2,100,1000,10000,5,3,4,6], is_even), [2,100,1000,10000]),
        (([2,4,10,100,64,78,92], is_even), [2,4,10,100,64,78,92]),
    ]

    for key, val in data:
        assert take_while(*key) == val


if __name__ == '__main__':
    test()
