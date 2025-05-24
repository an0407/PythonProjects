#Simple Calculator Program

flag = 1
while(flag == 1):
    operator = input("Choose an operator (+ - * /): ")
    num1 = float(input("Enter number1: "))
    num2 = float(input("Enter number2: "))

    if (operator == "+"):
        print(num1 + num2)
    elif (operator == "-"):
        print(num1 - num2)
    elif (operator == "*"):
        print(num1 * num2)
    elif (operator == "/"):
        print(num1 / num2)
    else:
        print("Operator not vaild")
    flag = int(input("Enter '1' to continue or '0' to exit : "))