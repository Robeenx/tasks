"""
Даны два массива a и b написать функцию comp(a, b), который проверяет,
содержат ли два массива «одинаковые» элементы с одинаковой кратностью (кратность элемента
— это количество раз, когда он появляется). «То же самое» здесь означает, что элементы в
b являются элементами в a в квадрате, независимо от порядка.
"""
from operator import eq
from collections import Counter


def comp(array1: list, array2: list) -> bool:
    return not set(map(type, (array1, array2))) - {list, } and eq(*map(Counter, ([x ** 2 for x in array1], array2)))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (([121, 144, 19, 161, 19, 144, 19, 11],
          [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]), True),
        (([121, 144, 19, 161, 19, 144, 19, 11],
          [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]), False),
        (([121, 144, 19, 161, 19, 144, 19, 11],
          [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]), False),
    )
    for key, val in data:
        assert comp(*key) == val


if __name__ == '__main__':
    test()
