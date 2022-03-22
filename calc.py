#description
"""
Python Calculator
2022
Maira Quinones
A simple test python calculator
"""

#imports

#global variables

#functions
def print_menu():
    print("=============")
    print("PyCalc 3000")
    print("=============")

    print("[1] Sum")
    print("[2] Subtract")
    print("[3] Multiply")
    print("[4] Divide")
    print("[5] Repeat message")
#exercise for tomorrow
#ask for a message
# ask for the num times

#plain instructions

print_menu()
option = input("Please select an option: ")
# ! means NOT in an if statmnent
if option != "5":
    num1= float(input("num 1:"))
    num2= float(input("num 2:"))

if option == "1":
    #ask for the sum of two numbers and print
    print(num1 + num2)
    res = num1 + num2
    print(f"Result is: {res}")
 #else if the option is 2, ask for 2 number and show the result of num1 -num2
elif option == "2":
    res = num1 - num2
    print (f"Result is: {res}")

elif option == "3":
    res = num1 * num2
    print (f"Result is: {res}")

elif option == "4":
    if num2 == 0: 
        print("Cant divide")
    else:
        res = num1 / num2
        print (f"Result is: {res}")

elif option == "5":
    message = input("Provide message: ")
    times = int(input("How mant times "))

    for i in range(0, times):
        print (f"{message}")
