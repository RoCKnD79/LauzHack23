from pythonmonkey import require as js_require
from globals import *

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
        case ACTION.ANGER: context.call(setLightMood, 0, 0, 255)
        case _: context.call(setLightMood, 255, 255, 255)

def main():
    tell_light_to(ACTION.WAKE_UP)


if __name__ == "__main__":
    main()