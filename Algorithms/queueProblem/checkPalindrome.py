from DataStructure.deque import Deque


def palchecker(aString):
    stillEqual = True
    chardeque = Deque()

    # 把字符串一个个加入双端队列队末
    for ch in aString:
        chardeque.addRear(ch)

    # 双端队列大小>1且目前保持两端相等时
    while chardeque.size() > 1 and stillEqual:
        # 双端队列头弹出
        first = chardeque.removeFront()
        # 双端队列尾弹出
        last = chardeque.removeRear()
        # 判断是否头尾相等
        if first != last:
            stillEqual = False
    return stillEqual


if __name__ == '__main__':
    print(palchecker("lsdkjfskf"))
    print(palchecker("radar"))
