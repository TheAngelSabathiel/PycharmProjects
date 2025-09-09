import art

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

print(art.logo)
operation = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

should_continue = "n"
while should_continue == "n":
    first_number = float(input("Type the first number: "))
    should_continue = "y"
    while should_continue == "y":
        ops = input("Type the operator: ")
        second_number = float(input("Type the next number: "))
        if ops in operation:
            calc = operation[ops](first_number,second_number)
            print(f"{first_number} {ops} {second_number} = {calc}")
            should_continue = input(f"Type 'y' to continue calculation with {calc} or 'n' to start over: ").lower()
        else:
            print("Wrong operation. Try again.")
            input("Type any key to restart the calculator.")
            should_continue = "n"
        if should_continue == "n":
            print("\n" * 100)
            print(art.logo)
print("Wrong input. Try again.")