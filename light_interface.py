from globals import *
import time

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
''' % os.path.join(os.path.dirname(__file__),'node_modules'))

def tell_light_to(action):
    setLightMood = 'setLightMood'
    match action:
        case ACTION.MOTIVATE: context.call(setLightMood, 241, 194, 50)
        case ACTION.WAKE_UP: context.call(setLightMood, 41, 134, 204)
        case ACTION.SOOTH: context.call(setLightMood, 188, 139, 145)
        case ACTION.ANGER: context.call(setLightMood, 255, 0, 0)
        case _: context.call(setLightMood, 255, 255, 255)

def AHHH():
    for i in range(10):
        tell_light_to(None)
        time.sleep(0.01)
        tell_light_to(ACTION.ANGER)
        time.sleep(0.1)

def main():
    #tell_light_to(ACTION.WAKE_UP)
    AHHH()

def splash():
    tell_light_to(ACTION.ANGER)
    time.sleep(0.05)
    tell_light_to(None)

if __name__ == "__main__":
    main()