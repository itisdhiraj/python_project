from art import logo
print(logo)
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 25
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

def is_resource_sufficient(order_ingredient):
    is_enough = True
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            is_enough= False
    return is_enough

def process_coins():
    """Return the total calculated coins inserted"""
    print("Please Insert Coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int( input( "How many dimes?: " ) ) * 0.1
    total += int( input( "How many nickels?: " ) ) * 0.05
    total += int( input( "How many pennies?: " ) ) * 0.01
    return total

def is_transaction_success(money_received, drink_cast):
    """Return True when the payment is accepted or False if money is insufficient."""
    if money_received>= drink_cast:
        change = round(money_received - drink_cast, 2)
        print(f"Here is the ${change}.")
        global profit
        profit += drink_cast
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}.")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_success(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])




