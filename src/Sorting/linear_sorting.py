# def counting_sort(arr, max_number):
#     counting_arr = [0] * (max_number + 1)
#     for i in arr:
#         counting_arr[i] += 1
#     j = 0
#     # only creates new values without copy
#     for i in range(max_number + 1):
#         for k in range(counting_arr[i]):
#             arr[j] = i
#             j += 1
#     return arr
#
#
# def radix_sort(arr, d):
#     for i in range(d):
#         counting_sort(arr, d)
import math


def radix_sort(array):
    max_len = -1
    for number in array: # Find longest number, in digits
        num_len = int(math.log10(number)) + 1
        if num_len > max_len:
            max_len = num_len
    buckets = [[] for i in range(0, 10)] # Buckets for each digit
    for digit in range(0, max_len):
        for number in array:
            buckets[number / 10**digit % 10].append(number)
        del array[:]
        for bucket in buckets:
            array.extend(bucket)
            del bucket[:]
    return array