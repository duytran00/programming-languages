#Duy Tran
#1002190361
#3/25/2025
#ubuntu 24.04.2
#python 3.12.3

import os

def infixToRpn(infix):
    precedence = {"(": 0, "-": 1, "+": 1, "*": 2, "/": 2, "~": 3}  
    #~, unary subtraction
    
    processInfix = []

    #process to treat - as unary or binary subtraction
    for i in range(len(infix)):
        #three cases for unary subtraction: -, at beginning, after (, 
        # or after operator
        if (infix[i] == "-" and (i == 0 or infix[i-1] == "(" or infix[i-1] 
                                 in "+-*/")):
            processInfix.append("~")
        else:
            processInfix.append(infix[i])

    stack = []
    rpn = []

    for token in processInfix:
        if token.isdigit():
            rpn.append(token)

        elif token == "(":
            stack.append(token)
        elif token == ")":
            while stack and stack[-1] != "(":
                rpn.append(stack.pop())
            stack.pop()

        #operators
        else:
            while (stack and stack[-1] != "(" and precedence.get(token, 0) 
                   <= precedence.get(stack[-1], 0)):
                rpn.append(stack.pop())
            stack.append(token)

    while stack:
        rpn.append(stack.pop())

    return rpn

def main():
    currentDirectory = os.path.dirname(os.path.abspath(__file__))
    filePath = os.path.join(currentDirectory, "input_RPN_EC.txt")

    with open(filePath, "r") as file:
        lines = file.readlines()

    for line in lines:
        infix = line.strip().split()

        rpn = infixToRpn(infix)
        #space sperated
        print(" ".join(rpn))

        stack = []

        for token in rpn:
            if token.isdigit():
                stack.append(int(token))

            #unary subtraction
            elif token == '~':
                    if stack:
                        stack.append(-stack.pop())

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