num1 = int(input("input number 1:"))
num2 = int(input("input number 2:"))
op = input("input an operator:")

if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1 + num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(abs(num1 / num2))
else:
    print("invalid operator")