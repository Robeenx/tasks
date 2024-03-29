"""
Учитывая массив аргументов, представляющих ключи и значения аргументов системного вызова,
объедините его в одну строку, разделенную пробелами. Вам не нужно заботиться об имени
приложения — ваша задача заключается только в параметрах.

Каждый элемент данного массива может быть:

    одна строка,
    один строковый массив,
    массив из двух строк

В последнем случае (массив из двух строк) первая строка должна иметь "--"префикс, если он имеет
длину более одного символа; или "-"префикс в противном случае; например:

    ["foo", "bar"]становится "--foo bar"
    ["f", "bar"]становится "-f bar"

Вы можете предположить, что все строки не пусты и не содержат пробелов.
Примеры

["foo", "bar"]                    #  "foo bar"
[["foo", "bar"]]                  #  "--foo bar"
[["f", "bar"]]                    #  "-f bar"
[["foo", "bar"], "baz"]           #  "--foo bar baz"
[["foo"], ["bar", "baz"], "qux"]  #  "foo --bar baz qux"
"""


def args_to_string(args: list) -> str:
    """
    Формирование строки запроса для коммандной строки из аргументов
    """
    return ' '.join(['-' * (1 < len(x) and (1 < len(x[0])) + 1) + ' '.join(x) if isinstance(x, list) else x for x in args])


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (["foo"], "foo"),
        (["f"], "f"),
        ([["f"]], "f"),
        ([["foo", "bar"]], "--foo bar"),
        ([["f", "bar"]], "-f bar"),
        ([["foo", "bar"], "baz"], "--foo bar baz"),
        ([["foo", "bar"], ["baz", "qux"]], "--foo bar --baz qux"),
    )
    for key, val in data:
        assert args_to_string(key) == val


if __name__ == '__main__':
    test()
