def hanoiTower(n):
    """
    开始柱->中间柱->目标柱
    """
    steps = []

    def move(n, A, B, C):
        """
        A:fromPlace(开始柱)
        B:withPlace(中间柱)
        C:toPlace(目标柱)
        """
        if n >= 1:
            # 开始柱移到中间柱
            move(n - 1, A, C, B)
            # 记录移动步骤
            steps.append(f'{A}->{C}')
            # 中间柱移到目标柱
            move(n - 1, B, A, C)

    move(n, '#1', '#2', '#3')
    return steps


if __name__ == '__main__':
    rst = hanoiTower(3)
    print(rst)
