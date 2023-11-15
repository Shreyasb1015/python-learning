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



