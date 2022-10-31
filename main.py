import json

import click

from Pizza import SizeOfPizza
from receipts import Hawaiian, Margherita, Pepperoni


# @click.group()
# def cli():
#     pass


# def create_menu():
#     receipts = dict(Margherita(SizeOfPizza.L))
#     receipts.update(dict(Pepperoni(SizeOfPizza.L)))
#     receipts.update(dict(Hawaiian(SizeOfPizza.L)))
#     res = '\n'.join([f'{x}: ' + ', '.join(receipts[x].keys())
#                      for x in receipts])
#     return res
#
#
# MENU = create_menu()


# @cli.command()
# @click.option(' =delivery', default=False, is_flag=True)
# @click.argument('pizza', nargs=1)
# def order(pizza: str, delivery: bool) :
#     """Готовит и доставляет пиццу"""
#
#
# @cli.command()
# def menu():
#     receipts = dict(Margherita(SizeOfPizza.L))
#     receipts.update(dict(Pepperoni(SizeOfPizza.L)))
#     receipts.update(dict(Hawaiian(SizeOfPizza.L)))
#     print(MENU)
#
#
# def test():
a = Hawaiian(SizeOfPizza.XL)
b = Hawaiian(SizeOfPizza.L)
print(a == b)
print(json.dumps(dict(a), indent=4))
u = a.recept()
print(u)
#
#
# if __name__ == '__main__':
#     cli()
