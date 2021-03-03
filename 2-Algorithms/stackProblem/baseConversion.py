from DataStructure.stack import Stack


def baseConversion(nums, base):
    """
    迭代版 进制转换:10进制~任意(2-16)进制
    """
    if base not in range(2, 17):
        print('ERROR!Base can only in 2-16')
        return
    digits = '0123456789ABCDEF'
    s = Stack()
    n = nums
    rst = ''
    while n:
        q, r = divmod(n, base)
        # 余数压入栈
        s.push(r)
        # 商继续运算
        n = q
    # 出栈并映射到0~F
    for i in range(s.size()):
        rst += digits[s.pop()]
    return rst


def baseConversion2(nums, base):
    """
        递归版 进制转换:10进制~任意(2-16)进制
    """
    digits = '0123456789ABCDEF'
    if nums < base:
        return digits[nums]
    else:
        return baseConversion2(nums // base, base) + digits[nums % base]


if __name__ == '__main__':
    newnum = baseConversion(996, 16)
    newnum2 = baseConversion2(996, 16)
    print(newnum, newnum2)
