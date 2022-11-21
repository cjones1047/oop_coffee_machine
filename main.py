# TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”. Prompt should show again after
#  customer drink is dispensed

# TODO 2. Turn off the Coffee Machine by entering “off” to the prompt.

# TODO 3. Print report by user entering 'report' which shows the resources left in the coffee machine

# TODO 4. Check if resources are sufficient to make the drink the user requests. If resources are insufficient,
#  should print to user which resources are insufficient

# TODO 5. If resources are sufficient, prompt user to insert coins totalling cost of drink. Calculate the total
#  value of all coins user inserts

# TODO 6. Check is transaction is successful by making sure that total is equal to at least as much as the cost of
#  the drink. If what the user inserted is insufficient, then tell them it was so and refund money. If user
#  inserted money WAS sufficient and too much, print the change being returned and add remainder to money property
#  in resources. If user inserted money was perfect amount print nothing, just add user's charge to 'money'
#  property.

# TODO 7. Make coffee and adjust resources accordingly if the transaction was successful. After resources are
#  deducted, print 'Here is your {user_choice}. Enjoy.' and return to asking the user what they would like.

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

espresso = MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5)
latte = MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5)
cappuccino = MenuItem(name="cappuccino", water=250, milk=100, coffee=24, cost=3.0)

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

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
        print(drink)
