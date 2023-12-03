from globals import *
import time
import math

import os
import sys

from execjs import get

runtime = get('Node')
context = runtime.compile('''
module.paths.push('%s');
const litra = require('litra');
const device = litra.findDevice();

function setLightMood(R, G ,B) {
    litra.setRGBColor(device, R, G, B);
}
                          
function setZoneRGB(zone, R, G, B) {
    litra.setZoneColorRGB(device, zone, R, G, B);
}
''' % os.path.join(os.path.dirname(__file__),'node_modules'))

MAX_COLOR_VAL = 255

def setLightMood(R, G, B):
    context.call('setLightMood', R, G, B)

def setZoneRGB(zone, R, G, B):
    context.call('setZoneRGB', zone, R, G, B)

def tell_light_to(action):
    match action:
        case ACTION.MOTIVATE: setLightMood(241, 194, 50)
        case ACTION.WAKE_UP: setLightMood(41, 134, 204)
        case ACTION.SOOTH: setLightMood(188, 139, 145)
        case ACTION.ANGER: setLightMood(255, 0, 0)
        case _: setLightMood(255, 255, 255)

def AHHH():
    for i in range(10):
        tell_light_to(None)
        time.sleep(0.01)
        tell_light_to(ACTION.ANGER)
        time.sleep(0.1)

def fade(R, G, B, period):
    if(period <= 0): 
        raise Exception("fading period cannot be <= 0")
    
    min_ratio = 0.1
    max_ratio = 0.9
    transitions = 100
    transition_period = period/(transitions)

    # increase color intensity
    ratio = min_ratio
    while(ratio < max_ratio):
        ratio += transition_period
        setLightMood(ratio * R, ratio * G, ratio * B)

    # decrease color intensity
    while(ratio > min_ratio):
        ratio -= transition_period
        setLightMood(ratio * R, ratio * G, ratio * B)


def energize():
    while(True):
        # orange
        fade(242, 112, 4, 1)
        # yellow
        fade(255, 192, 0, 1)

def blue_focus():
    while(True):
        # blue
        fade(41, 134, 204, 1)

def calm_down():
    while(True):
        # green
        fade(0, 255, 0, 1)

def arrow_focus(R, G, B):
    for i in range(7):
        zone = i + 1
        setZoneRGB(zone, R, G, B)

def splash():
    tell_light_to(ACTION.ANGER)
    time.sleep(0.05)
    tell_light_to(None)

def main():
    #tell_light_to(ACTION.WAKE_UP)
    #energize()
    #blue_focus()
    #setZoneRGB(6, 0, 0, 255)
    #AHHH()
    calm_down()


if __name__ == "__main__":
    main()