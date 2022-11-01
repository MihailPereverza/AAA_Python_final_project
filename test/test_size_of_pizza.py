from src.Pizza import SizeOfPizza


def test_create_coef():
    coef = SizeOfPizza.create_coef((1.2, 1.3))
    assert coef == {'L': 1.2, 'XL': 1.3}


def test_values():
    values = [x.value for x in SizeOfPizza]
    names = [x.name for x in SizeOfPizza]
    assert set(values) == {'L', 'XL'}
    assert set(names) == {'L', 'XL'}
