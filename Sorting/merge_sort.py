"""
Merge Sort is one of the most popular sorting algorithms that is based on the principle of Divide and Conquer Algorithm.
Here, a problem is divided into multiple sub-problems. Each sub-problem is solved individually.
 Finally, sub-problems are combined to form the final solution.
 
 Time Complexity : 
          Best Case Complexity:        O(n*log n)
          Worst Case Complexity:       O(n*log n)
          Average Case Complexity:     O(n*log n)
Space Complexity : 
          The space complexity of merge sort is O(n).
"""


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_list(left, right, arr)


def merge_two_sorted_list(a, b, arr):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            a[k] = a[i]
            i += 1
        else:
            a[k] = b[j]
            j += 1
        k += 1
    while i < len_a:
        a[k] = a[i]
        i += 1
        k += 1
    while i < len_b:
        b[k] = b[j]
        j += 1
        k += 1


test_cases = [
    [10, 3, 15, 7, 8, 23, 98, 29],
    [],
    [3],
    [9, 8, 7, 2],
    [1, 2, 3, 4, 5]
]

for arr in test_cases:
    merge_sort(arr)
    print(arr)
