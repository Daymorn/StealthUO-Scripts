from py_stealth import *


if __name__ == '__main__':
    while True:
        if FindTypesArrayEx([0xFFFF], [0xFFFF], [0x0], False):
            _foundList = GetFindedList()
            _lengthOfList = len(_foundList)
            print(f'objects found: {_lengthOfList}')
        else:
            print('no objects found!')

        Wait(500)
