"""
"""
try:
    from decimal import Decimal
    from typing import Union
    from .errors.ECUtm import _TemperatureError, _UndefinedStateError, _KeyTypeError, _InstabilityError
except ImportError:
    from decimal import Decimal
    from typing import Union
    from errors.ECUtm import _TemperatureError, _UndefinedStateError, _KeyTypeError, _InstabilityError

kelvinConstant: Decimal = Decimal('273.15')
rankinStatConstant: Decimal = Decimal('491.67')
rankinRedivConstant: Decimal = Decimal('0.55555555555')
rankinDivConstant: Decimal = Decimal('1.8')


def fahrenMethod(target, status: Union[str, None]) -> Decimal:
    target = Decimal(target)
    if status == 'to fehren':
        result = target * Decimal('1.8') + Decimal('32')
        return result

    elif status == 'to kelvin&celsius':
        result = (target - Decimal('32')) / Decimal('1.8')
        return result
        
    raise _UndefinedStateError(status)


def overloading(func):
    
    def capture(tm, key):
        
        if type(tm) in [int, float] and type(key) == str:
            exit(1)

        if type(tm) in [int, float]:
            exit(1)

        elif type(tm) and type(key) == list:

            if len(tm) != len(key):
                raise _InstabilityError(len(tm), len(key))

            result: list[int] = []
            dummy_tm: list[int] = tm
            dummy_key: list[int] = key
            for i in range(len(dummy_tm)):
                tm = dummy_tm[i]
                key = dummy_key[i]
                tm = float(tm)
                tm = Decimal(f'{tm}')

                if key in ['K', 'k', 'Kelvin']:
                    ex = float(tm - kelvinConstant)
                    result.append(ex)
                    tm = int(tm)
                elif key in ['C', 'c', 'Celsius']:
                    tm = float(tm)
                    result.append(tm)
                    tm = int(tm)
                elif key in ['F', 'f', 'Fahrenheit']:
                    tm = float(fahrenMethod(target = tm, status = 'to kelvin&celsius'))
                    result.append(tm)
                    tm = int(tm)
                elif key.lower() in ['r', 'rankin']:
                    tm -= rankinStatConstant
                    tm *= rankinRedivConstant
                    tm = float(tm)
                    result.append(tm)
                    tm = int(tm)
                return result
        capture(tm, key)
                
             
    return capture

@overloading
def gool(em, f):
    
    print(em + f)

print(gool([1,2,3], ['k','c','r']))