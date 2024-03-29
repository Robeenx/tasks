"""
Привет. Сегодня наша задача — найти Nчисло Пипи.

Определим P n так, чтобы выполнялось следующее выражение:


p0 + (p1 + (p2 + pn ** 0.5) ** 0.5) ** 0.5

равно n, если P0 = 0.
Примеры:

pipi(0) == 0

потому что
0=00 = 00 = 0

pipi(1) == 1

потому что
0+1=10 + \sqrt { 1 } = 10 + 1
= 1

pipi(2) == 9 

потому что
0+1+9=20 + \sqrt { 1 + \sqrt { 9 } } = 20 + 1 + 9
= 2

pipi(3) == 3025

потому что
0+1+9+3025=30 + \sqrt { 1 + \sqrt { 9 + \sqrt { 3025 } } } = 30 + 1 + 9 + 3025
= 3 
"""

from functools import lru_cache


@lru_cache
def pipi(n: int) -> int:
    """
    Поиск N числа PIPI.
    """
    return ([(r := ((r := r if i - 1 else n ** 2) - pipi(i)) ** 2) for i in range(1, n)] or [n ** 2])[-1]


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (0, 0),
        (1, 1),
        (2, 9),
        (3, 3025),
        (4, 1903664161),
    )
    for key, val in data:
        assert pipi(key) == val


if __name__ == '__main__':
    test()
