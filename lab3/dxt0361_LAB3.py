#Duy Tran
#1002190361
#3/25/2025
#ubuntu 24.04.2
#python 3.12.3

import os

def main():
    currentDirectory = os.path.dirname(os.path.abspath(__file__))
    filePath = os.path.join(currentDirectory, "input_RPN.txt")

    with open(filePath, "r") as file:
        lines = file.readlines()

    for line in lines:
        rpn = line.strip().split()
        stack = []

        for token in rpn:
            if token.isdigit():
                stack.append(int(token))

            else:
                b = stack.pop()
                a = stack.pop()
                
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    stack.append(a / b)

        print(stack[0])

if __name__ == '__main__':
    main()