def main():
    expression = input("Enter your sum: ")
    expression_list = expression.split(" ")

    return calculator(expression_list)

def calculator(list_expression):

    x = float(list_expression[0])
    y = list_expression[1]
    z = float(list_expression[2])

    if y == "+":
        answer = x + z
        print(round(answer,2))
    elif y == "-":
        answer = x - z
        print(round(answer,2))
    elif y == "/":
        answer = x / z
        print(round(answer,2))
    elif y == "*":
        answer = x * z
        print(round(answer,2))
    else:
        print("Enter a valid expression,(e.g) 1 + 2")


main()