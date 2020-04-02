# find minimum
def findSmallest(arr):
    # minimum value
    smallest = arr[0]
    # minimum index
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest_index = i
            smallest = arr[i]
    return smallest_index


# Sort
def selection_sort(arr):
    """
    def findSmallest(arr):
        smallest = arr[0]
        smallest_index = 0
        for i in range(1, len(arr)):
            if arr[i] < smallest:
                smallest_index = i
                smallest = arr[i]
        return smallest_index

    def selection_sort(arr):
        newArr = []
        for i in range(len(arr)):
            smallest = findSmallest(arr)
            newArr.append(arr.pop(smallest))
        return newArr
    """
    newArr = []
    for i in range(len(arr)):
        # find minimum value and pop+append it to new list
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr
