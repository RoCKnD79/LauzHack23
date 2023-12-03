from enum import IntEnum

class ACTION(IntEnum):
    MOTIVATE = 0
    WAKE_UP = 1
    SOOTH = 2
    ANGER = 3

class STATE(IntEnum):
    IDLE = 0
    GAME = 1
    WORK = 2
    SLEEP = 3
    RELAX = 4
    AWAKEN = 5