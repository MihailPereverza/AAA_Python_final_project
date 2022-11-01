from src.Pizza import SizeOfPizza
from src.helpers import log
from src.receipts import GLOBAL_MENU


@log('Приготовили за $time секунд!)')
def _cooking_pizza(pizza_name: str, pizza_size: str):
    # достаем из меню класс нужной пиццы
    PizzaClass = GLOBAL_MENU[pizza_name]
    # "готовим" нужную пиццу
    PizzaClass(SizeOfPizza(pizza_size))


@log('Доставили за $time секунд!)')
def _delivery_pizza():
    # типа доставили
    pass


def operate_pizza_order(pizza_name: str, pizza_size: str, delivery: bool):
    _cooking_pizza(pizza_name, pizza_size)

    if not delivery:
        return
    _delivery_pizza()
