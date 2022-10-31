from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import List, Dict, Tuple, Self, ForwardRef


class SizeOfPizza(Enum):
    L = 'L'
    XL = 'XL'

    @classmethod
    def create_coef(cls, coef) -> Dict[Self, float]:
        return {cls.L: coef[0], cls.XL: coef[1]}


@dataclass
class Ingredient:
    name: str
    amount: float
    unit_of_measure: str
    portion: SizeOfPizza
    _coef: Tuple[float, float]

    def __post_init__(self):
        print(SizeOfPizza.create_coef(self._coef))
        self.amount *= SizeOfPizza.create_coef(self._coef)[self.portion]


class Ingredients(list):
    def __init__(self, ingredients: List[Ingredient]):
        super().__init__()
        self.extend(ingredients)
        self._ingredients = tuple(x.name for x in ingredients)

    @property
    def ingredients(self) -> Tuple[str]:
        return self._ingredients


PizzaRef = ForwardRef('Pizza')


class Pizza(ABC):
    def __init__(self, size: SizeOfPizza):
        self._size = size
        self._ingredients = None

    @property
    @abstractmethod
    def name(self):
        return ''

    @property
    def size(self):
        return self._size

    def recept(self) -> Ingredients:
        return self._ingredients

    @property
    def __ingredients_to_dict(self):
        return {x.name: f'{x.amount}{x.unit_of_measure}'
                for x in self.recept()}

    def __iter__(self):
        yield self.name, self.__ingredients_to_dict

    def __eq__(self, other: Self):
        b_name = self.name == other.name
        b_size = self._size == other.size
        return b_name & b_size

