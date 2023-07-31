import re

prior = {
    "*":1,
    "/":1,
    "+":0,
    "-":0
}

operators = {
    "*": lambda a, b : a * b,
    "/": lambda a, b : a / b,
    "+": lambda a, b : a + b,
    "-": lambda a, b : a - b
}

def calculate(expression: str):
    notation = createNotation(expression)
    stack = []
    while len(notation) > 0:
        el = notation[0]
        del notation[0]
        if type(el) == int:
            stack.append(el)
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(operators[el](op1, op2))
    return stack[0]

def createNotation(expression: str):
    stack = []
    notation = []
    while len(expression) > 0:
        match = re.search("^[\d\.]+", expression)
        if match:
            el = int(match.group())
            expression = expression[len(match.group()):len(expression)]
        else:
            el = expression[0]
            expression = expression[1:len(expression)]

        if type(el) == int:
            notation.append(el)
        elif el == "(":
            stack.append(el)
        elif el == ")":
            while stack[-1] != "(":
                notation.append(stack.pop())
            stack.pop()
        else: 
            while len(stack) > 0 and stack[-1] in prior and prior[stack[-1]] >= prior[el]:
                notation.append(stack.pop())
            stack.append(el)

    while len(stack) > 0:
        notation.append(stack.pop())
    return notation

