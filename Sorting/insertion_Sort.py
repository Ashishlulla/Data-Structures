"""

     Insertion sort is a sorting algorithm that places an unsorted element at its suitable place in each iteration.
Insertion sort works similarly as we sort cards in our hand in a card game.We assume that the first card is already
sorted then, we select an unsorted card.
                   If the unsorted card is greater than the card in hand, it is placed on the right otherwise, to the left.
In the same way, other unsorted cards are taken and put in their right place. A similar approach is used by insertion sort.

Insertion Sort Complexity
Time Complexity	 :-     Best	: O(n)
                        Worst	: O(n2)
                       Average	: O(n2)
Space Complexity :- 	O(1)
Stability	     :-     Yes
"""


def insertion_sort(lst):
    for i in range(1, len(lst)):
        target = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > target:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = target
    return lst


print(insertion_sort([2, 4, 3, 1, 9, 7]))
