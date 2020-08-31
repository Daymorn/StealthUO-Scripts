from py_stealth import *
from helpers import RequestTarget
from datetime import datetime


Confidence = False
FanDancer = 0x0F7
Corpse = 0x2006
LootBag = 0
TypeList = []
PlayerTypes = [183, 184, 185, 186, 400, 401, 402, 403, 605, 606, 607, 608, 666, 667, 694, 695, 750, 751, 970]


def OnDrawObject(_objID):
    if GetType(_objID) in PlayerTypes:
        _tooltipRec = []
        _tooltipRec = GetTooltipRec(_objID)
        if len(_tooltipRec) > 0:
            _clilocID = _tooltipRec[0]['Cliloc_ID']
            if _clilocID == 1050045:
                _name = _tooltipRec[0]['Params'][1]
                _now = datetime.now()
                _now = _now.strftime("%m/%d/%Y %H:%M:%S")
                AddToSystemJournal(f'Player Found: {_name} at {_now}')


def OnClilocSpeech(_param1, _param2, _param3, _message):
    if 'exude' in _message:
        Confidence = True
    elif 'wanes' in _message:
        Confidence = False
    return


def LootCorpse(_corpse):
    UseObject(_corpse)
    Wait(250)
    if FindTypesArrayEx([0xFFFF], [0xFFFF], [_corpse], True):
        _items = GetFindedList()
        for _item in _items:
            if 'splintering' in GetTooltip(_item):
                AddToSystemJournal(f'Looting Item: {_item}')
                MoveItem(_item, 1, LootBag, 0, 0, 0)
                InsureItem(_item)
    return


def InsureItem(_item):
    RequestContextMenu(Self())
    SetContextMenuHook(Self(), 9)
    Wait(250)
    WaitTargetObject(_item)
    Wait(250)
    CancelMenu()
    CancelAllMenuHooks()
    CancelTarget()
    return


if __name__ == '__main__':
    SetEventProc('evclilocspeech', OnClilocSpeech)
    SetEventProc('evdrawobject', OnDrawObject)
    SetDropDelay(850)
    UseObject(Backpack())
    Wait(850)
    AddToSystemJournal('Target your loot bag...')
    LootBag = RequestTarget()
    UseObject(LootBag)
    Wait(850)
    _monsters = []
    _corpses = []
    _currentTarget = 0
    
    while True:
        while not Connected():
            Connect()
            Wait(10000)

        if FindTypesArrayEx([FanDancer], [0xFFFF], [0x0], False):
            _monsters = GetFindedList()
        
        # entrance 79, 97, 326, 344 - bloodyroom 104, 115, 640, 660
        if _currentTarget == 0 or IsDead(_currentTarget) or not IsObjectExists(_currentTarget) and len(_monsters) > 0:
            if 104 <= GetX(_currentTarget) <= 115 and 640 <= GetY(_currentTarget) <= 660:
                _currentTarget = _monsters[0]
                AddToSystemJournal(f'Current Target: {_currentTarget}')
                UseVirtue('honor')
                WaitTargetObject(_currentTarget)
                Attack(_currentTarget)
        
        if _currentTarget != 0 and not IsDead(_currentTarget) and IsObjectExists(_currentTarget):
            NewMoveXY(GetX(_currentTarget), GetY(_currentTarget), True, 0, True)
            Attack(_currentTarget)

        if GetHP(Self()) <= 90 and not Confidence:
            Cast('Confidence')

        if GetMana(Self()) >= 40:
            UsePrimaryAbility()
        
        if FindTypesArrayEx([Corpse], [0xFFFF], [0x0], False):
            _corpses = GetFindedList()
            if _corpses > 0:
                for _corpse in _corpses:
                    if GetDistance(_corpse) < 3:
                        LootCorpse(_corpse)
                        Ignore(_corpse)
                    else: # entrance 79, 97, 326, 344 - bloodyroom 104, 115, 640, 660
                        if 104 <= GetX(_corpse) <= 115 and 640 <= GetY(_corpse) <= 660:
                            NewMoveXY(GetX(_corpse), GetY(_corpse), True, 0, True)
                            LootCorpse(_corpse)
                            Ignore(_corpse)
        Wait(250)
