def report():
    print(f"Resource values:")
    for key in resources:
        if key == "water" or key == "milk":
            print(f"{key.capitalize()} : {resources[key]} ml")
        else:
            print(f"{key.capitalize()} : {resources[key]} g")
    print(f"Money : ${money} ")

def get_payment():
    print("Insert quantity of coins for payment:")
    dollars = 0
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0
    while True:
        try:
            dollars = int(input("Dollars: "))
            break
        except ValueError:
            print("Invalid input. Please input a whole number only.")
    while True:
        try:
            quarters = int(input("Quarters: "))
            break
        except ValueError:
            print("Invalid input. Please input a whole number only.")
    while True:
        try:
            dimes = int(input("Dimes: "))
            break
        except ValueError:
            print("Invalid input. Please input a whole number only.")
    while True:
        try:
            nickels = int(input("Nickels: "))
            break
        except ValueError:
            print("Invalid input. Please input a whole number only.")
    while True:
        try:
            pennies = int(input("Pennies: "))
            break
        except ValueError:
            print("Invalid input. Please input a whole number only.")
    return dollars * 1 + quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01

def resource_check(coffee):
    global is_sufficient
    is_sufficient = {}
    for key in menu[coffee]["ingredients"]:
        if menu[coffee]["ingredients"][key] <= resources[key]:
            is_sufficient[key] = 1
        else:
            is_sufficient[key] = 0
    if 0 in is_sufficient.values():
        return False
    else:
        return True

menu = {
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

resources = {
    "water": 500,
    "milk": 500,
    "coffee": 500,
}

money = 0
is_sufficient = {}

want_to_exit = False
while not want_to_exit:
    answer = input("What would you like? (espresso/latte/cappuccino)?\n").lower()
    if answer == "espresso" or answer == "latte" or answer == "cappuccino":
        sufficient = resource_check(answer)
        if sufficient:
            payment = get_payment()
            if menu[answer]["cost"] > payment:
                print("Sorry that's not enough money. Money refunded.")
            else:
                change = payment - menu[answer]["cost"]
                money += menu[answer]["cost"]
                for y in menu[answer]["ingredients"]:
                    resources[y] -= menu[answer]["ingredients"][y]
                print(f"Here is your delectable {answer} ☕️. Enjoy!")
                if change != 0:
                    print(f"Also, please accept {change:.2f} for your change.")
        else:
            print(f"Sorry there is not enough of the following:")
            for i in is_sufficient:
                if is_sufficient[i] == 0:
                    print(f"- {i}")
    elif answer == "off":
        want_to_exit = True
    elif answer == "report":
        report()
    else:
        print("Please provide correct input.")
    if answer != "off":
        input("Enter any key to continue.\n")
print("\nThank you for using the machine. See you next time.")