#File Objects

## The method below is not recommended, because it is easy to forget to close the file.

f = open('test.txt', 'r')
#If we want to read and write the file , we can specify it using r+ or w+.

print(f.name)

#To check the mode of file , we can do -->
print(f.mode)


f.close()

#Recommended way to open a file is using the with statement.

with open('test.txt','r') as f:
    print(f.name)
    
