from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

moneymachine = MoneyMachine()
coffeemaker = CoffeeMaker()
menu = Menu()
while True:
        entry = input("What would you like?")
        entry = entry.lower()
        if entry == "off" or entry == "quit":
            break
        elif entry == "menu" or entry == "m":
            print(menu.get_items())
        elif entry == "report" or entry == "r":
            coffeemaker.report()
        else:
            entry = Menu.find_drink(menu, entry)
            check_resources = coffeemaker.is_resource_sufficient(entry)
            if check_resources == True:
                payment = moneymachine.make_payment(entry.cost)
                if payment == True:
                    coffeemaker.make_coffee(entry)
