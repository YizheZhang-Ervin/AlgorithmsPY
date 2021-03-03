def printFibonacci(n):
    """
    n为数列的数字个数
    斐波那契数列0,1,1,2,3,5,8,13,21...
    f(n)=f(n-1)+f(n-2)
    """
    lis = [0, 1]
    a, b = lis
    for i in range(n - 2):
        a, b = b, a + b
        lis.append(b)
    return lis


def printFibonacci2(n):
    """
    递归斐波那契数列
    """
    def recursion(n):
        if n == 0: return 0
        if n == 1: return 1
        return recursion(n - 1) + recursion(n - 2)

    lis = []
    for i in range(n):
        lis.append(recursion(i))
    return lis


if __name__ == '__main__':
    rst = printFibonacci(10)
    rst2 = printFibonacci2(10)
    print(rst, rst2)
