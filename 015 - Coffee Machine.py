# Spyder Editor
# Created on Tue Oct 12 15:19:37 2021
# @author: Mani Mehrabi
# Part of a Python Bootcamp - Beginner
# 015 - Coffee Machine
    
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 3000,
    "milk": 200,
    "coffee": 100,
}


def print_report(list_of_repositories):
    print(f"Water: {list_of_repositories[0]}ml\nMilk: {list_of_repositories[1]}ml\nCoffee: {list_of_repositories[2]}g\nMoney: ${list_of_repositories[3]}")

    
def fill_machine():
    materials = []
    materials.append(resources["water"])
    materials.append(resources["milk"])
    materials.append(resources["coffee"])
    materials.append(0)
    return materials


def check_resources(flavor, amount_of_resources):
    if flavor[0] > amount_of_resources[0]:
        return"water"
    elif flavor[1] > amount_of_resources[1]:
        return "milk"
    elif flavor[2] > amount_of_resources[2]:
        return "coffee"
    else:
        return ""
    
    
def flavor_requirement(flavor):
    return [MENU[flavor]["ingredients"]["water"], MENU[flavor]["ingredients"]["milk"], MENU[flavor]["ingredients"]["coffee"]]


def ask_for_money():
    print("Please insert coins.")
    quarter = int(input("How many quarters?: "))
    dime = int(input("How many dimes?: "))
    nickel = int(input("How many nickels?: "))
    penny = int(input("How many pennies?: "))
    return quarter * 0.25 + dime * 0.1 + nickel * 0.05 + penny * 0.01
    
    
def check_payment(amount, flavor):
    return amount - MENU[flavor]["cost"]


def make_coffee(machine, flavor, money):
    result = []
    result.append(machine[0] - flavor[0])
    result.append(machine[1] - flavor[1])
    result.append(machine[2] - flavor[2])
    result.append(machine[3] + money)
    return result
    

def machine():
    machine_resources = fill_machine()
    machine_on = True
    while machine_on:
        request = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if request == "off":
            machine_on = False
        elif request == "report":
            print_report(machine_resources)
        elif request == "espresso" or request == "latte" or request == "cappuccino":
            flavor = flavor_requirement(request)
            lack_of_resource = check_resources(flavor, machine_resources)
            if lack_of_resource == "":
                payment = ask_for_money()
                change = round(check_payment(payment, request), 2)
                if change >= 0:
                    print(f"Here is ${change} in change.")
                    machine_resources = make_coffee(machine_resources, flavor, (payment - change))
                    print("Here is your latte. Enjoy!")
                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                print(f"Sorry! There is not enough {lack_of_resource}")
            

machine()