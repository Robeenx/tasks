"""
Допустим, возьмем две строки, A и B, и определим сходство строк
как длину самого длинного префикса, общего для обеих строк.
Например, сходство строк abc и abdравно 2, а сходство строк
aaa и aaab это 3.

напишите функцию, которая вычисляет сумму сходств строки S с
каждым из ее суффиксов.

Примеры (ввод -> вывод):
'ababaa' -> 11
'abc' -> 3

Объяснение:
В первом случае суффиксы строки имеют вид ababaa, babaa, abaa, baa, aaи a.
Сходство каждой из этих строк со строкой ababaaравны 6,0,3,0,1,1
соответственно. Таким образом, ответ: 6 + 0 + 3 + 0 + 1 + 1 = 11.

Во втором случае ответ просто 3 + 0 + 0 = 3.

Примечание. В каждой строке будет хотя бы один символ — нет необходимости
проверять пустые строки.
"""


def string_suffix(s: str) -> int:
    """
    Сумма сходств строки.
    """
    res = 0
    for i in range(len(s)):
        for x in range(len(s), i, -1):
            if s.startswith(s[i:x]):
                res += len(s[i:x])
                break
    return res


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ('aa', 3),
        ('abc', 3),
        ('ababaa', 11),
        ('aaaa', 10),
        ('aaaaa', 15),
        ('aaaaaa', 21),
        ('mnsomn', 8),
        ('apple', 5),
        ('a', 1),
        ('pippi', 8),
        ('gsjgozmfvtyxyso', 16),
    )
    for key, val in data:
        assert string_suffix(key) == val


if __name__ == '__main__':
    test()
