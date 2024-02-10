from stack import Stack

s=Stack()

num=int(input("Enter any number: "))

while(num !=0):
    s.push(num % 2)
    num=num // 2

print("Binary representation:")
s.reversestack()