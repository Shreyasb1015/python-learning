from queuee import Queue

q=Queue()
choice=0
while choice <4:
    print("Queue operations")
    print("1.Enqueue")
    print("2.Dequeue")
    print("3.Search")
    print("4.Exit")

    choice=int(input("Enter your choice: "))
    if choice==1:
        q.enqueue()
    elif choice==2:
        q.dequeue()
    elif choice==3:
        q.search()
    elif choice==4:
        break
