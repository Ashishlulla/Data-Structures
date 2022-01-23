"""
Bubble sort is a sorting algorithm that compares two adjacent elements and swaps them until
 they are not in the intended order.

Just like the movement of air bubbles in the water that rise up to the surface, each element of
 the array move to the end in each iteration. Therefore, it is called a bubble sort.

Time Complexities:  Best :	    O(n)
                    Worst :	    O(n2)
                    Average : 	O(n2)
"""


def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
            else:
                pass
    return lst


print(bubble_sort([2, 4, 3, 1, 9, 7]))
