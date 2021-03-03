def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
    # 从1开始到change逐个计算最少硬币数
    for cents in range(change + 1):
        # 初始最大值
        coinCount = cents
        # 初始化新加硬币
        newCoin = 1
        # 循环各个面值
        for j in [c for c in coinValueList if c <= cents]:
            # 判断这个面值是否优于之前的结果(更少硬币)
            if minCoins[cents - j] + 1 < coinCount:
                # 记录当前这种配置的硬币数
                coinCount = minCoins[cents - j] + 1
                # 当前配置的硬币面值
                newCoin = j
        # 记录得到当前最少硬币数
        minCoins[cents] = coinCount
        # 本步骤加的硬币面值
        coinsUsed[cents] = newCoin
    # 返回最后一个结果
    return minCoins[change]


def printCoins(coinsUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin


if __name__ == '__main__':
    amnt = 63
    clist = [1, 5, 10, 21, 25]
    coinsUsed = [0] * (amnt + 1)
    coinCount = [0] * (amnt + 1)

    print("Making change for", amnt, "requires")
    print(dpMakeChange(clist, amnt, coinCount, coinsUsed), "coins")
    print("They are:")
    printCoins(coinsUsed, amnt)
    print("The used list is as follows:")
    print(coinsUsed)
