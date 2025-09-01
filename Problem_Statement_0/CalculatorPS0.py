expression = input("> ")
# To remove confusion of any spacebars
expression = expression.replace(' ','') 
operators = ('+', '-', '*', '/', '^')
oprt = ''
op = False
e = 2.718281828
# Defining a ln fucntion
def ln(y):
    result = 1
    for i in range(1000000):
        result = result - (e**result-y)/e**result
    return result
# To check which mathematical operator is used
for o in operators:
    if o in expression:
        op = True
        oprt = o
# To check for natural logarithm
if expression.startswith('ln'):
    y = float(expression[3:-1])
    result = ln(y)
    print(result)
# To check for log10
elif expression.startswith('log10'):
    y = float(expression[6:-1])
    result = ln(y)/ln(10)
    print(result)
# To check for exponentials
elif expression.startswith('exp'):
    result = e**float(expression[4:-1])
    print(result)
# To check for sqrt 
elif expression.startswith('sqrt('):
    result = float(expression[5:-1])**0.5
    print(result)
# To check for basic mathematical operations
elif op:
    li = expression.split(oprt)
    num1 = float(li[0])
    num2 = float(li[1])
    if oprt == '+':
        result = num1 + num2
    if oprt == '-':
        result = num1 - num2
    if oprt == '*':
        result = num1*num2
    if oprt == '/':
        result = num1/num2
    if oprt == '^':
        result = num1**num2
    print(result)
else:
    print("Invalid expression!")


