import art

print("Welcome to my calculator!!")

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(art.logo)

    should_do = True
    num1 = float(input("What's the first number?: "))

    while should_do:
        # Display available operations
        for symbol in operation.keys():
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        
        # Validate operation symbol
        if operation_symbol not in operation:
            print("Invalid operation. Please try again.")
            continue

        num2 = float(input("What's the next number? "))

        # Handle division by zero
        if operation_symbol == "/" and num2 == 0:
            print("Division by zero is not allowed. Please try again.")
            continue

        # Perform the operation
        answer = operation[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # Ask if the user wants to continue
        want_to_continue = input(f"Type 'yes' to continue with {answer}, or 'no' to exit: ").lower()
        if want_to_continue == "yes":
            num1 = answer
        else:
            should_do = False
            print("Goodbye!")

calculator()
