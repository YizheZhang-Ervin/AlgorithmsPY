def binary_search(lis, item):
    """
    def binary_search(lis, item):
        low = 0
        high = len(lis) - 1
        while low <= high:
            mid = (low + high) // 2
            guess = lis[mid]
            if guess == item:
                return mid
            if guess > item:
                high = mid - 1
            else:
                low = mid + 1
        return None
    """
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

