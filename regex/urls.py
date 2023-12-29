import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern=re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches=pattern.finditer(urls)

for match in matches:
    print(match)
    
#We can also extract the domain name using group attribute
matches=pattern.finditer(urls)
for match in matches:
     print(match.group(3))
     

### To substitute and get the new string whcih only conatisn domain name and .com we can use sub() and speicfy teh group name to be repalced.
subbed_urls=pattern.sub(r'\2\3', urls)
print(subbed_urls)