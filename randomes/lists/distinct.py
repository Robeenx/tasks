"""
Определите функцию, которая удаляет дубликаты из массива
неотрицательных чисел и возвращает их в качестве результата.
Порядок последовательности должен оставаться прежним.
"""


def distinct(seq: list[int]) -> list[int]:
    """Удаление дубликатов с сохранением последовательности"""
    return sorted(set(seq), key=seq.index)


def test() -> None:
    """Тестирование работы алгоритмов."""

    data = (
        ([1], [1]),
        ([1, 2], [1, 2]),
        ([1, 1, 2], [1, 2]),
        ([1, 1, 1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 7, 7], [1, 2, 3, 4, 5, 6, 7]),
    )

    for key, val in data:
        assert distinct(key) == val


if __name__ == '__main__':
    test()
