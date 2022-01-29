qeueu = []


class PriorityQueue:
    def enqueue(self, size):
        if len(qeueu) == size:
            print("Queue is Full!!!")
        else:
            priority, element = map(int, input("Enter the priority and element separated by space: ").split(" "))
            qeueu.append((priority, element))
            qeueu.sort()

    def dequeue(self, ):
        if len(qeueu) == 0:
            print("Queue is empty!!!")
        else:
            print(qeueu.pop(0))

    def is_empty(self):
        if len(qeueu) == 0:
            print("queue is empty")
        else:
            print("queue is not empty")

    def is_full(self, size):
        if len(qeueu) == size:
            print("queue is full")
        else:
            print("queue is not Full")

    def peek(self):
        if len(qeueu) == 0:
            print("Stack is empty")
        else:
            print(qeueu[0])


queue1 = PriorityQueue()
n = int(input("Enter the size of Qeueu: "))
print("Enter the Operation:\n"
      "1 : Push\n"
      "2 : Pop\n"
      "3 : Peek\n"
      "4 : is_empty\n"
      "5 : is_full\n"
      "6 : Quit")
while True:
    choice = int(input("Enter the your Choice: "))
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
