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
        
## We can use tell method to tell the current position of the cursor in the file.
with open('test.txt','r') as f:
    size_to_read=100
    f_contents = f.read(size_to_read)
    print(f.tell())
    
# We can use f.seek() method to change the position of the cursor in the file.
#For e.g to set the cursor at starting -->

with open('test.txt','r') as f:
    size_to_read=10
    f_contents = f.read(size_to_read)
    print(f_contents,end='')
    
    f.seek(0)
    f_contents=f.read(size_to_read)
    print(f_contents)
    
#Now , lets look at writing to the file.

#While writing ,if file doesnt exists , it creates the file and if file exists alreadty , it overwrites the file.

with open('test1.txt','w') as f:
    f.write('Hi, I m Shreyas')
    
# We can also use here seek()) method to change the position of the cursor in the file and go to the beginning of the file.


#We can also copy the contents of one file to another file. For that we use double with statement.
## We copy each line in the rf file to wf file.

with open('test.txt','r') as rf:
    with open('test_copy.txt','w') as wf:
       for line in rf:
           wf.write(line)
           
# Now , lets look at copying the image file.
### To make a copy of image ,we should open the file in binary mode,i.e we should specify 'rb' and 'wb' as arguments in open method.

with open('pic1.jpg','rb') as rf:
    with open('pic1_copy.jpg','wb') as wf:
       for line in rf:
           wf.write(line)