from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

espresso = MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5)
latte = MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5)
cappuccino = MenuItem(name="cappuccino", water=250, milk=100, coffee=24, cost=3.0)

print(espresso)
print(latte)
print(cappuccino)
