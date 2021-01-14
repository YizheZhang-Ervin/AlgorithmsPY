from DataStructure.stack import Stack


def expressionCheck(exp):
    """
    括号匹配检查，不包含数字符号等
    """
    exp_dict = {'(': ')', '[': ']', '{': '}'}
    s = Stack()
    flag = True
    for i in exp:
        # 如果是左括号
        if i in '([{':
            s.push(i)
        # 如果是右括号
        else:
            # 栈空则说明不匹配
            if s.isEmpty():
                flag = False
                break
            # 栈不空看括号类型是否匹配
            else:
                top = s.pop()
                if not exp_dict[top] == i:
                    flag = False
                    break
    return flag and s.isEmpty()


if __name__ == '__main__':
    flag = expressionCheck('(([{}]))')
    print(flag)
