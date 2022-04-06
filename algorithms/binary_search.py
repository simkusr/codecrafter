def binary_search(arr, val):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) / 2
        mid_val = arr[mid]
        if mid_val == val:
            return mid
        elif mid_val > val:
            start = mid + 1
        elif mid_val < val:
            end = mid -1
    return None


if __name__ == '__main__':
    arr = input("provide array: ")
    val = input("provide search val: ")

    res = binary_search(arr, val)
    print(res)

