from DataStructure.graphs.graph import Graph
from DataStructure.queue import Queue


def wordproc():
    f = open("rawwords.txt", "r")
    wl = []
    for aline in f:
        l = aline.split()
        wl.append(l[0])
    of = open("fourletterwords.txt", "w")
    for w in wl:
        of.write(w + '\n')


def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile, 'r')
    # create buckets of words that differ by one letter
    # 如果是4字母单词,属于4个桶
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i + 1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    # 给同一个桶的单词增加边和顶点
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)
    return g


# 广度优先遍历
def bfs(g, start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while vertQueue.size() > 0:
        # 队首作为当前顶点
        currentVert = vertQueue.dequeue()
        # 遍历邻接节点
        for nbr in currentVert.getConnections():
            if nbr.getColor() == 'white':
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')


# 回途追溯函数
def traverse(y):
    x = y
    while x.getPred():
        print(x.getId())
        x = x.getPred()
    print(x.getId())


if __name__ == '__main__':
    # 构建单词关系图
    wordgraph = buildGraph("fourletterwords.txt")
    # 广度优先搜索
    bfs(wordgraph, wordgraph.getVertex('FOOL'))
    # 遍历找词路径
    traverse(wordgraph.getVertex('SAGE'))
    # traverse(wordgraph.getVertex('COOL'))
