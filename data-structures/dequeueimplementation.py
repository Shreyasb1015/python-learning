from dequeue import Deque

deque = Deque()
choice = 0

while choice != 5:
    print("\nDeque operations")
    print("1. Add to Front")
    print("2. Add to Rear")
    print("3. Remove from Front")
    print("4. Remove from Rear")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        deque.add_front()
    elif choice == 2:
        deque.add_rear()
    elif choice == 3:
        deque.remove_front()
    elif choice == 4:
        deque.remove_rear()
    elif choice == 5:
        break
