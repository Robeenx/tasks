"""
У механический часов, сломалась минутная стрелка.
Необходимо, зная угол отклонения часовой стрелки,
векнуть текущее время в 12-ти часовом формате (02:00)
"""

from operator import mod, truediv as div


def what_time_is_it(n: int) -> str:
    """Определяет время по углу минутной стрелки"""
    return ':'.join(('%d' % x([n, n + 360][n < 30] / 360 * 720, 60)).zfill(2) for x in [div, mod])


def test() -> None:
    """Тестирование работы алгоритмов."""

    data = (
        (0, '12:00'),
        (30, '01:00'),
        (90, '03:00'),
        (180, '06:00'),
        (270, '09:00'),
        (360, '12:00'),
    )

    for key, val in data:
        assert what_time_is_it(key) == val


if __name__ == '__main__':
    test()
