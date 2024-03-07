import urllib.parse
url='https://mail.google.com/mail/u/0/#inbox'
tpl=urllib.parse.urlparse(url)
print(tpl)
print("scheme=",tpl.scheme)
print("Net location=",tpl.netloc)
print("Path=",tpl.path)
print("Parameters=",tpl.params)
print("Port numbers=",tpl.port)
print("Total url=",tpl.geturl())
