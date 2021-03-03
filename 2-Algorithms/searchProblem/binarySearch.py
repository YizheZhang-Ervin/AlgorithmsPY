def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        # 中间值 = (头+尾)/2
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            # 目标值<中间值，在前部找
            if item < alist[midpoint]:
                last = midpoint - 1
            # 目标值>中间值，在后部找
            else:
                first = midpoint + 1

    return found


def binarySearch2(alist, item):
    """
    递归 二分查找
    """
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            # 目标值<中间值，在前部找
            if item < alist[midpoint]:
                return binarySearch2(alist[:midpoint], item)
            # 目标值>中间值，在后部找
            else:
                return binarySearch2(alist[midpoint + 1:], item)


if __name__ == '__main__':
    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
    print(binarySearch(testlist, 3))
    print(binarySearch(testlist, 13))
    print(binarySearch2(testlist, 3))
    print(binarySearch2(testlist, 13))
