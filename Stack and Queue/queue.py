"""
A queue is a useful data structure in programming. It is similar to the ticket queue outside a cinema hall,
 where the first person entering the queue is the first person who gets the ticket.
Queue follows the First In First Out (FIFO) rule - the item that goes in first is the item that comes out first.

In programming terms, putting items in the queue is called enqueue, and removing items from the queue is called dequeue.

Basic Operations of Queue :
    A queue is an object (an abstract data structure - ADT) that allows the following operations:
        Enqueue: Add an element to the end of the queue
        Dequeue: Remove an element from the front of the queue
        IsEmpty: Check if the queue is empty
        IsFull: Check if the queue is full
        Peek: Get the value of the front of the queue without removing it

"""


import collections

queue = collections.deque()


def enqueue(size):
    if len(queue) == size:
        print("Queue is Full!!!")
    else:
        element = int(input("Enter the element: "))
        queue.appendleft(element)


def dequeue():
    if len(queue) == 0:
        print("queue is Empty!!!")
    else:
        queue.pop()
        print(queue)


def is_empty():
    if len(queue) == 0:
        print("queue is empty")
    else:
        print("queue is not empty")


def is_full(size):
    if len(queue) == size:
        print("queue is full")
    else:
        print("queue is not Full")


def peek():
    if len(queue) == 0:
        print("Stack is empty")
    else:
        print(queue[-1])


n = int(input("Enter the Limit of the Queue : "))
print("Enter the Operation:\n"
      "1 : put\n"
      "2 : get\n"
      "3 : is_empty\n"
      "4 : is_full\n"
      "5 : peek\n"
      "3 : Quit\n")
while True:
    choice = int(input())
    if choice == 1:
        enqueue(n)
    elif choice == 2:
        dequeue()
    elif choice == 3:
        is_empty()
    elif choice == 4:
        is_full(n)
    elif choice == 5:
        peek()
    elif choice == 6:
        break
    else:
        print("Invalid Operation !!!!!")
