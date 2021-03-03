from DataStructure.queue import Queue


def hotPotato(namelist, num):
    simqueue = Queue()
    # 全部加入队列
    for name in namelist:
        simqueue.enqueue(name)
    # 循环传递土豆，直到队列仅一个
    while simqueue.size() > 1:
        # 队首出，队尾进，循环num次
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        # 每隔num次，从队列出去一个
        simqueue.dequeue()
    # 返回最后一个人
    return simqueue.dequeue()


if __name__ == '__main__':
    print(hotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))
