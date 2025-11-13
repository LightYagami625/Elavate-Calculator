print("---CALCULATOR---")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")
while True:
    num = int(input("Enter your choice: "))

    if num == 1:
        print("--ADDITION---")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result: ", a + b)
    elif num == 2:
        print("--SUBTRACTION---")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result: ", a - b)
    elif num == 3:
        print("--MULTIPLICATION---")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result: ", a * b)
    elif num == 4:
        print("--DIVISION---")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        if b != 0:
            print("Result: ", a / b)
        else:
            print("Error: Division by zero")
    elif num == 5:
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
    print("------------------")