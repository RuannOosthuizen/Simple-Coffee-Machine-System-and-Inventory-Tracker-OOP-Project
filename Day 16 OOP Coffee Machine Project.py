# Imported libraries:
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Objects created:
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

# Here the variable so the machine repeates itself is defined:
is_on = True

# The main code block:
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
          coffee_maker.make_coffee(drink)