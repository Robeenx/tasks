"""
Завершите решение так, чтобы оно возвращало true, если оно содержит повторяющиеся значения
аргументов. В функцию можно передать любое количество аргументов.

Передаваемые значения массива будут только строками или числами. Единственными допустимыми
возвращаемыми значениями являются trueи false.

Примеры:

solution(1, 2, 3)             -->  false
solution(1, 2, 3, 2)          -->  true
solution('1', '2', '3', '2')  -->  true


"""


def is_duplicates(*args):
    """
    Проверяет, есть ли дубликаты значений в переданных аргументах.
    """
    return bool(next((1 for i, x in enumerate(args) if x in args[:i]), 0))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ((1, 2, 3, 1, 2), True),
        ((), False),
        ((1, 1), True),
        ((1, 0), False),
        (('a', 'b'), False),
        (('a', 'b', 'a'), True),
        ((1, 2, 42, 3, 4, 5, 42), True),
        (('a', 'b', 'c', 'd'), False),
        (('a', 'b', 'c', 'd'), False),
        (('a', 'b', 'c', 'c'), True),
        (('a', 'b', 'c', 'd', 'e', 'f', 'f', 'b'), True),
    )
    for key, val in data:
        assert is_duplicates(*key) == val


if __name__ == '__main__':
    test()