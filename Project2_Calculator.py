## Parse Expression
### Arithmetic Operators
##1. / Division
##2. *
##3. +
##4. -
##5. ** Exponents always use with **
##6. % Modulus Symbol gives remainder after div
## B E D M A S
## (Time 1:16:15) Function is reusable block of code
expression = input("Type an expression: ")  # Always stored in str
result = 2 / 2  # outcome always float


## Functions
def get_number(number):
    while True:
        operand = input("Number " + str(number) + ": ")
        try:
            return float(operand)
        except:
            print("Invalid number, try again.")  # Output with str error


while True:
    operand2 = input("Number 2: ")  # Type str
    try:
        operand2 = float(operand2)
        break
    except:
        print("Invalid number, try again.")

operand = get_number(1)
operand2 = get_number(2)
sign = input("Sign: ")

print(operand, sign, operand2)
result = operand + operand2  # Used for simple number as str value not added
result = int(operand) + int(operand2)  # Used for int value  add numbers
result = float(operand) + float(operand2)  # Used for float value for decimal
print(result)
valid = False
try:
    operand = float(operand)
    operand2 = float(operand2)
    valid = True
except:
    print("Invalid operand")
if valid:

    result = 0
if sign == "+":
    result = operand + operand2
elif sign == "-":
    result = operand - operand2
elif sign == "/":
    if float(operand2) != 0:
        result = operand / operand2
    else:
        print("Division by zero")
elif sign == "*":
    result = operand * operand2
else:
    print("Invalid sign.")


print(result)

##While loop continue to run while condition is true
## while example is
i = 0
while i <= 10:  # i is less than or equal to 10
    print(i)
    i = i + 1  # Output count upto 0-9=10
    i += 2  # Output count with difference of 2, 4 6
    break  # immediate break and stop
    continue  # Infinite loop
    print("run")  # continue infinite loop
