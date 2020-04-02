from Algorithms.binarySearch import binary_search
from Algorithms.quickSort import quick_sort
from Algorithms.selectionSort import selection_sort
from time import perf_counter


def run(alg=None, ord_list=None, mess_list=None, elem=None):
    if alg == 'BinarySearch':
        # binary search = low<high -> middle
        bs_t1 = perf_counter()
        bs = binary_search(ord_list, elem)  # 3
        bs_t2 = perf_counter()
        bs_delta = bs_t2 - bs_t1
        return bs, bs_delta, binary_search.__doc__

    elif alg == 'SelectionSort':
        # selection sort = find minimum -> save in list
        ss_t1 = perf_counter()
        ss = selection_sort(mess_list)
        ss_t2 = perf_counter()
        ss_delta = ss_t2 - ss_t1
        return ss, ss_delta, selection_sort.__doc__

    elif alg == 'QuickSort':
        # quick sort = pivot ->recur subsmall+subgreat
        qs_t1 = perf_counter()
        qs = quick_sort(mess_list)
        qs_t2 = perf_counter()
        qs_delta = qs_t2 - qs_t1
        return qs, qs_delta, quick_sort.__doc__

    # # sort time
    # print("Time Rank-------------------------------------")
    # print(*sorted(time_list, key=lambda x: x[1]), sep='\n')

    # results output
    # print("result----------------------------------------")
    # print('Binary Search1: {:^20},time: {:.2}'.format(bs1, bs1_delta))
    # print('Binary Search2: {:^20},time: {:.2}'.format(str(bs2), bs2_delta))
    # print('Selection Sort: {:^20},time: {:.2}'.format(str(ss), ss_delta))
    # print('Quick     Sort: {:^20},time: {:.2}'.format(str(qs), qs_delta))


if __name__ == '__main__':
    ord_lis = [1, 3, 5, 7, 9]
    mess_lis = [4, 1, 3, 5, 2, 6]
    ele = 3
    # ele = -1
    run(ord_lis, mess_lis, ele)
