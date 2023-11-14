
#pyttsx3 => Python Text to speech version 3
#pyttsx3 is the Python library that provides a simple interface to text-to-speech engines.
# It allows you to convert text into spoken words using different TTS (Text-to-Speech) engines.

import pyttsx3

#First step is to initliaze the TTS engine and load the driver object for your device .For e.g sapi5 for windows

engine = pyttsx3.init('sapi5')

#Next yo can get the current value of engine property like voices,rate,volume.

voices=engine.getProperty('voices')

#You can also set the value of engine property as per your choice.For this we use ,setProperty().
#It takes 2 arguments ,one is the name of property to be change, and second is the value that will set to that property.
#For e.g in sapi5 driver voices[0].id => male voice and voice[1].id => female voice , hence I can choose any one of them.

engine.setProperty('voice',voices[0].id)
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 0.7)  # Volume level (0.0 to 1.0) => only floating values

#Now to make the system speak your entered text we can use engine.say().
#It takes only one argument i.e text in the form of string.

engine.say('Hi!,I am Shreyas Bagwe. I love coding.')

#For smooth implementation of above speech ,we use a method called engine.runAndWait().
#This method wait for the speech to finish.

engine.runAndWait()

#After the above command is executed ,we can continue our program execution
