stack = []


class Stack:

    def push(self, size):
        if len(stack) == size:
            print("Stack is Full !!!")
        else:
            element = int(input("Enter the stack element: "))
            stack.append(element)
            print(stack)

    def pop(self):
        stack.pop()
        print(stack)

    def peek(self):
        if len(stack) == 0:
            print("Stack is Empty!!")
        else:
            print(stack[0])

    def is_empty(self):
        if len(stack) == 0:
            print("Stack is empty!!!")
        else:
            print("Stack is not Empty!!!")

    def is_full(self, size):
        if len(stack) == size:
            print("Stack is full!!!")
        else:
            print("Stack is not full!!!")


stck1 = Stack()
n = int(input("Enter the size of stack: "))
print("Enter the Operation:\n"
      "1 : Push\n"
      "2 : Pop\n"
      "3 : Peek\n"
      "4 : is_empty\n"
      "5 : is_full\n"
      "6 : Quit")
while True:
    choice = int(input())
    if choice == 1:
        stck1.push(n)
    elif choice == 2:
        stck1.pop()
    elif choice == 3:
        stck1.peek()
    elif choice == 4:
        stck1.is_empty()
    elif choice == 5:
        stck1.is_full(n)
    elif choice == 6:
        break
    else:
        print("Invalid Operation")
