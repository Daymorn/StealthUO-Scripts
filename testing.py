from py_stealth import *
from helpers import *


if __name__ == '__main__':
    while True:
        Wait(250)
        RequestContextMenu(Self())
        _i = 0
        _insure = False
        for _menuItem in GetContextMenu().splitlines():
            if "Toggle Item Insurance" in _menuItem:
                SetContextMenuHook(Self(), _i)
                _insure = True
            else:
                _i += 1

        Wait(25000)
