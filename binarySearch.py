def binary_search(lis, item):
    # search part
    low = 0
    high = len(lis) - 1
    # narrow scope
    while low <= high:
        mid = (low + high) // 2
        guess = lis[mid]
        # Found
        if guess == item:
            return mid
        # too high
        if guess > item:
            high = mid - 1
        # too low
        else:
            low = mid + 1
    # not exist
    return None

