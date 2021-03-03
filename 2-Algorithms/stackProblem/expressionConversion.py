from DataStructure.stack import Stack


def expressionConversion(infixexpr):
    prec = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        # 字符数字直接加入list
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        # 左括号压入栈
        elif token == '(':
            opStack.push(token)
        # 右括号
        elif token == ')':
            # 弹出栈顶符号
            topToken = opStack.pop()
            # 栈顶非左括号
            while topToken != '(':
                # 栈顶元素加入list
                postfixList.append(topToken)
                # 继续从栈顶拿出元素直到是左括号位置
                topToken = opStack.pop()
        # 运算符号
        else:
            # 栈顶运算符号优先级>当前运算符号，栈顶运算符号出栈并加入list
            while not opStack.isEmpty() and prec[opStack.peek()] >= prec[token]:
                postfixList.append(opStack.pop())
            # 当前运算符号加入栈
            opStack.push(token)
    # 栈不空则把栈剩下的全部加到list中
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)


if __name__ == '__main__':
    print(expressionConversion("A * B + C * D"))
    print(expressionConversion("( A + B ) * C - ( D - E ) * ( F + G )"))