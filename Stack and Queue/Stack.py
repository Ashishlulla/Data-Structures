"""
A stack is a linear data structure that follows the principle of Last In First Out (LIFO).
This means the last element inserted inside the stack is removed first. You can think of the
stack data structure as the pile of plates on top of another.

There are some basic operations that allow us to perform different actions on a stack.
    1).Push: Add an element to the top of a stack
    2).Pop: Remove an element from the top of a stack
    3).IsEmpty: Check if the stack is empty
    4).IsFull: Check if the stack is full
    5).Peek: Get the value of the top element without removing it
"""
stack = []


def push(size):
    if len(stack) == size:
        print("Stack is Full!!!!")
    else:
        element = input("Enter the element: ")
        stack.append(element)
        print(stack)


def pop():
    if len(stack) == 0:
        print("Stack is Empty!!!")
    else:
        stack.pop()
        print(stack)


def is_empty():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Stack is not empty")


def is_full(size):
    if len(stack) == size:
        print("Stack is full")
    else:
        print("Stack is not Full")


def peek():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print(stack[-1])


n = int(input("Enter the Limit of the Stack : "))
print("Enter the Operation:\n"
      "1 : push\n"
      "2 : pop\n"
      "3 : is_empty\n"
      "4 : is_full\n"
      "5 : peek\n"
      "3 : Quit\n")
while True:
    choice = int(input())
    if choice == 1:
        push(n)
    elif choice == 2:
        pop()
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
