from py_stealth import ClientRequestObjectTarget, ClientTargetResponsePresent
from py_stealth import ClientTargetResponse
import time


def RequestTarget(_timeoutS = 0):
    ClientRequestObjectTarget()
    _timeout = time.time() + _timeoutS

    while not ClientTargetResponsePresent():
        if _timeoutS != 0 and time.time() > _timeout:
            return ""
    
    return ClientTargetResponse()['ID']
