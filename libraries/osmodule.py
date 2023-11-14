import os
#Os module allows us to interact with  underlying operating system
#E.g task => navigate the file system,get file info,mpve files

#If you want to know all the attributes and methods of any module ,we can just do print(dir(os))

#To get the current working directory,we can do =>

print(os.getcwd())

#We can change the directory ,by using os.chdir() method.
#This method takes one argument i.e path of folder where we want our current directory.

os.chdir('C:/Users/bagwe/OneDrive/Documents')
print(os.getcwd())

os.chdir('C:/code-files')
print(os.getcwd())

#To get the list of folders in the specific directory,we can use os.listdir().
#It takes one argument i.e path of directory, if not passed ,it lists folders of current working directory

print(os.listdir('C:/code-files'))

#To create new folder in the specific directory,we can use os.mkdir().We need to pass the name of folder as argument.
# os.mkdir('os-tutorials')
#To create more layers in your folder,i.e creating files in the directory,we can use os.makedirs().
#It takes one argument,where we need to spcify the path of folder as we want.For e.g => os.makedirs(C:\desktop\os-tutorials)

os.makedirs('C:/code-files/os-tutorials')
print(os.listdir('C:/code-files'))

#To delete the folder,we can use os.rmdir().It takes the name of directory to be removed
#To delete the specific folder of any  bigger folder,we can use os.removedirs().It takes one argument,i.e path of file.

os.removedirs('C:/code-files/os-tutorials')

#To rename the file ,we can use os.rename().It takes two arguments i.e current name of file, and second is the name that we want to give the file.
os.rename('test.c','test1.c')

#To print out the contents of text file, we can use os.stat().It takes one argument i.e name of file.
#To get the environment variable of home directory,we can use os.environ.get().We need to pass the enviornment variable HOME in it.

print(os.environ.get('HOME'))

#To check if there exists a true path or not  ,we can use os.path.exists() .You will pass one argument ,i.e path of file=>
print(os.path.exists('home.txt'))

#To check if any folder is directory or not, we can use os.path.isdir().You will pass one argument ,i.e path of folder =>

print(os.path.isdir('C:/code-files/python-learning'))

#To check if any any given file is valid existing file or not, we can use os.path.isfile().You will pass one argument ,i.e path of file =>
print(os.path.isfile('C:/code-files/python-learning/libraries/osmodule.py'))

#To split the filename and its extension ,we can use os.path.splitext().You will pass one argument ,i.e path of file=>
print(os.path.split('C:/code-files/python-learning/libraries/osmodule.py'))






