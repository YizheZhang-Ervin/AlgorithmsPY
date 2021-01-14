def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        # 比较还未排序的余下的列表
        for i in range(passnum):
            # 整个列表所有数比较，最大的放最后
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp


def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist) - 1

    while passnum > 0 and exchanges:
        exchanges = False
        # 比较还未排序的余下的列表
        for i in range(passnum):
            # 整个列表所有数比较，最大的放最后
            if alist[i] > alist[i + 1]:
                # 如果所有数都<后一个，则说明已有序，不用继续比较
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp
        passnum = passnum - 1


if __name__ == '__main__':
    # 普通冒泡排序
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bubbleSort(alist)
    print(alist)
    # 优化版冒泡排序
    alist = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
    shortBubbleSort(alist)
    print(alist)
