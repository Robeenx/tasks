"""
«Игра в ракушки» включает в себя перевернутые чашки на игровой поверхности, под одну из которых
помещается мяч. Индексы чашек меняются местами несколько раз. После этого игроки попытаются найти,
в каком стаканчике лежит мяч.

Ваша задача состоит в следующем. Учитывая чашку, под которой начинается мяч, и список перестановок,
верните местоположение мяча в конце. Чашки задаются как индексы массива/списка.

Например, учитывая исходное положение 0и свопы [(0, 1), (1, 2), (1, 0)]:

    Первый обмен перемещает мяч из 0к 1
    Второй обмен перемещает мяч из 1к 2
    Окончательный обмен не влияет на положение мяча.

Так

find_the_ball(0, [(0, 1), (2, 1), (0, 1)]) == 2

Кубков в этой игре не обязательно будет всего три, но будет как минимум два. Вы можете предположить,
что все свопы действительны и включают два разных индекса.
"""


def find_the_ball(n: int, swaps: list[tuple]) -> int:
    """
    Определяет в каком находится шарик.
    """
    return [n := [n, [a, b][n == a]][n in (a, b)] for a, b in swaps][-1] if swaps else n


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ((5, []), 5),
        ((0, [(0, 1), (2, 1), (0, 1)]), 2),
    )
    for key, val in data:
        assert find_the_ball(*key) == val


if __name__ == '__main__':
    test()
