
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

