from binarySearch import binary_search
from quickSort import quick_sort
from selectionSort import selection_sort
from time import perf_counter


def run(ord_list, mess_list, elem, elem_x):
    time_list = []
    mess_list_copy = mess_list[:]

    # binary search = low<high -> middle
    bs1_t1 = perf_counter()
    bs1 = binary_search(ord_list, elem)  # 3
    bs1_t2 = perf_counter()
    bs1_delta = bs1_t2 - bs1_t1
    time_list.append(['binary search', bs1_delta])

    bs2_t1 = perf_counter()
    bs2 = binary_search(ord_list, elem_x)  # None
    bs2_t2 = perf_counter()
    bs2_delta = bs2_t2 - bs2_t1
    time_list.append(['binary search2', bs2_delta])

    # selection sort = find minimum -> save in list
    ss_t1 = perf_counter()
    ss = selection_sort(mess_list)
    ss_t2 = perf_counter()
    ss_delta = ss_t2 - ss_t1
    time_list.append(['selection sort', ss_delta])

    # quick sort = pivot ->iterate subsmall+subgreat
    qs_t1 = perf_counter()
    qs = quick_sort(mess_list_copy)
    qs_t2 = perf_counter()
    qs_delta = qs_t2 - qs_t1
    time_list.append(['quick sort', qs_delta])

    # sort time
    print("Time Rank-------------------------------------")
    print(*sorted(time_list, key=lambda x: x[1]), sep='\n')

    # results output
    print("result----------------------------------------")
    print('Binary Search1: {:^20},time: {:.2}'.format(bs1, bs1_delta))
    print('Binary Search2: {:^20},time: {:.2}'.format(str(bs2), bs2_delta))
    print('Selection Sort: {:^20},time: {:.2}'.format(str(ss), ss_delta))
    print('Quick     Sort: {:^20},time: {:.2}'.format(str(qs), qs_delta))


if __name__ == '__main__':
    ord_lis = [1, 3, 5, 7, 9]
    mess_lis = [4, 1, 3, 5, 2, 6]
    ele = 3
    ele_x = -1
    run(ord_lis, mess_lis, ele, ele_x)
