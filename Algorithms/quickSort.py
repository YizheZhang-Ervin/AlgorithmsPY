def quick_sort(array):
    """
    def quick_sort(array):
        if len(array) < 2:
            return array
        else:
            pivot = array[0]
            less = [i for i in array[1:] if i <= pivot]
            greater = [i for i in array[1:] if i > pivot]
            return quick_sort(less) + [pivot] + quick_sort(greater)
    """
    if len(array) < 2:
        # base case: array with 0 or 1 element
        return array
    else:
        # recursive case
        pivot = array[0]
        # sub-array: elements less than the pivot
        less = [i for i in array[1:] if i <= pivot]
        # sub-array: elements greater than the pivot
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

