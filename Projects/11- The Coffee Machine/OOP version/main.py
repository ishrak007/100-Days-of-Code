from Coffee_Machine_Stuffs import *
import time
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

def process_prompt(prompt_str):
    
    checked_for_prompt = menu.find_drink(prompt_str)
    item_available = checked_for_prompt[0]
    item_instance = checked_for_prompt[1]
    if prompt_str == "report":
        coffee_maker.report()
        money_machine.report()
    elif prompt_str == "off":
        print("Closing Machine...")
        time.sleep(1)
        print("Bye")
    elif prompt_str == "menu":
        print(menu.get_items())
    elif item_available == True:
        resources_ok = coffee_maker.is_resource_sufficient(item_instance)
        if resources_ok == True:
            print(f"{prompt_str} available.")
            payment_ok = money_machine.make_payment(item_instance.cost)
            if payment_ok == True:
                coffee_maker.make_coffee(item_instance)
            else:
                pass
        else:
            print(f"Sorry. {prompt_str} is not available at the moment.")
    else:
        print("Please type again.")

# Main

print(logo)
print("Welcome to The Coffee Corner!!")

end_machine = False

while not end_machine:
    prompt = input("What would you like? ")
    process_prompt(prompt)
    if prompt == "off":
        end_machine = True