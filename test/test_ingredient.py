from src.Pizza import Ingredient, SizeOfPizza


def test_creation():
    name, amount, uom, portion = 'test', 1.2345, 'uom', SizeOfPizza.L
    coef = (1, 1)
    ingredient = Ingredient(
        name=name,
        amount=amount,
        unit_of_measure=uom,
        portion=portion,
        _coef=coef,
    )
    assert ingredient.name == name
    assert ingredient.amount == amount
    assert ingredient.unit_of_measure == uom
    assert ingredient.portion == portion
    assert ingredient._coef == coef


def test_set_amount():
    amount, coef = 1.2345, (1.1, 1.2)
    ingredient = Ingredient(
        name='test',
        amount=amount,
        unit_of_measure='uom',
        portion=SizeOfPizza.L,
        _coef=coef,
    )
    assert ingredient.amount == amount * coef[0]
