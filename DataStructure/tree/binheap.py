# 优先队列/二叉堆(用完全二叉树近似实现)


class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    # 节点上浮
    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    # 节点插入
    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    # 节点下降
    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    # 获取某节点最小子节点
    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    # 移走根节点
    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    # 无序表生成堆
    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1


if __name__ == '__main__':
    # test 1
    bh = BinHeap()
    bh.buildHeap([9, 5, 6, 2, 3])
    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())
    # test 2
    bh = BinHeap()
    bh.insert(5)
    bh.insert(7)
    bh.insert(3)
    bh.insert(11)
    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())