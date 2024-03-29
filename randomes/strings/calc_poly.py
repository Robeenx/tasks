"""
Вам будет предоставлен список с коэффициентами полинома. Посмотрите в следующем порядке в обоих случаях:

P(x) =       6x³ + 3x² + 5x -4
coefficients =  [ 6,   3,    5, -4]

Ваша задача — выразить полином в виде строки с его значением для определенного определенного x:

[6, 3, 5, -4], 4 returns "For 6*x^3 + 3*x^2 + 5*x - 4 with x = 4 the value is 448"

Если у нас есть некоторые коэффициенты, равные 0, соответствующий ему член не будет виден.

[2, 0, 5, -6, 4, 0], 2 returns "For 2*x^5 + 5*x^3 - 6*x^2 + 4*x with x = 2 the value is 88"

Интересным будет случай, когда первый коэффициент равен -1

[-1, -6, 28, 79], 35 returns "For -x^3 - 6*x^2 + 28*x + 79 with x = 35 the value is -49166"

Следующий ответ будет считаться неправильным:

"For -1x^3 - 6*x^2 + 28*x + 79 with x = 35 the value is -49166"

Вы не получите пустой список и значения переменной. xбудет справедливым для всех случаев. 
"""


def calc_poly(lst: list[int], x: int) -> str:
    """
    Расписывает каждое действие вычисления по заданному алгоритму.
    """
    r, s = 0, ''
    for i, n in enumerate(lst, -len(lst) + 1):
        r += n * x ** abs(i)
        t = [[' - ', '-'][not s], [' + ', ''][not s]][0 < n] + [str(abs(n)), ''][not abs(n) - 1]
        s += [t + ['*x'[not abs(n) - 1:] + ['', f'^{abs(i)}'][i < -1], ''][not i], ''][not n]
    return f'For {s} with x = {x} the value is {r}'


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (([6, 3, 5, -4], 4), "For 6*x^3 + 3*x^2 + 5*x - 4 with x = 4 the value is 448"),
        (([2, 0, 5, -6, 4, 0], 2), "For 2*x^5 + 5*x^3 - 6*x^2 + 4*x with x = 2 the value is 88"),
        (([10, 26, 12], -70), "For 10*x^2 + 26*x + 12 with x = -70 the value is 47192"),
        (([7, -10, -25], 0), "For 7*x^2 - 10*x - 25 with x = 0 the value is -25"),
    )
    for key, val in data:
        assert calc_poly(*key) == val


if __name__ == '__main__':
    test()
