from art import logo


# Calculator

# Add
def add(n1, n2):
    return n1 + n2


# Substract
def substract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    if n1 == 0:
        return 'Error'
    else:
        return n1 / n2


operations = {
    '+': add,
    '-': substract,
    '*': multiply,
    '/': divide,
}


def calculator():
    print(logo)

    condition = True
    num1 = float(input("\nWhat's the first number?: "))

    while condition:
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation = operations[operation_symbol]
        answer = calculation(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {round(answer)}")

        keep_calculating = input(
            f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation ")

        if keep_calculating == 'y':
            num1 = answer
            continue
        else:
            condition = False
            calculator()  # We call the function again, this is known as recursion.


calculator()
