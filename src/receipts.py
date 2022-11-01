from typing import Dict, Type

from Pizza import Ingredient, Ingredients, Pizza, SizeOfPizza


class Margherita(Pizza):
    def __init__(self, size):
        super().__init__(size)
        self._ingredients = Ingredients(
            [
                Ingredient('tomato sauce', 1, 'g', size, (1, 1.2)),
                Ingredient('mozzarella', 1, 'g', size, (1, 1.2)),
                Ingredient('tomatoes', 1, 'g', size, (1, 1.2)),
            ]
        )

    @property
    def name(self):
        return 'Margherita🧀'


class Pepperoni(Pizza):
    def __init__(self, size: SizeOfPizza):
        super().__init__(size)
        self._ingredients = Ingredients(
            [
                Ingredient('tomato sauce', 1, 'g', size, (1, 1.05)),
                Ingredient('mozzarella', 1, 'g', size, (1, 1.11)),
                Ingredient('pepperoni', 1, 'g', size, (1, 1.1)),
            ]
        )

    @property
    def name(self):
        return 'Pepperoni🍕'


class Hawaiian(Pizza):
    def __init__(self, size):
        super().__init__(size)
        self._ingredients = [
            Ingredient('tomato sauce', 1, 'g', size, (1, 1.2)),
            Ingredient('mozzarella', 1, 'g', size, (1, 1.3)),
            Ingredient('chicken', 1, 'g', size, (1, 1.25)),
            Ingredient('pineapples', 1, 'g', size, (1, 1.13)),
        ]

    @property
    def name(self):
        return 'Hawaiian🍍'


GLOBAL_MENU: Dict[str, Type[Margherita | Pepperoni | Hawaiian]] = {
    'Margherita': Margherita,
    'Pepperoni': Pepperoni,
    'Hawaiian': Hawaiian,
}
