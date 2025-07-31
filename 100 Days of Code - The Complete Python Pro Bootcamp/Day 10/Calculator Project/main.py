import art
print(art.logo)
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

setups = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# print(setups["*"](7, 2))
calculation = False
first_num_condition = True
toyo_check = int(0)


while not calculation:
    if not first_num_condition:
        first_number = toyo_check
    else:
        first_number = int(input("What is the your first number?:"))
    operator_choice = input("+\n-\n*\n/\nChoose a mathematical operator:")
    second_number = int(input("What is the your second number?:"))
    toyo_check = 0


    if operator_choice == "+":
        ty = setups["+"](first_number, second_number)
        toyo_check += ty
        print(toyo_check)
    elif operator_choice == "-":
        ty_2 = setups["-"](first_number, second_number)
        toyo_check += ty_2
        print(toyo_check)
    elif operator_choice == "*":
        ty_3 = setups["*"](first_number, second_number)
        toyo_check += ty_3
        print(toyo_check)
    elif operator_choice == "/":
        ty_4 = setups["/"](first_number, second_number)
        toyo_check += ty_4
        print(toyo_check)
    else:
        print("You've entered a wrong operator.")

    to_continue = input(f"Do you want to continue working with {toyo_check}? Choose 'Yes' or 'No'\n").lower()
    if to_continue == "yes":
        first_num_condition = False
    elif to_continue == "no":
        first_num_condition = True

