from py_stealth import *
from helpers import RequestTarget
from datetime import datetime

SnakeTypes = [0x15, 0x34, 0x5A, 0x5B, 0x5C, 0x5D]
NestTypes = [0x2233]
EggTypes = [0x41BF]
BombTypes = [0x2809, 0x2808]
FluteTypes = [0x2805, 0x504, 0x503, 0x2807]
CureTypes = [0x0F07]
Areas = [
    [
        [640, 749], [634, 740], [627, 730], [617, 720], [617, 711], [627, 707], [637, 703], [647, 699], [656, 699],
        [664, 701], [673, 701], [675, 707], [678, 714], [673, 719], [664, 712], [658, 721], [664, 731], [661, 740],
        [650, 729], [663, 742], [667, 734], [662, 725], [662, 716], [668, 715], [675, 723], [680, 717], [676, 710],
        [674, 705], [666, 703], [658, 703], [650, 709], [642, 710], [634, 711], [628, 718], [636, 726], [640, 733],
        [643, 740], [644, 746]
    ],
    [
        [691, 729], [684, 734], [675, 740], [665, 743], [659, 753], [655, 765], [660, 773], [673, 772], [683, 775],
        [693, 777], [701, 770], [703, 762], [709, 753], [714, 761], [717, 768], [717, 760], [712, 752], [711, 738],
        [712, 732], [706, 741], [706, 750], [704, 758], [698, 768], [690, 770], [682, 769], [673, 769], [663, 767],
        [659, 758], [663, 750], [671, 743], [680, 740], [687, 735], [693, 731]
    ],
    [
        [694, 709], [687, 703], [688, 700], [691, 707], [698, 705], [701, 698], [708, 691], [714, 687], [715, 680],
        [716, 673], [723, 666], [729, 663], [735, 661], [741, 661], [746, 667], [747, 673], [740, 679], [740, 686],
        [740, 693], [738, 699], [732, 701], [727, 703], [726, 700], [727, 693], [729, 688], [731, 681], [735, 680],
        [735, 686], [733, 693], [727, 699], [729, 702], [728, 708], [725, 713], [726, 720], [730, 726], [737, 731],
        [740, 736], [735, 739], [728, 738], [722, 734], [715, 734], [709, 730], [709, 723], [705, 717], [698, 710]
    ],
    [
        [812, 646], [704, 654], [793, 660], [783, 662], [785, 670], [796, 676], [803, 685], [799, 696], [790, 702],
        [800, 706], [805, 714], [814, 705], [809, 693], [815, 681], [826, 671], [837, 665], [830, 656], [820, 646]
    ],
    [
        [749, 749], [758, 760], [768, 768], [777, 771], [777, 761], [772, 753], [776, 742], [786, 736], [797, 727],
        [803, 719], [794, 724], [784, 727], [772, 736], [761, 738], [749, 735], [740, 740], [749, 750]
    ]
]
Path = Areas[0]
CurrentSpot = 0


def MoveNextSpot():
    global CurrentSpot
    AddToSystemJournal("Moving to next spot...")
    while GetX(Self()) != Path[CurrentSpot][0] or GetY(Self()) != Path[CurrentSpot][1]:
        Wait(750)
        NewMoveXY(Path[CurrentSpot][0], Path[CurrentSpot][1], False, 0, False)
        if GetX(Self()) != Path[CurrentSpot][0] or GetY(Self()) != Path[CurrentSpot][1]:
            break
    CurrentSpot += 1
    if CurrentSpot == len(Path):
        CurrentSpot = 0
    return


if __name__ == '__main__':
    SetFindDistance = 5
    SetFindVertical = 5
    _flutes = []
    _snakes = []
    _eggs = []
    _bombs = []
    _cures = []
    _nests = []
    _currentSpot = 0
    MoveNextSpot()

    while True:
        while not Connected():
            Connect()
            Wait(10000)

        if FindTypesArrayEx(FluteTypes, [0xFFFF], [Backpack()], False):
            _flutes = GetFindedList()
        else:
            AddToSystemJournal('Out of flutes, quitting...')
            exit()

        if FindTypesArrayEx([EggTypes], [0xFFFF], [0x0], False):
            _eggs = GetFindedList()
            for _egg in _eggs:
                while GetX(Self()) != GetX(_egg) and GetY(Self()) != GetY(_egg):
                    NewMoveXY(GetX(_egg), GetY(_egg), False, 0, False)
                    Wait(250)
                MoveItem(_egg, 1, Backpack(), 0, 0, 0)
                Ignore(_egg)

        if FindTypesArrayEx(SnakeTypes, [0xFFFF], [0x0], False):
            _snakes = GetFindedList()

        if FindTypesArrayEx(NestTypes, [0xFFFF], [0x0], False):
            _nests = GetFindedList()







        if len(_snakes) == 0 or len(_nests) == 0:
            MoveNextSpot()
