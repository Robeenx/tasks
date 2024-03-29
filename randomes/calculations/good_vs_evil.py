"""
В Средиземье вот-вот начнется война. Силам добра предстоит немало сражений с силами зла. Разумеется,
будут задействованы разные расы. Каждая раса имеет определенные worthкогда сражаешься с другими.
На стороне добра у нас есть следующие расы и связанные с ними worth:

    Хоббиты: 1
    Мужчины: 2
    Эльфы: 3
    Гномы: 3
    Иглз: 4
    Волшебники: 10

На стороне зла мы имеем:

    Орки: 1
    Мужчины: 2
    Варги: 2
    Гоблины: 2
    Где находится Урук: 3
    Тролли: 5
    Волшебники: 10

Хотя погода, местоположение, припасы и доблесть играют роль в любой битве, если сложить ценность
стороны добра и сравнить ее с ценностью стороны зла, то победит сторона с большей ценностью.

Таким образом, учитывая подсчет каждой из рас на стороне добра, а затем подсчет каждой из рас на
стороне зла, определите, какая сторона победит.
Вход:

Функция будет иметь два параметра. Каждый параметр представляет собой строку из нескольких целых
чисел, разделенных одним пробелом. Каждая строка будет содержать количество каждой расы на стороне
добра и зла.

Первый параметр будет содержать количество каждой расы на стороне добра в следующем порядке:

    Хоббиты, Люди, Эльфы, Гномы, Орлы, Волшебники.

Второй параметр будет содержать количество каждой расы на стороне зла в следующем порядке:

    Орки, Люди, Варги, Гоблины, Урук Хай, Тролли, Волшебники.

Все значения являются неотрицательными целыми числами. Результирующая сумма значений для каждой
стороны не будет превышать предел 32-битного целого числа.
Выход:

Возвращаться "Battle Result: Good triumphs over Evil"если добро победит, "Battle Result: Evil
eradicates all trace of Good"если зло победит, или "Battle Result: No victor on this battle
field"если дело закончится вничью.
"""


def good_vs_evil(good: str, evil: str) -> str:
    """
    Определяет победителя.
    """
    n = [[1, 2, 3, 3, 4, 10], [1, 2, 2, 2, 3, 5, 10]]
    a, b = [sum(a * b for a, b in zip(a, map(int, b.split()))) for a, b in zip(n, (good, evil))]
    res = {a < b: 'Evil eradicates all trace of Good', a > b: 'Good triumphs over Evil'}
    return f"Battle Result: {res.get(1, 'No victor on this battle field')}"


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (('1 1 1 1 1 1', '1 1 1 1 1 1 1'),  'Battle Result: Evil eradicates all trace of Good'),
        (('0 0 0 0 0 10', '0 1 1 1 1 0 0'), 'Battle Result: Good triumphs over Evil'),
        (('1 0 0 0 0 0', '1 0 0 0 0 0 0'),  'Battle Result: No victor on this battle field'),
    )
    for key, val in data:
        assert good_vs_evil(*key) == val


if __name__ == '__main__':
    test()
