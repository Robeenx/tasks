"""
Напишите функцию, которая принимает две квадратные матрицы
( N x Nдвумерные массивы) и возвращают сумму двух.
Обе матрицы, передаваемые в функцию, будут иметь
размер N x N(квадрат), содержащий только целые числа.

Как суммировать две матрицы:
Возьмите каждую ячейку [n][m] из первой матрицы и дополняем
ее тем же [n][m]ячейка из второй матрицы. Это будет ячейка
[n][m]матрицы решения. (За исключением C, где матрица решения
будет одномерным псевдомногомерным массивом). 
"""


def matrix_addition(a, b):
    """
    Сложение квадратных, идентичных матриц.
    """
    return [list(map(sum, zip(*x))) for x in zip(a, b)]


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ((
            [
                [1, 2, 3],
                [3, 2, 1],
                [1, 1, 1],
            ],
            [
                [2, 2, 1],
                [3, 2, 3],
                [1, 1, 3],
            ],
        ),
        [
            [3, 4, 4],
            [6, 4, 4],
            [2, 2, 4],
        ]),
    )

    for key, val in data:
        assert matrix_addition(*key) == val


if __name__ == '__main__':
    test()
