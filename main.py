MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO 4: Check resources sufficient?
def are_resources_available(drink):
    ingredients = MENU[drink]['ingredients']
    for j in ingredients:
        if resources.get(j) < ingredients.get(j):
            return False
    return True


def make_coffee(drink):
    ingredients = MENU[drink]['ingredients']
    for j in ingredients:
        resources[j] -= ingredients.get(j)


def process_coins(choice):
    cost = MENU[choice]['cost']
    print("Please insert coins.")
    quarters = int(input("How many quarters?")) * 0.25
    dimes = int(input("How many dimes?")) * 0.10
    nickles = int(input("How many nickles?")) * 0.05
    pennies = int(input("How many pennies?")) * 0.01
    total = quarters + dimes + nickles + pennies
    return total


def is_transaction_successful(choice, total):
    global profit
    cost = MENU[choice]['cost']
    if cost > total:
        print("Sorry your money is not enough to purchase a coffee!")
        return False
    elif cost <= total:
        change = total - cost
        print(f"Here's your change {round(change)}$")
        profit += cost
        return True


def play():
    is_on = True
    enough_resources = True
    while is_on and enough_resources:
        # TODO 1: Prompt user by asking “What would you like?
        choice = str(input("Hello I'm the Coffee Machine!\nWhat would you like to drink?(espresso/latte/cappuccino):"))
        # TODO 2: Turn off the Coffee Machine by entering "off” to the prompt.
        if choice.lower() == "off":
            print("Coffee Machine has been turned off!")
            is_on = False
        # TODO 3: Print report.
        elif choice.lower() == "report":
            print(resources)
        elif choice.lower() == "espresso" or choice.lower() == "latte" or choice.lower() == "cappuccino":
            if not are_resources_available(choice):
                print("Resources are not enough to make your coffee, Sorry!")
                enough_resources = False
            else:
                # TODO 5: Process coins
                total = process_coins(choice)
                # TODO 6: Check transaction successful?
                if is_transaction_successful(choice, total):
                    # TODO 7: Make Coffee
                    make_coffee(choice)
                    print(f"Here's your {choice}! Enjoy your drink")
        else:
            print("Incorrect Choice")


play()
