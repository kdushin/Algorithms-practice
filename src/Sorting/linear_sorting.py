def counting_sort(arr, max_number):
    counting_arr = [0] * (max_number + 1)
    for i in arr:
        counting_arr[i] += 1
    j = 0
    # only creates new values without copy
    for i in range(max_number + 1):
        for k in range(counting_arr[i]):
            arr[j] = i
            j += 1
    return arr
