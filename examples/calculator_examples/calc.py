from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation (or type 'q' to quit): ")
        
        if operation_symbol == "q":
            print("Goodbye!")
            should_continue = False
            break

        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        next_step = input(
            f"Type 'y' to continue calculating with {answer}, 'n' to start a new calculation, or 'q' to quit: "
        )
        if next_step == "y":
            num1 = answer
        elif next_step == "n":
            should_continue = False
            calculator()
        elif next_step == "q":
            print("Goodbye!")
            should_continue = False
        else:
            print("Invalid input. Exiting.")
            should_continue = False


calculator()
