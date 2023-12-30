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
    

#To read the file, we can use the read method.

with open('test.txt','r') as f:
    f_contents = f.read()
    f_lines=f.readlines()
    f_firstLine=f.readline
    print(f_contents)
    print(f_lines)
    print(f_firstLine)
    
#To read the lines , we can use the readlines method.
#To read first line from the file, we can use the readline method.

with open('test.txt','r') as f:
   
    f_lines=f.readlines()
    f_firstLine=f.readline
    print(f_lines)
    print(f_firstLine)