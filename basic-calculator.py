def calculator():
    print("Basic Calculator")
    print("Available operations: +, -, *, /")

    try:
        first_number = float(input("Enter the first number: "))
        operation = input("Choose an operation (+, -, *, /): ")
        second_number = float(input("Enter the second number: "))

        if operation == "+":
            result = first_number + second_number
        elif operation == "-":
            result = first_number - second_number
        elif operation == "*":
            result = first_number * second_number
        elif operation == "/":
            if second_number == 0:
                print("Error: You cannot divide by zero.")
                return
            result = first_number / second_number
        else:
            print("Error: Please choose +, -, *, or /.")
            return

        print(f"Result: {result}")

    except ValueError:
        print("Error: Please enter valid numbers.")


if __name__ == "__main__":
    calculator()