import json
import random

import click

from Pizza import SizeOfPizza
from receipts import Hawaiian, Margherita, Pepperoni, GLOBAL_MENU


@click.group()
def cli():
    pass


def create_menu():
    receipts = dict(Margherita(SizeOfPizza.L))
    receipts.update(dict(Pepperoni(SizeOfPizza.L)))
    receipts.update(dict(Hawaiian(SizeOfPizza.L)))
    res = '\n'.join([f'{x}: ' + ', '.join(receipts[x].keys())
                     for x in receipts])
    return res


MENU = create_menu()


@cli.command()
def menu():
    receipts = dict(Margherita(SizeOfPizza.L))
    receipts.update(dict(Pepperoni(SizeOfPizza.L)))
    receipts.update(dict(Hawaiian(SizeOfPizza.L)))
    print(MENU)


@cli.command()
@click.option('=delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
@click.argument('size', nargs=1, default='L')
def order(size: str, pizza: str, delivery: bool):
    """Готовит и доставляет пиццу"""
    PizzaClass = GLOBAL_MENU[pizza]  # достаем из меню класс нужной пиццы
    ready_pizza = PizzaClass(size)  # "готовим" нужную пиццу
    print(f'Приготовили за {random.randint(5, 125)} секунд !)')
    if delivery:
        print(f'Доставили за {random.randint(5, 125)} секунд !)')


cli()


def test():
    a = Hawaiian(SizeOfPizza.XL)
    b = Hawaiian(SizeOfPizza.L)
    print(a == b)
    print(json.dumps(dict(a), indent=4))
    u = a.recept()
    print(u)


# if __name__ == '__main__':

