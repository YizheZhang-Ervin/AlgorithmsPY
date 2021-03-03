from DataStructure.graphs.graph import Graph


class dfsgraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        # 颜色初始化
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        # 如果还有未包括的顶点则建森林
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)

    def dfsvisit(self, startVertex):
        startVertex.setColor('gray')
        # 算法的步数
        self.time += 1
        startVertex.setDiscovery(self.time)
        # 深度优先递归访问
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)
