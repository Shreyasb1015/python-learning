#Python pyautogui library is an automation library that allows mouse and keyboard control.
#We can move the mouse and click in the other applications' window.
#We can send the keystrokes to the other applications. For example - filling out the form, typing the search query to browser, etc.
#We can also take snapshots and give an image.
#It allows us to locate a window of the application, and move, maximize, minimize, resizes, or close it.
#Display alert and message boxes.

import pyautogui

#We can get the screenwidth and screenheight using pyautogui.size()

screenWidth,screenHeight=pyautogui.size()
print('ScreenWidth :',screenWidth)
print('ScreenHeight :',screenHeight)

#To get the x and y co-ordinate of the mouse,we can use pyautogui.position().It return x and y co-ordinate of mouse
mouseX,mouseY=pyautogui.position()
print(mouseX,mouseY)

#Mouse functions =>

#To move the mouse to the specific x,y co-ordinate,we use pyautogui.moveTo().
#It takes 3 parameters i.e x,y co-ordinate and the duration. The cursor moves to specified co-ordinates in the given duration.

pyautogui.moveTo(200,150,duration=5)

#To move the mouse to relative to the x,y co-ordinate of current position of mouse,we can use moveRel().It takes the x-y coordinate and duration.
pyautogui.moveRel(100, 100, 3)

#We can also make our mouse to click use click().
#It can at most takes 5 arguments => x,y co-ordinate to be reached,no of clicks when cursor move to screen,interval between each mouse click in seconds,any  button that we want to click rather than mouse click

pyautogui.click(200,250)

#As a shortcut to the no of clicks, we have pyautogui.doubleclick(),pyautogui.tripleclick().This func performs double click of left button.
#To perform double click of right button we use rightClick().

pyautogui.doubleClick(300,350)

#To scroll the mouse, we can use pyautogui.scroll().It takes one argument.i.e no of clicks to scroll an optional two arguments that is xand y co-ordinate.
#If we pass 10 as argument,it scroll till 10 clicks.
#Positive no of scrolls represent to scroll in upwards direction and negative no of scrolls represent to scroll in downward direction.


pyautogui.scroll(-400)

#KeyBoard Operations =>
#The typewrite() function is used to write the something in a text field.It takes 2 arguments ,i.e text to be written and duration in which it should be wrriten.

pyautogui.typewrite('Shreyas Bagwe',2)

#we use the hotkey() function that helps us to press two or more keys at same time.It takes the name of keys as argument.
pyautogui.hotkey('ctrl','c')
pyautogui.hotkey('ctrl','v')

#The screenshot() function is used to take the screenshot of the screen at any instance.
#It will return a PIL object containing the image in a variable. We can also store the screenshot at the desired path .

im1=pyautogui.screenshot()

# Passing a string of a filename will save the screenshot to a file as well as return it as an Image object. 
im2 = pyautogui.screenshot('my_screenshot.png')

