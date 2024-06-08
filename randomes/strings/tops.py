"""
Напишите функцию, которая принимает msg string и возвращает локальные вершины
строки от самой высокой до самой низкой.
Вершины строки получены при отображении строки следующим образом:

                                                      3
                              p                     2   4
            g               o   q                 1
  b       f   h           n       r             z
a   c   e       i       m          s          y
      d           j   l             t       x
                    k                 u   w
                                        v

Следующая вершина всегда на 1 символ выше предыдущей. В приведенном выше
примере решение abcdefghijklmnopqrstuvwxyz1234 входная строка 3pgb.

    Когда msg строка пуста, верните пустую строку.
    Входные строки могут быть очень длинными. Убедитесь, что ваше решение
    имеет хорошую производительность.

Проверьте тестовые примеры для получения дополнительных образцов.
"""


def tops(s: str) -> str:
    """
    Поиск локальных вершин строки.
    """
    r, n, x = '', 0, 1
    while x <= len(s):
        r += [s[x - 1], ''][x == 1]
        x, n = x + 5 + 4 * (n - 1), n + 1
    return r[::-1]


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("", ""),
        ("12", "2"),
        ("abcdefghijklmnopqrstuvwxyz12345", "3pgb"),
        ("abcdefghijklmnopqrstuvwxyz1236789ABCDEFGHIJKLMN", "M3pgb"),
    )
    for key, val in data:
        assert tops(key) == val


if __name__ == '__main__':
    test()
