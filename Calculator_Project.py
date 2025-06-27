logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

# from art import logo
# print(logo)
# # or
# import art
# print(art.logo)

# from replit import clear
# # you can use clear() to clear the console using replit

def add(n1, n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def mul(n1,n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

# You can store the function value inside a variable
# my_favorite_operation = add
# print(my_favorite_operation(2,3))

operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div,
}

# # We can do this in two ways
# # Below is done using function()

def calculator():
    print(logo)
    first_num = float(input("What's the first number?: "))

    result_as_first_num = True

    while result_as_first_num:

        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        second_num = float(input("What's the second number?: "))

        result = operations[operation_symbol](first_num,second_num)
        print(f"{first_num} {operation_symbol} {second_num} = {result}")

        while True:
            choice = input(f"Type 'Y' to continue calculating with {result}, or type 'N' to start a new calculation, or type 'EXIT' to exit the calculator: ").upper()

            if choice == "Y":
                first_num = result
                break
            elif choice == "N":
                result_as_first_num = False
                print("\n" * 25) # or we can also use this clear()
                calculator()
                break
            elif choice == "EXIT":
                result_as_first_num = False
                print("\n" * 25) # or we can also use this clear()
                print("THANK YOU FOR USING THE CALCULATOR! SEE YOU AGAIN")
                break
            else:
                print("\nInvalid choice! PLEASE TRY AGAIN\n".upper())

calculator()

# # or This is done using while loop both have the same logic

# loop = True
# while loop:
#     print(art.logo)
#     first_num = float(input("What's the first number?: "))
# 
#     result_as_first_num = True
# 
#     while result_as_first_num:
# 
#         for symbol in operations:
#             print(symbol)
#         operation_symbol = input("Pick an operation: ")
#         second_num = float(input("What's the second number?: "))
# 
#         result = operations[operation_symbol](first_num,second_num)
#         print(f"{first_num} {operation_symbol} {second_num} = {result}")
# 
#         while True:
#             choice = input(f"Type 'Y' to continue calculating with {result}, or type 'N' to start a new calculation, or type 'E' to exit the calculator: ").upper()
# 
#             if choice == "Y":
#                 first_num = result
#                 break
#             elif choice == "N":
#                 result_as_first_num = False
#                 print("\n" * 25) # or we can also use this clear()
#                 break
#             elif choice == "E":
#                 result_as_first_num = False
#                 loop = False
#                 print("\n" * 25) # or we can also use this clear()
#                 print("THANK YOU FOR USING THE CALCULATOR! SEE YOU AGAIN")
#                 break
#             else:
#                 print("\nInvalid choice! PLEASE TRY AGAIN\n".upper())
