from py_stealth import *
from helpers import *


if __name__ == '__main__':
    while True:
        try:
            if FindTypeEx(0xFFFF, 0xFFFF, 0x0, True):
                _itemList = GetFoundList()
                print(f'{len(_itemList)} items found')
            else:
                print(f'none found')
        except:
            print(f'something went wrong')
        Wait(250)
