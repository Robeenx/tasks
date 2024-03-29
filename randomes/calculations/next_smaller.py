"""
Напишите функцию, которая принимает положительное целое число и возвращает
следующее меньшее положительное целое число, содержащее те же цифры.

Например:

next_smaller(21) == 12
next_smaller(531) == 513
next_smaller(2071) == 2017

Возврат -1 (для Haskell: возвращаться Nothing, для Rust: возвращаться None),
когда не существует меньшего числа, содержащего такие же цифры.
Также верните -1, если следующее меньшее число с теми же цифрами потребует,
чтобы первая цифра была равна нулю.

next_smaller(9) == -1
next_smaller(135) == -1
next_smaller(1027) == -1  # 0721 is out since we don't write numbers with leading zeros

    некоторые тесты будут включать очень большие числа.
    В тестовых данных используются только положительные целые числа.
"""


def next_smaller(n: int) -> int:
    """
    Поиск максимального числа, меньше текущего при перестановки цифр исходного.
    """
    s = str(n)[::-1]
    for i, x in enumerate(s):
        a, b = '0123456789'[not (i + 1) % len(s):int(x)], s[:i]
        m = max(set(a) & set(b), default='9')
        if x > m:
            return int(''.join(sorted(x + b.replace(m, '', 1)) + [m, s[i+1:]])[::-1])
    return -1


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (100, -1),
        (315, 153),
        (907, 790),
        (531, 513),
        (135, -1),
        (414, 144),
        (1207, 1072),
        (2071, 2017),
        (29009, 20990),
        (123456789, -1),
        (123456798, 123456789),
        (1234567908, 1234567890),
    )
    for key, val in data:
        assert next_smaller(key) == val


if __name__ == '__main__':
    test()
