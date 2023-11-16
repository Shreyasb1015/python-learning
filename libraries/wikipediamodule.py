
#Importing the library.

import wikipedia

#Summary of the title can be obtained using summary method.
#It takes 2 arguments,one is title to be searched and second is the no of sentences that we want.
#It returns the summary in string format.

summary=wikipedia.summary('Rohit Sharma',sentences=5)

print(summary)

#Titles and suggestions can be get using search().
#It takes 2 arguments ,i.e one is title to be searched and second is no of suggestions/result.
#It returns the list of titles.

result=wikipedia.search('Virat Kohli',results=5)
print(result)

#We can also change the language ,if page exists in the native language by using set_lang().
#It takes only one argument i.e language.
#For hindi ,we can pass 'hi' in the form of string.

wikipedia.set_lang('hi')

print(wikipedia.summary('Virat Kohli',sentences=5))