def sumArray(lis):
    """
    数组求和
    """
    if len(lis) == 1:
        return lis[0]
    else:
        return lis[0] + sumArray(lis[1:])


if __name__ == '__main__':
    rst = sumArray([1, 2, 3, 4, 5])
    print(rst)
