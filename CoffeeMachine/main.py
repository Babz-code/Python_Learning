MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coffee_game = False
money = 0

# TODO 4. Check resources sufficient?
def check_resources(resource1, ingredient1, ingredient2):
    compare_1 = resources[ingredient1]
    compare_2 = MENU[resource1][ingredient2][ingredient1]
    if compare_1 >= compare_2:
        return True
    else:
        print(f"Sorry there is not enough {ingredient1}.")


# TODO 1. . Prompt user by asking “What would you like?
while not coffee_game:
    order_type = input("What would you like? (espresso/latte/cappuccino): ").lower()

# TODO 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if order_type == "off":
        coffee_game = True

# TODO 3. Print report
    elif order_type == "report":
        print(f"water: {resources["water"]}ml")
        print(f"milk: {resources["milk"]}ml")
        print(f"coffee: {resources["coffee"]}g")
        print(f"Money: ${money}")

    else:
        ty = check_resources(order_type, "water", "ingredients")
        ty_2 = check_resources(order_type, "milk", "ingredients")
        ty_3 = check_resources(order_type, "coffee", "ingredients")

# TODO 5. Process coins.
        if ty and ty_2 and ty_3:
            print("Please enter your coins.")

            quarters = float(input("How many quarters?: "))
            dimes = float(input("How many dimes?: "))
            nickels = float(input("How many nickels?: "))
            pennies = float(input("How many pennies?: "))

            total_coins_inserted = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01

# TODO 6. Check transaction successful?
            amount = MENU[order_type]["cost"]
            change = round(total_coins_inserted - amount, )
            if total_coins_inserted < amount:
                print("Sorry that's not enough money. Money refunded.")
            elif total_coins_inserted == amount:
                money += amount
                resources["water"] -= MENU[order_type]["ingredients"]["water"]
                resources["milk"] -= MENU[order_type]["ingredients"]["milk"]
                resources["coffee"] -= MENU[order_type]["ingredients"]["coffee"]
                print(f"Here's your {order_type}☕. Enjoy")
            else:
                money += amount
                resources["water"] -= MENU[order_type]["ingredients"]["water"]
                resources["milk"] -= MENU[order_type]["ingredients"]["milk"]
                resources["coffee"] -= MENU[order_type]["ingredients"]["coffee"]
                print(f"Here is ${change} in change")
                print(f"Here's your {order_type}☕. Enjoy")
