import urllib.request

try:
    file=urllib.request.urlopen('http://www.python.org/')
    content=file.read()
except urllib.error.HTTPError:  #type:ignore
    print("The webpage doesnt exist")
    exit()
f=open('myfile.html','wb')
f.write(content)
f.close()
