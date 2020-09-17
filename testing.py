from py_stealth import *
from helpers import *


if __name__ == '__main__':
    while True:
        _item = RequestTarget()
        _tooltipRec = GetTooltipRec(_item)
        if GetParam(_tooltipRec, 1112857) >= 20 and not ClilocIDExists(_tooltipRec, 1152714) and not \
                ClilocIDExists(_tooltipRec, 1049643):
            print(f'True')
        else:
            print(f'False')
