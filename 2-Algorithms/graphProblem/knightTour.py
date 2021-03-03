from DataStructure.graphs.graph import Graph, Vertex


def genLegalMoves(x, y, bdSize):
    newMoves = []
    moveOffsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
                   (1, -2), (1, 2), (2, -1), (2, 1)]
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX, bdSize) and legalCoord(newY, bdSize):
            newMoves.append((newX, newY))
    return newMoves


def legalCoord(x, bdSize):
    if 0 <= x < bdSize:
        return True
    else:
        return False


def knightGraph(bdSize):
    ktGraph = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = posToNodeId(row, col, bdSize)
            newPositions = genLegalMoves(row, col, bdSize)
            for e in newPositions:
                nid = posToNodeId(e[0], e[1], bdSize)
                ktGraph.addEdge(nodeId, nid)
    return ktGraph


def knightTour(n, path, u, limit):
    # n=层次，path=路径，u=当前节点，limit=搜索总深度
    u.setColor('gray')
    # 当前节点加入路径
    path.append(u)
    if n < limit:
        # 对所有合法移动逐一深入
        nbrList = list(u.getConnections())
        i = 0
        done = False
        while i < len(nbrList) and not done:
            # 深入未经过的顶点
            if nbrList[i].getColor() == 'white':
                # 层次加一，递归深入
                done = knightTour(n + 1, path, nbrList[i], limit)
            i = i + 1
        # 无法完成总深度，回溯，试本层下一个顶点
        if not done:  # prepare to backtrack
            path.pop()
            u.setColor('white')
    else:
        done = True
    return done


def posToNodeId(row, col, bdSize):
    return row * bdSize + col


# Warnsdorff改进
def orderByAvail(n):
    resList = []
    for v in n.getConnections():
        if v.getColor() == 'white':
            c = 0
            for w in v.getConnections():
                if w.getColor() == 'white':
                    c = c + 1
            resList.append((c, v))
    resList.sort(key=lambda x: x[0])
    return [y[1] for y in resList]


def knightTourBetter(n, path, u, limit):  # use order by available function
    u.setColor('gray')
    path.append(u)
    if n < limit:
        # 具有最少合法移动目标的格子优先搜索
        nbrList = orderByAvail(u)
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white':
                done = knightTour(n + 1, path, nbrList[i], limit)
            i = i + 1
        if not done:  # prepare to backtrack
            path.pop()
            u.setColor('white')
    else:
        done = True
    return done


if __name__ == '__main__':
    kg = knightGraph(5)  # five by five solution
    thepath = []
    start = kg.getVertex(4)
    knightTourBetter(0, thepath, start, 24)
    for v in thepath:
        print(v.getId())
