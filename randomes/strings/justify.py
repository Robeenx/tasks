"""
Ваша задача в этой ката — эмулировать выравнивание текста моноширинным шрифтом.
Вам будет предоставлен однострочный текст и ожидаемая ширина выравнивания.
Самое длинное слово никогда не будет больше этой ширины.

Вот правила:

    Используйте пробелы, чтобы заполнить пробелы между словами.
    Каждая строка должна содержать как можно больше слов.
    Используйте '\n' для разделения строк.
    Пробел между словами не может отличаться более чем на один пробел.
    Строки должны заканчиваться словом, а не пробелом.
    '\n' не включается в длину строки.
    Сначала идут большие промежутки, затем меньшие
    («Лорем--сам--боль--сит-амет», (2, 2, 2, 1 пробела)).
    Последняя строка не должна быть по ширине, между словами используйте
    только один пробел. Последняя строка не должна содержать '\n'
    Строки, состоящие из одного слова, не нуждаются в пробелах
    («somelongword\n»).

"""


def justify(text: str, width: int) -> str:
    """
    Выравнивание текста по заданной ширине.
    """
    txt, res, tmp = text.split(), [], []

    for i, x in enumerate(txt + [''], -len(txt)):
        if not i or tmp and width <= sum(map(len, (*tmp, tmp, x))) - 1:
            line = ' '.join(tmp)
            if i and len(tmp) > 1:
                a, b = divmod(width - sum(map(len, tmp)), len(tmp) - 1)
                line = line.replace(' ', ' ' * a).replace(' ' * a, ' ' * (a+1), b)
            res.append(line)
            tmp = []
        tmp.append(x)
    return '\n'.join(res)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (('123 45 6', 7), '123  45\n6'),
    )
    for key, val in data:
        assert justify(*key) == val

if __name__ == '__main__':
    test()
