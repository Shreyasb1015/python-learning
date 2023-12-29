
#Importing necessary module
import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

##### We will be using raw strings so that python doesnt interfare with our code.
#### For e.g if we print('\tTab')  -->output -->  Tab
#### Now ,if we use raw strings , we will do  --> print(r'\tTab') -> Output \tTab

## To write our patterns that we want to search,we use re.compile method in the variable.

pattern=re.compile(r'abc')

# We use finditer( ) to find the ocurrence of pattern
matches=pattern.finditer(text_to_search)

for match in matches:
    print(match)
    

#To search any metacharacters, we need to escape the character by adding \ in front of it.

pattern=re.compile(r'\.')
matches=pattern.finditer(text_to_search)

for match in matches:
    print(match)
    
#To match any url which contains meta character like . , we need to specify it .

pattern=re.compile(r'coreyms\.com')
matches=pattern.finditer(text_to_search)

for match in matches:
    print(match)
    

# For matching digits , we use /d
pattern=re.compile(r'\d')
matches=pattern.finditer(text_to_search)

for match in matches:
    print(match)
    
## To match any character , i.e not a digits  ,we use \D
### To match any word character i.e digit or alphabets (bith lower and uppercase), we pass \w


#For matching whitespaces ,we use \s

pattern=re.compile(r'\s')
matches=pattern.finditer(text_to_search)

for match in matches:
    print(match)
    

#We use /b for matching word boundary specifying the word and /B to match not a word boundary.
pattern=re.compile(r'\bHa')
matches=pattern.finditer(text_to_search)

for match in matches:
    print(match)
    

#We use ^ to match beginning of string and  $ to match end of string
pattern=re.compile(r'^Start')
matches=pattern.finditer(sentence)

for match in matches:
    print(match)
    
#To match end of the string , we use  $ sign.
pattern=re.compile(r'end$')
matches=pattern.finditer(sentence)

for match in matches:
    print(match)
    

#Creating a pattern to match both phone numbers (one containing . and other -) in the text_to_search string.

pattern=re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
matches=pattern.finditer(text_to_search)

for match in matches:
    print(match)
    

## Now ,we will open the file data.txt which contains fake info and we will try to extract the phone nos in the file

with open('data.txt','r',encoding='utf-8') as f:
    contents=f.read()
   
    matches=pattern.finditer(contents)
    for match in matches:
       print(match)

#In the above  pattern , we have use . so it will macth al the characters .But if we want ot match only certain meta characters ,we shoudl use [].

pattern=re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
matches=pattern.finditer(text_to_search)

for match in matches:
    print(match)
    

#Similary , we use [^] ot match the characters which arent in bracket.

# To match the numbers which starts from 800 or 900

pattern=re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
matches=pattern.finditer(text_to_search)

for match in matches:
    print(match)
    
# Dash character is the special character , when put at start or end , it will only match literal -characters,but when used between numbers it finds the characters in that range.
# for e.g --> matchinh the digits between  1 and 5
#pattern=re.compile(r'[1-5]')

# For lower case letters matching --->
#pattern=re.compile(r'[a-z]')

#For both lower case and upper case matching
pattern=re.compile(r'[a-zA-Z]')

# If we use ^ character inside [], then it will act as not operator
#pattern=re.compile(r'[^a-zA-Z]')  -->  Only those characters which arent alphabets

matches=pattern.finditer(text_to_search)

for match in matches:
    print(match)

  