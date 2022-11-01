from cli_methods.operate_pizza_order import operate_pizza_order
from cli_methods.show_menu import show_menu

import click


@click.group()
def cli():
    pass


@cli.command()
def menu():
    show_menu()


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
@click.argument('size', nargs=1, default='L')
def order(size: str, pizza: str, delivery: bool):
    """Готовит и доставляет пиццу"""
    operate_pizza_order(pizza, size, delivery)


cli()
