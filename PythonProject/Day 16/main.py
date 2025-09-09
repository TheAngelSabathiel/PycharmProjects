from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_project_menu = Menu()
coffee_project_coffee_maker = CoffeeMaker()
coffee_project_money_machine = MoneyMachine()

turn_off = False

while not turn_off:
    what_to_do = input(f"What would you like? ({coffee_project_menu.get_items()})\n")
    if what_to_do == "off":
        turn_off = True
    elif what_to_do == "report":
        coffee_project_coffee_maker.report()
        coffee_project_money_machine.report()
    else:
        want_drink = coffee_project_menu.find_drink(what_to_do)
        if coffee_project_coffee_maker.is_resource_sufficient(want_drink):
            enough_paid = coffee_project_money_machine.make_payment(want_drink.cost)
            if enough_paid:
                coffee_project_coffee_maker.make_coffee(want_drink)
