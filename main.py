
num1 = int(input())  
num2 = int(input())  

result = num1 + num2

print(result)

print("\nExtra Features: Choose an operation")
print("1. Subtract")
print("2. Multiply")
print("3. Divide")
print("4. Modulus")
print("5. Add three numbers")
print("6. Enter a full mathematical expression")
print("0. Exit")

choice = input("Enter your choice: ")

if choice == "1":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("Result:", num1 - num2)

elif choice == "2":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("Result:", num1 * num2)

elif choice == "3":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Cannot divide by zero!")

elif choice == "4":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("Result:", num1 % num2)

elif choice == "5":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))
    print("Result:", num1 + num2 + num3)

elif choice == "6":
    expression = input("Enter a mathematical expression (e.g., 2 + 4 - 3, 4 * 5 + 1 / 3): ")
    try:
        print("Result:", eval(expression))
    except:
        print("Error: Invalid expression!")

elif choice == "0":
    print("Goodbye!")

else:
    print("Invalid option, please try again.")

