"""
  Linear search is one of the searching Algorithm . It is also called as
  sequential algorithm.
         It compares each and every element with the value that we are searching for.
  If both are matched, the element is found, and the algorithm returns the key's
  index position.

  Time Complexity : Worst Case -O(n),
                    Average Case - O(n)
                    Base Case - O(1)
"""


# Implementation of Linear Search

def linear_search(lst, tgt):
    for i in range(len(lst)):
        if lst[i] == target:
            return f"{lst[i]} is found at {i} positions"
        else:
            pass
    return f"{tgt} not in a array"


lst = [4, 2, 3, 10, 7, 9]
target = 9
print(linear_search(lst, target))
