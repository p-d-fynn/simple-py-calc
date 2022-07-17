# Simple Calculator

import time
numbers =[]


print("Welcome to the simple calculator application :)")
time.sleep(2)

print("\n")

print("Select an operation to perform")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("2.Divide")
time.sleep(2)

print("\n")
operation = input("Enter operation: ")
operation = int(operation)
total = 0

if operation == 1:
    print("How many numbers do you want to add")
    amount = input("Enter amount")
    amount = int(amount)

    for i in range (amount):
        num = int(input("Enter num: "))
        numbers.append(num)
        total = sum(numbers)
    print("The total is: ",total)

elif operation == 2:
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    total = num1 - num2
    print("The total is: ",total)

elif operation == 3:
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    total = num1 * num2
    print("The total is: ",total)

elif operation == 4:
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    total = num1 / num2
    print("The total is: ",total)

else:
    print("Invalid operation!")
