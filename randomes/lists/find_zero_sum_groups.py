"""
Вам дан массив положительных и отрицательных целых чисел и число nи n > 1. Массив может содержать элементы, встречающиеся более одного раза. Найдите все комбинации из n элементов массива, сумма которых равна 0.

arr = [1, -1, 2, 3, -2]
n = 3
find_zero_sum_groups(arr, n) == [-2, -1, 3] # -2 - 1 + 3 = 0

Функция должна выводить каждую комбинацию или группу в порядке возрастания.

У нас может быть более одной группы:

arr = [1, -1, 2, 3, -2, 4, 5, -3 ]
n = 3
find_zero_sum_groups(arr, n) == [[-3, -2, 5], [-3, -1, 4], [-3, 1, 2], [-2, -1, 3]]

В приведенном выше случае функция должна вывести отсортированный двумерный массив.

Функция не выдаст группу дважды и более, а только один раз.

arr = [1, -1, 2, 3, -2, 4, 5, -3, -3, -1, 2, 1, 4, 5, -3 ]
n = 3
find_zero_sum_groups(arr, n) == [[-3, -2, 5], [-3, -1, 4], [-3, 1, 2], [-2, -1, 3]]

Если комбинаций с суммой, равной 0, нет, функция выдаст предупреждающее сообщение.

arr = [1, 1, 2, 3]
n = 2
find_zero_sum_groups(arr, n) == "No combinations"

Если функция получает пустой массив, она выводит конкретное предупреждение:

arr = []
n = 2
find_zero_sum_groups(arr, n) == "No elements to combine"

"""


from itertools import combinations as cb


def find_zero_sum_groups(arr: list, n: int) -> list | str:
    """
    Поиск вхождений согласно шаблону.
    """
    if not arr:
        return "No elements to combine"

    res = sorted(map(list, {x for x in cb(sorted(arr), n) if not sum(x) and len(set(x)) == n}))

    if not res:
        return "No combinations"
    if len(res) == 1:
        return res[-1]
    return res


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (([1, -1, 2, 3, -2], 3), [-2, -1, 3]),
        (([1, -1, 2, 3, -2, 4, 5, -3], 3), [[-3, -2, 5], [-3, -1, 4], [-3, 1, 2], [-2, -1, 3]]),
        (([1, -1, 2, 3, -2, 4, 5, -3, -3, -1, 2, 1, 4, 5, -3], 3),
         [[-3, -2, 5], [-3, -1, 4], [-3, 1, 2], [-2, -1, 3]]),
        (([1, 1, 2, 3], 2), "No combinations"),
        (([], 2), "No elements to combine"),
    )
    for key, val in data:
        assert find_zero_sum_groups(*key) == val


if __name__ == '__main__':
    test()
