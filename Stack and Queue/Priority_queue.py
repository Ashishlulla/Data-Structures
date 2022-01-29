qeueu = []


def enqueue(size):
    if len(qeueu) == size:
        print("Queue is Full!!!")
    else:
        priority, element = map(int, input("Enter the priority and element separated by space: ").split(" "))
        qeueu.append((priority, element))
        qeueu.sort()


def deqeue():
    if len(qeueu) == 0:
        print("Qeueu is empty!!!")
    else:
        print(qeueu.pop(0))


def is_empty():
    if len(qeueu) == 0:
        print("queue is empty")
    else:
        print("queue is not empty")


def is_full(size):
    if len(qeueu) == size:
        print("queue is full")
    else:
        print("queue is not Full")


def peek():
    if len(qeueu) == 0:
        print("Stack is empty")
    else:
        print(qeueu[0])


n = int(input("Enter the Limit of the Queue : "))
print("Enter the Operation:\n"
      "1 : put\n"
      "2 : get\n"
      "3 : is_empty\n"
      "4 : is_full\n"
      "5 : peek\n"
      "3 : Quit\n")
while True:
    choice = int(input("Enter the your Choice: "))
    if choice == 1:
        enqueue(n)
    elif choice == 2:
        deqeue()
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


