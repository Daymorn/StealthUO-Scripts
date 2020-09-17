from py_stealth import ClientRequestObjectTarget, ClientTargetResponsePresent
from py_stealth import ClientTargetResponse
import time


def RequestTarget(_timeoutS=0):
    ClientRequestObjectTarget()
    _timeout = time.time() + _timeoutS

    while not ClientTargetResponsePresent():
        if _timeoutS != 0 and time.time() > _timeout:
            return ""

    return ClientTargetResponse()['ID']


def GetParam(_tooltipRec, _clilocID):
    for _tooltip in _tooltipRec:
        if _tooltip['Cliloc_ID'] == _clilocID:
            return int(_tooltip['Params'][0])
    return 0


def ClilocIDExists(_tooltipRec, _clilocID):
    for _tooltip in _tooltipRec:
        if _tooltip['Cliloc_ID'] == _clilocID:
            return True
    return False
