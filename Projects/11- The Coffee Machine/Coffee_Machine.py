from Coffee_Machine_Stuffs import *
import time

items_list = list(MENU.keys())

# Functions

def show_resources():
    
    print(f"Water: {resources["water"]} ml")
    print(f"Milk: {resources["milk"]} ml")
    print(f"Coffee: {resources["coffee"]} g")
    print(f"Money: ${profit}")
    
def show_menu():
    
    print(f"Today's Menu:")
    print(f"Items       Price")
    for i in range(len(items_list)):
        print(f"{items_list[i]}       ${MENU[items_list[i]]["cost"]}")
        
def check_resources(prompt_str):
    
    ingredients = MENU[prompt_str]["ingredients"]
    items_needed = list(ingredients)
    checker = []
    for i in items_needed:
        if resources[i] >= ingredients[i]:
            checker.append(True)
        else:
            checker.append(False)
    return all(checker)
        
def adjust_resources(prompt_str):  
    
    ingredients = MENU[prompt_str]["ingredients"]
    items_to_adjust = list(ingredients)    
    for i in items_to_adjust:
        item_amount = ingredients[i]
        resources[i] -= item_amount
        
def take_payment(prompt_str):
    
    print("Please insert coins.")
    q = int(input("how many quarters?: "))
    d = int(input("how many dimes?: "))
    n = int(input("how many nickels?: "))
    p = int(input("how many pennies?: "))
    paid_amount = sum([q * 0.25, d * 0.1, n * 0.05, p * 0.01])
    item_cost =  MENU[prompt_str]["cost"]
    to_return = paid_amount - item_cost
    if paid_amount < item_cost:
        print("Sorry that's not enough money. Money refunded.")
        return 0
    else:
        global profit
        print(f"Here is ${to_return:.2f} in change.")
        print(f"Here is your {prompt_str} ☕. Enjoy!!")
        profit += item_cost
        print(f"Profit till now: {profit}")
        return 1

# Main

def process_prompt(prompt_str):
    
    if prompt_str == "report":
        show_resources()
    elif prompt_str == "off":
        print("Closing Machine...")
        time.sleep(1)
        print("Bye")
    elif prompt_str == "menu":
        show_menu()
    elif prompt_str in items_list:
        checked_resource = check_resources(prompt_str)
        if checked_resource == True:
            print(f"{prompt_str} available.")
            process_pay = take_payment(prompt_str)
            if process_pay == 0:
                pass
            else:
                adjust_resources(prompt_str)
        else:
            print(f"Sorry. {prompt_str} is not available at the moment.")
    # elif prompt_str == "off":
    #     pass
    else:
        print("Please type again.")
        prompt = input("What would you like? ")
        process_prompt(prompt)

# ON & OFF

print(logo)
print("Welcome to The Coffee Corner!!")

end_machine = False
prompt = input("What would you like? ")

while not end_machine:
    process_prompt(prompt)
    if prompt == "off":
        end_machine = True
    else:
        prompt = input("What would you like? ")
        
        