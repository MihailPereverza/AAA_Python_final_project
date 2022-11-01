from src.Pizza import Pizza, SizeOfPizza, Ingredients, Ingredient
from helpers import ingredient


def test_create():
    pizza_name = 'test_pizza'
    list_of_ingredients = [ingredient(0), ingredient(1)]
    ingredients = Ingredients(list_of_ingredients)

    class ImplementPizza(Pizza):
        name = pizza_name

        def __init__(self, size: SizeOfPizza):
            super().__init__(size)
            self._ingredients = ingredients

    implementation = ImplementPizza(SizeOfPizza.L)
    assert implementation.name == pizza_name
    assert implementation.size == SizeOfPizza.L.value
    assert implementation._size == SizeOfPizza.L
    assert implementation._ingredients == ingredients


def test_dict():
    pizza_name = 'test_pizza'
    list_of_ingredients = [ingredient(0), ingredient(1)]
    ingredients = Ingredients(list_of_ingredients)

    class ImplementPizza(Pizza):
        name = pizza_name

        def __init__(self, size: SizeOfPizza):
            super().__init__(size)
            self._ingredients = ingredients

    implementation = ImplementPizza(SizeOfPizza.L)
    assert dict(implementation) == {pizza_name: {
        x.name: str(x.amount) + x.unit_of_measure
        for x in list_of_ingredients
    }}


def test_eq():
    pizza_name = 'test_pizza'
    list_of_ingredients = [ingredient(0), ingredient(1)]
    ingredients = Ingredients(list_of_ingredients)

    class ImplementPizza(Pizza):
        name = pizza_name

        def __init__(self, size: SizeOfPizza):
            super().__init__(size)
            self._ingredients = ingredients

    implementationL1 = ImplementPizza(SizeOfPizza.L)
    implementationL2 = ImplementPizza(SizeOfPizza.L)
    implementationXL = ImplementPizza(SizeOfPizza.XL)
    assert implementationL1 == implementationL2
    assert not implementationL1 == implementationXL
