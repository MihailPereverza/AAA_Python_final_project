from helpers import ingredient

from src.Pizza import Ingredients


def test_create():
    list_of_ingredients = [ingredient(0), ingredient(1)]
    ingredients = Ingredients(list_of_ingredients)
    assert isinstance(ingredients, list)
    assert set(ingredients.ingredients) == {'test1', 'test2'}
