"""
    This is a one of the searching algorithm. There are many searching algorithms
    but the binary search is most popular among them.
    The elements in the list must be sorted to apply the binary search algorithm.
    If elements are not sorted then sort them first.

    Time Complexity : Base Case: 0(1)
                      Worst Case: 0(logn)

"""


# Implementation of Binary Search :
# 1.Recursive Method:

def binary_search(lst, left, right, tgt):
    mid = (left + right) // 2
    if left <= right:
        if lst[mid] == tgt:
            return f"Element {lst[mid]} is found at {mid + 1}"
        elif lst[mid] < tgt:
            return binary_search(lst, mid + 1, right, tgt)
        else:
            return binary_search(lst, left, mid - 1, tgt)
    else:
        return f"Element not found"


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(lst, 0, len(lst), 7))


# 2. Iterative Method :

def binary_search(lst, tgt):
    left, right = 0, len(lst)-1
    while left <= right:
        pivot = left + (right-left)//2
        if lst[pivot] == tgt:
            return pivot+1
        elif lst[pivot] < tgt:
            left = pivot + 1
        else:
            right = pivot - 1
    return -1


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(lst, 7))
