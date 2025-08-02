# calculator.py

def calculator():
    while True:
        print("\n🧮 Calculator Menu")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Back")

        choice = input("Choose an operation: ")

        if choice == '5':
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                result = num1 + num2
                print(f"Result: {result}")
            elif choice == '2':
                result = num1 - num2
                print(f"Result: {result}")
            elif choice == '3':
                result = num1 * num2
                print(f"Result: {result}")
            elif choice == '4':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    result = num1 / num2
                    print(f"Result: {result}")
            else:
                print("Invalid operation.")
        except ValueError:
            print("Invalid input. Please enter numbers.")
