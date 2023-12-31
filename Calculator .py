def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Cannot divide by zero"

def calculator():
    print("Welcome to the calculator!")

    while True:
        print("\nPlease select an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            break

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == '1':
                result = add(num1, num2)
                print("Result: ", result)
            elif choice == '2':
                result = subtract(num1, num2)
                print("Result: ", result)
            elif choice == '3':
                result = multiply(num1, num2)
                print("Result: ", result)
            elif choice == '4':
                result = divide(num1, num2)
                print("Result: ", result)

        else:
            print("Invalid choice. Please try again!")

    print("Thank you for using the calculator!")

calculator()
