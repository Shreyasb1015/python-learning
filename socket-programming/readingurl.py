import urllib.request
file=urllib.request.urlopen('http://python.org/')
print(file.read())
