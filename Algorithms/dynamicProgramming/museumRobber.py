def museumRobber(treasure, maxbag):
    # 初始化各种商品重量组合的最大价值
    m = {(i, w): 0 for i in range(len(treasure)) for w in range(maxbag + 1)}

    for i in range(1, len(treasure)):
        for w in range(1, maxbag + 1):
            # 装不下第i个商品
            if treasure[i]['w'] > w:
                # 不装第i个
                m[(i, w)] = m[(i - 1, w)]
            # 装得下第i个
            else:
                # 判断不装第i和装第i个哪种价值更大
                m[(i, w)] = max(m[(i - 1, w)],
                                m[(i - 1, w - treasure[i]['w'])] + treasure[i]['v'])
    return m


m = {}


def museumRobber2(tr, w):
    """
    迭代方法
    """
    if tr == set() or w == 0:
        m[(tuple(tr), w)] = 0
        return 0
    elif (tuple(tr), w) in m:
        return m[(tuple(tr), w)]
    else:
        vmax = 0
        for t in tr:
            if t[0] <= w:
                # 逐个从集合中去掉某个商品，递归调用选出所有价值中最大值
                v = museumRobber2(tr - {t}, w - t[0]) + t[1]
                vmax = max(vmax, v)
        m[(tuple(tr), w)] = vmax
        return vmax


if __name__ == '__main__':
    # 方法1调用
    tr = [None, {'w': 2, 'v': 3}, {'w': 3, 'v': 4},
          {'w': 4, 'v': 8}, {'w': 5, 'v': 8}, {'w': 9, 'v': 10}]
    max_bagweight = 20
    rst = museumRobber(tr, max_bagweight)
    print(rst[(len(tr) - 1, max_bagweight)])

    # 方法2调用
    tr2 = {(2, 3), (3, 4), (4, 8), (5, 8), (9, 10)}
    rst2 = museumRobber2(tr2, max_bagweight)
    print(rst2)
