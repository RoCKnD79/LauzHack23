from pynput.keyboard import Key, Listener
from pynput.mouse import Controller

import time
import numpy as np

import light_interface
from threading import Thread

import colorsys



#not used yet
#mouse = Controller()

#light interface
litra_ctrller = light_interface.LitraController()

#only update one input
wasReleased = True


#pressing speed
currentPress = 0
speed = 0
MAX_NUMBER_OF_SPEED = 100
speeds = []
averagePressingSpeed = 0

transitionTime = 0

#typing speed

TYPING_TIMEOUT = 1 #in s
MAX_NUMBER_OF_TYPING_SPEED = 20
typingSpeeds = []
averageTypingSpeed = 0

#word detection
TYPING_THRESHOLD = 0.3  #accepted variation in user typing speed, above typing speed + threshold word's counter is reset 
wordDetectionTimeout = TYPING_TIMEOUT  #in s, base on typing speed
lastPress = 0
currentWordLength = 0

#Error detection
averageError = 0
numberOfWords = 0
numberOFErrors = 0

#multy press
MULTY_PRESS_TRIGER = 3
keyCurrentlyPress = []


def on_press(key):
    addNewMultyPress(key)
    #print(key)
    global wasReleased, currentPress
    if not wasReleased :
        return
    wasReleased = False

    # typing speed
    currentPress = time.time()

    #end of a word
    if key == Key.space :
        wordFinish()
    else :
        #detect word
        wordDetection()
        
    #backspace press
    if key == Key.backspace :
        detectError()

step = 0
def on_release(key):
    removeMultyPress(key)

    global wasReleased, currentPress, speed, transitionTime, step
    wasReleased = True

    speed = time.time() - currentPress
    transitionTime += speed

    addNewPresSpeed(speed)
    
    if (step == 5):
        # if(0.05 < averagePressingSpeed and averagePressingSpeed < 0.3):
        #     litra_ctrller.state = STATE.RELAX
        #     Thread(target = litra_ctrller.relax, args=()).start()

        # else:
        #     litra_ctrller.state = STATE.IDLE
        #     tell_light_to(None)
        
        #min 0.2 max .05
        colors = colorsys.hsv_to_rgb(2 * (averageTypingSpeed), 1, 1)
        light_interface.setLightMood(round(colors[0] * 255), round(colors[1] * 255), round(colors[2] * 255))
        # light_interface.custom_b = round(colors[2] * 255)
        # light_interface.custom_g = round(colors[1] * 255)
        # light_interface.custom_r = round(colors[0] * 255)
        # litra_ctrller.state = light_interface.STATE.CUSTOM
        # litra_ctrller.custom_rgb()
        step = 0
    else :
        step += 1


    #global averageError, averagePressingSpeed, currentWordLength, numberOfWords, numberOFErrors
    #print(str(averageError) + "   " + str(numberOfWords) + "   " + str(numberOFErrors) + "   "+ str(averagePressingSpeed) + "   " + str(currentWordLength))
    print(averageTypingSpeed)
    if key == Key.esc:
        return False

"""
Press Speed
"""
def addNewPresSpeed(newSpeed):
    #print("add new speed and average")
    global MAX_NUMBER_OF_SPEED, speeds, averagePressingSpeed
    if len(speeds) >= MAX_NUMBER_OF_SPEED :
        speeds.pop(0)
    speeds.append(newSpeed)
    averagePressingSpeed = np.mean(speeds)


"""
Word detection
"""
def wordDetection():
    #print("word detection")
    global wordDetectionTimeout, lastPress, currentPress, currentWordLength
    currentTypingSpeed = currentPress - lastPress
    if currentTypingSpeed > wordDetectionTimeout :
        wordFinish()
    else :
        currentWordLength += 1
        addNewTypingSpeed(currentTypingSpeed)

    lastPress = currentPress

def wordFinish():
    global currentWordLength, numberOfWords
    if currentWordLength > 2:
        numberOfWords += 1
    currentWordLength = 0

"""
Typing speed
"""

def addNewTypingSpeed(newSpeed):
    #print("add new typing speed and average")
    global MAX_NUMBER_OF_TYPING_SPEED, typingSpeeds, averageTypingSpeed, wordDetectionTimeout, TYPING_THRESHOLD
    if len(typingSpeeds) >= MAX_NUMBER_OF_TYPING_SPEED :
        typingSpeeds.pop(0)
    typingSpeeds.append(newSpeed)
    averageTypingSpeed = np.mean(typingSpeeds)

    #update word detection timeout base on user typing speed
    wordDetectionTimeout = averageTypingSpeed + TYPING_THRESHOLD



"""
Error detection
"""

def detectError():
    #print("backspacePress")
    global currentWordLength, numberOFErrors
    if currentWordLength > 3 :
        numberOFErrors += 1

"""
Multy press
"""

def addNewMultyPress(newKey):
    global keyCurrentlyPress, MULTY_PRESS_TRIGER
    if newKey not in keyCurrentlyPress :
        keyCurrentlyPress.append(newKey)

    if len(keyCurrentlyPress) > MULTY_PRESS_TRIGER :
        print("multi press")
        #call a function to trigger led
        #litra_ctrller.state = STATE.RELAX
        #Thread(target = litra_ctrller.splash, args=()).start()
        litra_ctrller.splash()


def removeMultyPress(newKey):
    global keyCurrentlyPress
    if newKey in keyCurrentlyPress :
        keyCurrentlyPress.remove(newKey)

def keyboard_thread():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


