def calculator():
    print("Welcome to the Simple Calculator!")

    #Input wo numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    #Input operation choice
    print("Choose an operation:")
    print("1. Adddition (+)")
    print("2. Substraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter the operation (1/2/3/4): ")

    #Perform calculation based on user choice
    if choice == '1':
        result = num1 + num2
        operation = '+'
    elif choice == '2':
        result = num1 - num2
        operation = "-"
    elif choice == '3':
        result = num1 * num2
        operation = "*"
    elif choice == '4':
        if num2 != 0:
             result == num1 / num2
             operation = "/"
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Invalid operation choice."
    # Display the result 
    return f"The result of {num1} {operation} {num2} = {result}"

# Run the calculator
print(calculator())
        

