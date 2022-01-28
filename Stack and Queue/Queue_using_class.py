import collections

queue = collections.deque()


class Queue:

    def enqueue(self, size):
        if len(queue) == size:
            print("Queue is Full !!!")
        else:
            element = int(input("Enter the queue element: "))
            queue.append(element)
            print(queue)

    def dequeue(self):
        queue.popleft()
        print(queue)

    def peek(self):
        if len(queue) == 0:
            print("Stack is Empty!!")
        else:
            print(queue[0])

    def is_empty(self):
        if len(queue) == 0:
            print("queue is empty!!!")
        else:
            print("queue is not Empty!!!")

    def is_full(self, size):
        if len(queue) == size:
            print("queue is full!!!")
        else:
            print("queue is not full!!!")


queue1 = Queue()
n = int(input("Enter the size of Qeueu: "))
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
        queue1.enqueue(n)
    elif choice == 2:
        queue1.dequeue()
    elif choice == 3:
        queue1.peek()
    elif choice == 4:
        queue1.is_empty()
    elif choice == 5:
        queue1.is_full(n)
    elif choice == 6:
        break
    else:
        print("Invalid Operation")
