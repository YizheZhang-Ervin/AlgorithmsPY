from DataStructure.tree.priorityQueue import PriorityQueue


def dijkstra(aGraph, start):
    # 对所有顶点建堆，形成优先队列
    pq = PriorityQueue()
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(), v) for v in aGraph])
    while not pq.isEmpty():
        # 优先队列出队
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() + currentVert.getWeight(nextVert)
            # 修改出队顶点所邻接顶点的dist，并逐个重排队列
            if newDist < nextVert.getDistance():
                nextVert.setDistance(newDist)
                nextVert.setPred(currentVert)
                pq.decreaseKey(nextVert, newDist)
