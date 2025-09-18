
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice: ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print("addition:", num1 + num2)

elif choice == '2':
    print("subtraction:", num1 - num2)

elif choice == '3':
    print("multiplication:", num1*num2)

elif choice == '4':
    if num2 == 0:
        print("undefined")
    else:
        print("division:", num1/num2)

else:
    print("Invalid Input")
