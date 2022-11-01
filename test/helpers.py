from src.Pizza import Ingredient, SizeOfPizza


def ingredient(number):
    return Ingredient(
        name=f'test{number + 1}',
        amount=number + 1.3,
        unit_of_measure='uom',
        portion=SizeOfPizza.L,
        _coef=(number + 1.1, number + 2.2),
    )
