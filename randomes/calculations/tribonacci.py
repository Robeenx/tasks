"""
Хорошо встретился со старшим братом Фибоначчи, также известным как Трибоначчи.

Как уже видно из названия, он работает в основном как Фибоначчи, но суммируя
последние 3 (вместо 2) чисел последовательности для генерации следующего.
И, что еще хуже, я, к сожалению, не смогу услышать, как люди, не являющиеся
носителями итальянского языка, пытаются его произнести :(

Итак, если мы хотим начать нашу последовательность Трибоначчи с [1, 1, 1] в
качестве начального ввода ( подпись AKA ) у нас есть такая последовательность:

[1, 1 ,1, 3, 5, 9, 17, 31, ...]

Но что, если мы начнем с [0, 0, 1] в качестве подписи? Как начиная с [0, 1]
вместо [1, 1]по сути сдвигает обычную последовательность Фибоначчи на одно место,
у вас может возникнуть соблазн подумать, что мы получим ту же последовательность,
смещенную на два места, но это не так, и мы получим:

[0, 0, 1, 1, 2, 4, 7, 13, 24, ...]

Что ж, вы, возможно, уже догадались, но чтобы внести ясность: вам нужно создать функцию
Фибоначчи, которая, учитывая подписей массив/список , возвращает первые n элементов -
подпись, включенную в полученную таким образом последовательность.
"""


def tribonacci(signature: list, n: int) -> list:
    """
    Числа "Триббоначи" заданной диапазона.
    """
    return tribonacci(signature + [sum(signature[-3:])], n) if len(signature) < n else signature[:n]


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (([1, 1, 1], 10), [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]),
        (([0, 0, 1], 10), [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]),
        (([0, 1, 1], 10), [0, 1, 1, 2, 4, 7, 13, 24, 44, 81]),
        (([1, 0, 0], 10), [1, 0, 0, 1, 1, 2, 4, 7, 13, 24]),
        (([0, 0, 0], 10), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
        (([1, 2, 3], 10), [1, 2, 3, 6, 11, 20, 37, 68, 125, 230]),
        (([3, 2, 1], 10), [3, 2, 1, 6, 9, 16, 31, 56, 103, 190]),
        (([1, 1, 1], 1), [1]),
        (([300, 200, 100], 0), []),
        (([0.5, 0.5, 0.5], 30), [0.5, 0.5, 0.5, 1.5, 2.5, 4.5, 8.5, 15.5, 28.5, 52.5, 96.5, 177.5, 326.5, 600.5, 1104.5, 2031.5, 3736.5,
                                 6872.5, 12640.5, 23249.5, 42762.5, 78652.5, 144664.5, 266079.5, 489396.5, 900140.5, 1655616.5, 3045153.5, 5600910.5, 10301680.5]),
    )
    for key, val in data:
        assert tribonacci(*key) == val


if __name__ == '__main__':
    test()
