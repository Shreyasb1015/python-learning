from linkedlist import LinkedList

choice=0
l=LinkedList()

while choice<5:
    print("linked list operations")
    print("1.add element")
    print("2.remove element")
    print("3.replace element")
    print("4.search element")
    print("5.exit")
    
    choice=int(input("enter your choice "))
    
    if choice==1:
        l.add()
    elif choice==2:
       l.remove()
    elif choice==3:
        l.replace()
    elif choice==4:
        l.search()
    elif choice ==5:
        break
