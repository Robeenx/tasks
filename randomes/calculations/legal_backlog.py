"""
В здании суда накопилось несколько дел, которые необходимо рассмотреть,
и он пытается составить эффективный график для устранения этой очереди.
Вам 1будут предоставлены следующие входные данные:
 - Словарь cases чьи значения представляют собой количество судебных заседаний,
 которые необходимо завершить по каждому делу.
 - Целое число max_daily_sessionsчто дает максимальное количество судебных
 заседаний, которые могут проводиться каждый день.

Важно отметить, что невозможно провести два заседания по одному и
тому же делу в один и тот же день.

Напишите функцию, которая определяет минимальное количество дней,
необходимое для очистки журнала.
"""

import math


def legal_backlog(cases: dict, sess: int) -> int:
    """
    Поиск минимального кол-ва дней для проведения всех дел.
    """
    return max(list(cases.values()) + [math.ceil(sum(cases.values()) / sess)])


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (({'A': 4, 'B': 3, 'C': 2}, 5), 4),
        (({'A': 4, 'B': 3, 'C': 2}, 3), 4),
        (({'A': 4, 'B': 3, 'C': 2}, 1), 9),
        (({'A': 4, 'B': 3, 'C': 2}, 2), 5),
        (({'A': 4, 'B': 4, 'C': 4}, 2), 6),
        (({'A': 2, 'B': 5, 'C': 9, 'D': 1}, 3), 9),
    )
    for key, val in data:
        assert legal_backlog(*key) == val


if __name__ == '__main__':
    test()