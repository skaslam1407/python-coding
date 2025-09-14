# # Basic Calculator

# n1 = input("Enter 1st number: ")
# n2 = input("Enter 2nd number: ")
# opt = input("Operation Type Like + , - , / , * : ")

# # Validate numbers
# if not n1.isdigit() or not n2.isdigit():
#     print("❌ Please enter numbers only!")
# else:
#     n1 = int(n1)
#     n2 = int(n2)

#     if opt == '+':
#         print(f"Addition of {n1} and {n2} = {n1+n2}")
#     elif opt == '-':
#         print(f"Subtraction of {n1} and {n2} = {n1-n2}")
#     elif opt == '*':
#         print(f"Multiplication of {n1} and {n2} = {n1*n2}")
#     elif opt == '/':
#         if n2 != 0:
#             print(f"Division of {n1} and {n2} = {n1/n2}")
#         else:
#             print("❌ Cannot divide by zero!")
#     else:
#         print("❌ Invalid operation selected!")

# Basic Calculator with try/except

try:
    n1 = float(input("Enter 1st number: "))
    n2 = float(input("Enter 2nd number: "))
    opt = input("Operation Type Like + , - , / , * : ")

    if opt == '+':
        print(f"Addition of {n1} and {n2} = {n1+n2}")
    elif opt == '-':
        print(f"Subtraction of {n1} and {n2} = {n1-n2}")
    elif opt == '*':
        print(f"Multiplication of {n1} and {n2} = {n1*n2}")
    elif opt == '/':
        print(f"Division of {n1} and {n2} = {n1/n2}")
    else:
        print("❌ Invalid operation selected!")

except ValueError:
    print("❌ Please enter numbers only!")

except ZeroDivisionError:
    print("❌ Cannot divide by zero!")

except Exception as e:
    print("⚠️ Something went wrong:", e)

