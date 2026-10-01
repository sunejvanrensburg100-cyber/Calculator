import os

while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiply")
    print("4. Divide")
    print("5. Clear")
    print("6. Exit")
#These lines of code are the options available to the user for performing calculations. The user can choose to add, subtract, multiply, divide, or exit the calculator.

    choice = input("Enter choice (1/2/3/4/5/6): ")

    if choice == '5':
            os.system('cls' if os.name == 'nt' else 'clear')
            continue  
            # Clears the console screen
    elif choice == '6':
            print("Goodbye!")
            break
#The above lines of code check if the user has chosen to exit the calculator. If the user inputs '5', a message is displayed, and the loop breaks, ending the program.

    if choice in ['1', '2', '3', '4', '5', '6']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
#The above lines of code prompt the user to input two numbers for the selected operation. The input is converted to a float to allow for decimal calculations.
       
        if choice == '1':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
            #The numbers inputted by the user are added together, and the result is displayed in a formatted string.
        elif choice == '2':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
            #The numbers inputted by the user are subtracted, and the result is displayed in a formatted string.
        elif choice == '3':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
            #The numbers inputted by the user are multiplied, and the result is displayed in a formatted string.
        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
                #The numbers inputted by the user are divided, and the result is displayed in a formatted string. The code checks if the second number is not zero before performing the division to avoid division by zero errors.
            else:
                print("Error: Division by zero is not allowed.")
                #This line checks if the user is trying to divide by zero, which is not allowed in mathematics. If the second number is zero, an error message is displayed instead of performing the division.
        input("Press Enter to continue...")
    else:
        print("Invalid input. Please try again.")
        #This tells the user that their input was invalid and prompts them to try again. It ensures that the user selects a valid operation from the available options.
