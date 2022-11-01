from src.Pizza import SizeOfPizza
from src.receipts import Hawaiian, Margherita, Pepperoni


def create_menu() -> str:
    receipts = dict(Margherita(SizeOfPizza.L))
    receipts.update(dict(Pepperoni(SizeOfPizza.L)))
    receipts.update(dict(Hawaiian(SizeOfPizza.L)))
    res = '\n'.join([f'{x}: ' + ', '.join(receipts[x].keys())
                     for x in receipts])
    return res


MENU = create_menu()


def show_menu():
    receipts = dict(Margherita(SizeOfPizza.L))
    receipts.update(dict(Pepperoni(SizeOfPizza.L)))
    receipts.update(dict(Hawaiian(SizeOfPizza.L)))
    print(MENU)
