from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
print('lets start')
my_menu=Menu()                          #creating the object of class Menu
my_coffee_maker=CoffeeMaker()           #creating the object of class CoffeeMaker()
my_money_machine=MoneyMachine()         #creating the object of class MoneyMachine()

option=my_menu.get_items()              #making the instance by attaching the attributes & saving it in option variable
is_on=True
while is_on:
    choice=input(f"what is it you want to drink ({option})")
    if choice=="off":
        is_on=False
    elif choice=="report":              #this help to make report
        my_coffee_maker.report()        #report of coffee ingredients
        my_money_machine.report()       #report of money machine
    else:
        drink=my_menu.find_drink(choice)                        #this search the name and if the name is present it storename in drink
        if (my_coffee_maker.is_resource_sufficient(drink)):     #checking the resources of the drink
            if my_money_machine.make_payment(drink.cost):       #this do the money section all <<making and calculating the profit (drink.cost determine the cost)
                (my_coffee_maker.make_coffee(drink))            #Ending statement print by it


