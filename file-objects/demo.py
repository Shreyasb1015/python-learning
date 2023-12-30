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
    
# We can read line by line using readline method.At first ,it reads first line ,then it reads second line and so on.
with open('test.txt','r') as f:
    f_line=f.readline()
    print(f_line,end='')
    
    f_line=f.readline()
    print(f_line,end='')
    

# We can  read all the lines using for loop.
with open('test.txt','r') as f:
    
    for line in f:
        print(line,end='')
        

## We can also specify the number of characters to read from the file as argument in the read func. This helps us when file is too large.

with open('test.txt','r') as f:
    f_contents = f.read(100)
    print(f_contents,end='')
    

## We can actually read the large files in chunks by specifying no of characters to be read in one go.When the file has nothing left to read ,it returns null list.

with open('test.txt','r') as f:
    size_to_read=100
    f_contents = f.read(size_to_read)
    
    while len(f_contents)>0:
        print(f_contents,end='')
        f_contents=f.read(size_to_read)