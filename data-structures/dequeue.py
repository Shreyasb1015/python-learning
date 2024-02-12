class Deque():
    def __init__(self):
        self.deque = []

    def add_front(self):
        ele = input("Enter the element to add at the front: ")
        self.deque.insert(0, ele)
        print(self.deque)

    def add_rear(self):
        ele = input("Enter the element to add at the rear: ")
        self.deque.append(ele)
        print(self.deque)

    def remove_front(self):
        try:
            self.deque.pop(0)
            print(self.deque)
        except IndexError:
            print("Deque is empty, cannot remove from front.")

    def remove_rear(self):
        try:
            self.deque.pop()
            print(self.deque)
        except IndexError:
            print("Deque is empty, cannot remove from rear.")

    def search(self):
        element = input("Enter the element to search: ")
        try:
            pos = self.deque.index(element)
            print(f"Element found at position {pos}.")
        except ValueError:
            print("Element not found in the deque.")


