from DataStructure.stack import Stack


def expressionEvaluation(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        # 数字则压入栈
        if token in "0123456789":
            operandStack.push(int(token))
        # 非数字
        else:
            # 先出栈的是操作数2
            operand2 = operandStack.pop()
            # 后出栈的是操作数1
            operand1 = operandStack.pop()
            # 运算
            result = doMath(token, operand1, operand2)
            # 运算结果压入栈
            operandStack.push(result)
    return operandStack.pop()


def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


if __name__ == '__main__':
    print(expressionEvaluation('7 8 + 3 2 + /'))
