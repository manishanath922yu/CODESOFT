def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def main():
    print("Simple Calculator")
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    while True:
        try:
            # Get user input
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            print("Choose an operation:")
            operation = input("Enter +, -, *, or /: ")

            # Perform calculation based on user choice
            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)
            else:
                print("Invalid operation. Please choose +, -, *, or /.")
                continue

            # Display the result
            print(f"The result of {num1} {operation} {num2} is: {result}")

        except ValueError:
            print("Invalid input. Please enter numeric values.")

        # Ask if the user wants to perform another calculation
        play_again = input("Do you want to perform another calculation? (yes/no): ").lower()
        if play_again != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def main():
    print("Simple Calculator")
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    while True:
        try:
            # Get user input
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            print("Choose an operation:")
            operation = input("Enter +, -, *, or /: ")

            # Perform calculation based on user choice
            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)
            else:
                print("Invalid operation. Please choose +, -, *, or /.")
                continue

            # Display the result
            print(f"The result of {num1} {operation} {num2} is: {result}")

        except ValueError:
            print("Invalid input. Please enter numeric values.")

        # Ask if the user wants to perform another calculation
        play_again = input("Do you want to perform another calculation? (yes/no): ").lower()
        if play_again != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
