num1 = float(input("enter first number"))
num2 = float(input("enter second number"))
operator = input("enter operator (+,-,*,/):")

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 + num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1/num2)
else:
    print("invalid operator")