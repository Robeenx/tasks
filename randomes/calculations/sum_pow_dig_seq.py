"""
Возьмем целое число, start и давайте выполним итерационный процесс,
описанный ниже:

    берем его цифры и возводим каждую из них в определенную степень,
    n и сложите все эти значения. (результат = r1)

    мы повторяем тот же процесс со значением r1 и так далее, k раз.

Давайте сделаем это с start = 420, n = 3, k = 5

420 ---> 72 (= 4³ + 2³ + 0³) ---> 351 (= 7³ + 2³) ---> 153 ---> 153 ----> 153

Мы можем заметить, что это заняло 3шаги для достижения циклического паттерна
[153]( h = 3). Длина этого циклического паттерна равна 1, patt_len. Последний
член наших k операций равен 153, last_term

Сейчас, start = 420, n = 4, k = 30

420 ---> 272 ---> 2433 ---> 434 ---> 593 ---> 7267 --->
6114 ---> 1554 ---> 1507 ---> 3027 ---> 2498 ---> 10929 --->
13139 ---> 6725 ---> 4338 ---> 4514 ---> 1138 ---> 4179 ---> 9219 --->
13139 ---> 6725 ---> 4338 ---> 4514 ---> 1138 ---> 4179 ---> 9219 --->
13139 ---> 6725 ---> 4338 ---> 4514 ---> 1138 ---> 4179 ---> 9219......

В этом примере мы можем наблюдать, что циклический паттерн ( cyc_patt_arr)
является [13139, 6725, 4338, 4514, 1138, 4179, 9219]с длиной 7, ( patt_len = 7),
и это заняло 12 шаги (h = 12), чтобы достичь циклического паттерна.
Последний семестр после выполнения 30операции 1138

Сделайте функцию sum_pow_dig_seq(), который получает аргументы в порядке,
показанном ниже, с соответствующим выводом:

sum_pow_dig_seq(start, n, k) ---> [h, cyc_patt_arr, patt_len, last_term]

Для приведенных нами примеров

sum_pow_dig_seq(420, 3, 5) == [3, [153], 1, 153]

sum_pow_dig_seq(420, 4, 30) == [12, [13139, 6725, 4338, 4514, 1138, 4179,
9219], 7, 1138]

Ограничения для тестов:

500 ≤ start ≤ 8000
2 ≤ n ≤ 9
100 * n ≤ k ≤ 200 * n
"""


def sum_pow_dig_seq(start: int, n: int, k: int) -> list:
    """
    Преобразования заданного числа по шаблону.
    """
    r, x = [], None
    for i in range(k):
        start = sum(int(x) ** n for x in str(start))
        if x is None:
            if start in r:
                x = r.index(start)
                r = r[x:]
                return [x + 1, r, len(r), r[(k-i-1) % len(r)]]
            r.append(start)
    return []


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ((420, 3, 5), [3, [153], 1, 153]),
        ((420, 4, 30), [12, [13139, 6725, 4338,
         4514, 1138, 4179, 9219], 7, 1138]),
        ((420, 5, 100),
         [23, [9045, 63198, 99837, 167916, 91410, 60075, 27708, 66414,
               17601, 24585, 40074, 18855, 71787, 83190, 92061, 66858, 84213,
               34068, 41811, 33795, 79467, 101463], 22, 18855]),
    )
    for key, val in data:
        assert sum_pow_dig_seq(*key) == val


if __name__ == '__main__':
    test()
