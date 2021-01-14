def mergeSort(alist):
    print("Splitting ", alist)
    if len(alist) > 1:
        # 拆分左半右半
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        # 递归归并排序
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i, j, k = 0, 0, 0
        # 拉链对比
        while i < len(lefthalf) and j < len(righthalf):
            # 左小，左数加入总表
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            # 右小，右数加入总表
            else:
                alist[k] = righthalf[j]
                j = j + 1
            # 判断完一次后，总表索引向后移一格
            k = k + 1
        # 右表比完之后，左表还有遗留，逐个加入总表
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1
        # 左表比完之后，右表还有遗留，逐个加入总表
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1
    print("Merging ", alist)


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    mergeSort(alist)
    print(alist)
