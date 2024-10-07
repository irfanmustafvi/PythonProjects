day_of_week = input("Enter the day of week: ")
# # day_of_week = input("Enter the day of week: ").lower()  # convert to lowercase
# # day_of_week = input("Enter the day of week: ").upper()  # convert to uppercase
# print(day_of_week)

#### Conditionals
if day_of_week == "friday" or day_of_week == "saturday":  # condition true
    print("I learn LIVE DevOPs/Python")
else:  # condition false
    print("I practice DevOps/Python")

num1 = int(
    input("Enter first number! ")
)  # str=> int type casting (conversion ont data type to another data type)
num2 = int(input("Enter second number! "))
choice = input("Enter the operation: (options +, -, *, /, %) ")

if choice == "+":
    sum_of_num = num1 + num2
    print("addition: ", sum_of_num)
elif choice == "-":
    diff_of_num = num1 - num2
    print("subtraction: ", diff_of_num)
elif choice == "*":
    prod_of_num = num1 * num2
    print("multiplication: ", prod_of_num)
elif choice == "/":
    div_of_num = num1 / num2
    print("division: ", div_of_num)
elif choice == "%":
    rem_of_num = num1 % num2
    print("remainder: ", rem_of_num)
else:
    print("invalid choice")
