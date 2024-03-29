"""
Пит любит печь торты. У него есть несколько рецептов и ингредиентов.
К сожалению, он не силен в математике. Можете ли вы помочь ему узнать,
сколько тортов он сможет испечь по его рецептам?

Напишите функцию cakes(), который принимает рецепт (объект) и
доступные ингредиенты (также объект) и возвращает максимальное
количество тортов, которые Пит может испечь (целое число).
Для простоты нет единиц измерения количества (например,
1 фунт муки или 200 г сахара — это просто 1 или 200).
Ингредиенты, отсутствующие в объектах, можно принять за 0.
"""


def cakes(recipe: dict, available: dict) -> int:
    """Поиск минимального кол-ва тортов по рецепту из ингридиентов."""
    return min(available.get(k, 0) // v for k, v in recipe.items())


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (
            (
                {"flour": 500, "sugar": 200, "eggs": 1},
                {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200},
            ),
            2
        ),
        (
            (
                {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},
                {"sugar": 500, "flour": 2000, "milk": 2000},
            ),
            0
        ),
    )
    for key, val in data:
        assert cakes(*key) == val


if __name__ == '__main__':
    test()
