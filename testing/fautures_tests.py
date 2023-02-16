
try:
    from typing import Union, Optional, List
    from types import NoneType
    from decimal import Decimal
except ImportError:
    from typing import Union
    from types import NoneType
    from decimal import Decimal


global kelvinConstant, rankinDivConstant, rankinRedivConstant, rankinStatConstant
kelvinConstant: Decimal = Decimal('273.15')
rankinStatConstant: Decimal = Decimal('491.67')
rankinRedivConstant: Decimal = Decimal('0.55555555555')
rankinDivConstant: Decimal = Decimal('1.8')

listup = list[Union[int, float]]
super_listup = Union[int, float, listup]
key_list = Optional[Union[str, list[str]]]

def fahrenMethod(target, status: Union[str, None]) -> Decimal:
    target = Decimal(target)
    if status == 'to fehren':
        result = target * Decimal('1.8') + Decimal('32')
        return result

    elif status == 'to kelvin&celsius':
        result = (target - Decimal('32')) / Decimal('1.8')
        return result
        
    raise TypeError(status)# _UndefinedStateError

class Temperature:
        
    def Kelvin(_Temperature: super_listup, *, Key: key_list ='celsius') -> Union[float, list[float]]:
        """
            This function converts the entered temperature `into Kelvin`.
        
        """
        if isinstance(Key, NoneType):
            Key = 'celsius'
            Temperature.Kelvin(_Temperature, Key = Key)

        if isinstance(Key, list) and isinstance(_Temperature, list):

            if type(_Temperature[0]) not in [int, float] and type(Key[0]) != str:

                _Temperature = list(map(int, _Temperature))
                Key = list(map(str, Key))
                Temperature.Kelvin(_Temperature, Key = Key)

            if isinstance(_Temperature[0], not int or float):#type(_Temperature[0]) not in [int, float]
                    _Temperature = list(map(int, _Temperature))
                    Temperature.Kelvin(_Temperature, Key = Key)

            if isinstance(Key[0], not str):
                Key = list(map(str, Key))
                Temperature.Kelvin(_Temperature, Key = Key)

            else:

                    if len(_Temperature) != len(Key):
                        raise TypeError(len(_Temperature), len(Key))#    _InstabilityError

                    result: list[int] = []
                    dummy_tm: list[int] = _Temperature
                    dummy_key: list[str] = Key
                    for i in range(len(dummy_tm)):
                        _Temperature = dummy_tm[i]
                        Key = dummy_key[i]
                        _Temperature = float(_Temperature)
                        _Temperature = Decimal(f'{_Temperature}')

                        if Key.lower() in ['k', 'kelvin']:
                            ex = float(_Temperature)
                            result.append(ex)
                            _Temperature = int(_Temperature)
                        elif Key.lower() in ['c', 'celsius']:
                            _Temperature += kelvinConstant
                            result.append(float(_Temperature))
                            _Temperature = int(_Temperature)
                        elif Key.lower() in ['f', 'fahrenheit']:
                            _Temperature = fahrenMethod(target = _Temperature, status = 'to kelvin&celsius')
                            _Temperature += kelvinConstant
                            result.append(float(_Temperature))
                            _Temperature = int(_Temperature)
                        elif Key.lower() in ['r', 'rankin']:
                            _Temperature -= rankinStatConstant
                            _Temperature *= rankinRedivConstant
                            result.append(float(_Temperature))
                            _Temperature = int(_Temperature)
                        else:
                            result.append('KNE') # KNE: Key Not Exist
                    return result

        elif isinstance(Key, str) and isinstance(_Temperature, int or float):  

            _Temperature = float(_Temperature)
            _Temperature = Decimal(f'{_Temperature}')

            if Key.lower() in ['k', 'kelvin']:
                return float(_Temperature)

            elif Key.lower() in ['c', 'celsius']:
                return float(_Temperature + kelvinConstant)

            elif Key.lower() in ['f', 'fahrenheit']:
                _Temperature = fahrenMethod(target = _Temperature, status = 'to kelvin&celsius')
                _Temperature += kelvinConstant 
                return float(_Temperature)
            
            elif Key.lower() in ['r', 'rankin']:
                _Temperature -= rankinStatConstant
                _Temperature *= rankinRedivConstant
                _Temperature += kelvinConstant
                return float(_Temperature)
        
            raise TypeError(Key)#   _TemperatureError

        elif isinstance(Key, str) and isinstance(_Temperature, list):

                if type(_Temperature[0]) not in [int, float]:
                    _Temperature = list(map(int, _Temperature))
                    Temperature.Kelvin(_Temperature, Key = Key)

                result: list[int] = []
                dummy_tm: list[int] = _Temperature
                dummy_key: str = Key
                for i in range(len(dummy_tm)):
                    _Temperature = dummy_tm[i]
                    Key = dummy_key
                    _Temperature = float(_Temperature)
                    _Temperature = Decimal(f'{_Temperature}')

                    if Key.lower() in ['k', 'kelvin']:
                        ex = float(_Temperature)
                        result.append(ex)
                        _Temperature = int(_Temperature)
                    elif Key.lower() in ['c', 'celsius']:
                        _Temperature += kelvinConstant
                        result.append(float(_Temperature))
                        _Temperature = int(_Temperature)
                    elif Key.lower() in ['f', 'fahrenheit']:
                        _Temperature = fahrenMethod(target = _Temperature, status = 'to kelvin&celsius')
                        _Temperature += kelvinConstant
                        result.append(float(_Temperature))
                        _Temperature = int(_Temperature)
                    elif Key.lower() in ['r', 'rankin']:
                        _Temperature -= rankinStatConstant
                        _Temperature *= rankinRedivConstant
                        result.append(float(_Temperature))
                        _Temperature = int(_Temperature)
                    else:
                        result.append('KNE') # KNE: Key Not Exist
                return result

        raise TypeError(Key, _Temperature) #    _KeyTypeError



# print(Temperature.Kelvin([785, '34'], Key='c'))