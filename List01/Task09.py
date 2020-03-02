from math import sin, tan, cos


def cal():
    num1 = int(input("Number 1 --> "))
    sign = input("Sign --> ")
    num2 = 1
    if sign != 'sin' and sign != 'cos' and sign != 'tan':
        num2 = int(input("Last number --> "))

    if sign == "+" or sign == "-" or sign == "*" or sign == "/" or sign == "^":
        print("You want to calculate %s%s%s." % (num1, sign, num2))
    elif sign == 'sin' and sign == 'cos' and sign == 'tan':
        print("You want to calculate %s(%s)." % (sign, num1))

    if sign == "+":
        result = int(num1) + int(num2)
        print("The result is %s." % (result))

    elif sign == "-":
        result = int(num1) - int(num2)
        print("The result is %s." % (result))

    elif sign == "*":
        result = num1 * num2
        print("The result is %s." % (result))

    elif sign == "/":
        result = num1 / num2
        print("The result is %s." % (result))

    elif sign == "^":
        result = num1 ** num2
        print("The result is %s." % (result))

    elif sign == "%":
        result = num1 % num2
        print("The result is %s." % (result))

    elif sign == "sin":
        result = sin(num1)
        print("The result is %s." % (result))

    elif sign == "cos":
        result = cos(num1)
        print("The result is %s." % (result))

    elif sign == "tan":
        result = tan(num1)
        print("The result is %s." % (result))

    else:
        print("Something went wrong.")


cal()
