from enum import Enum


class Type(Enum):
    NONE = 0
    ERROR = 1
    FATAL = 2
    WARNING = 3
    INFO = 4
    STATUS = 5
    SUCCESS = 7


def cmd_print(status, *args):
    esc = {Type.NONE: '', Type.ERROR: '\033[31m', Type.FATAL: '\033[1;41m', Type.WARNING: '\033[33m',
           Type.INFO: '\033[97m', Type.STATUS: '\033[34m', Type.SUCCESS: '\033[32m'}
    print(esc[status], end='')
    print(' '.join(map(str, args)))
