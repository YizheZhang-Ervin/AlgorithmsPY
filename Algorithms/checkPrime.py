from math import sqrt


def checkPrime(nums):
    """
    从2~sqrt(n)+1判断
    """
    ranges = range(2, int(sqrt(nums) + 1))
    for i in ranges:
        if nums % i == 0:
            return False
    return True


def checkPrime2(nums):
    """
    从2~sqrt(n)判断,只需要判断6x+1,6x+5
    """
    flag = True
    if nums == 2 or nums == 3:
        return flag
    if nums % 6 != 1 and nums % 6 != 5:
        flag = False
        return flag
    for i in range(5, int(sqrt(nums)) + 2, 6):
        if nums % i == 0 or nums % (i + 2) == 0:
            flag = False
            return flag
    return flag


if __name__ == '__main__':
    rst = checkPrime(3)
    rst2 = checkPrime2(3)
    print(rst, rst2)
