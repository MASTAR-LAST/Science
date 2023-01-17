
try:
    from typing import Union, Optional
    from decimal import Decimal
except ImportError:
    from typing import Union
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
        
    def Rankin(_Temperature: super_listup, *, Key: key_list ='celsius') -> float:
        """
            This function converts the entered temperature into Rankin
        
        """
        if type(Key) == None:
            Key = 'celsius'
            Temperature.Fahrenheit(_Temperature, Key)

        if type(Key) == list and type(_Temperature) == list:

            if type(_Temperature[0]) not in [int, float] and type(Key[0]) != str:

                _Temperature = list(map(int, _Temperature))
                Key = list(map(str, Key))
                Temperature.Fahrenheit(_Temperature, Key)

            if type(_Temperature[0]) not in [int, float]:
                    _Temperature = list(map(int, _Temperature))
                    Temperature.Fahrenheit(_Temperature, Key)
                    
            if type(Key[0]) != str:
                Key = list(map(str, Key))
                Temperature.Fahrenheit(_Temperature, Key)

            else:
                    if len(_Temperature) != len(Key):
                        raise TypeError(len(_Temperature), len(Key))# _InstabilityError

                    result: list[int] = []
                    dummy_tm: list[int] = _Temperature
                    dummy_key: list[str] = Key
                    for i in range(len(dummy_tm)):
                        _Temperature = dummy_tm[i]
                        Key = dummy_key[i]
                        _Temperature = float(_Temperature)
                        _Temperature = Decimal(f'{_Temperature}')

                        if Key.lower() in ['k', 'kelvin']:
                            _Temperature *= rankinDivConstant
                            result.append(float(_Temperature))
                            _Temperature = int(_Temperature)
                        elif Key.lower() in ['c', 'celsius']:
                            _Temperature += kelvinConstant
                            _Temperature *= rankinDivConstant
                            result.append(float(_Temperature))
                            _Temperature = int(_Temperature)
                        elif Key.lower() in ['f', 'fahrenheit']:
                            _Temperature = fahrenMethod(target = _Temperature, status = 'to kelvin&celsius')
                            _Temperature *= rankinDivConstant
                            result.append(float(_Temperature))
                            _Temperature = int(_Temperature)
                        elif Key.lower() in ['r', 'rankin']:
                            result.append(float(_Temperature))
                            _Temperature = int(_Temperature)
                        else:
                            result.append('KNE') # KNE: Key Not Exist
                    return result

        elif type(Key) == str and type(_Temperature) in [int, float]:  

            _Temperature = float(_Temperature)
            _Temperature = Decimal(f'{_Temperature}')

            if Key.lower() in ['k', 'kelvin']:
                _Temperature *= rankinDivConstant
                return float(_Temperature)

            elif Key.lower() in ['c', 'celsius']:
                _Temperature += kelvinConstant
                _Temperature *= rankinDivConstant
                return float(_Temperature)

            elif Key.lower() in ['f', 'fahrenheit']:
                _Temperature = fahrenMethod(target = _Temperature, status = 'to kelvin&celsius')
                _Temperature *= rankinDivConstant
                return float(_Temperature)
            
            elif Key.lower() in ['r', 'rankin']:
                return float(_Temperature)
        
            raise TypeError(Key)# _TemperatureError

        elif type(Key) == str and type(_Temperature) == list:

                    result: list[int] = []
                    dummy_tm: list[int] = _Temperature
                    dummy_key: str = Key
                    for i in range(len(dummy_tm)):
                        _Temperature = dummy_tm[i]
                        Key = dummy_key
                        _Temperature = float(_Temperature)
                        _Temperature: Decimal = Decimal(f'{_Temperature}')

                        if Key.lower() in ['k', 'kelvin']:
                            _Temperature *= rankinDivConstant
                            result.append(float(_Temperature))
                            _Temperature = int(_Temperature)
                        elif Key.lower() in ['c', 'celsius']:
                            _Temperature += kelvinConstant
                            _Temperature *= rankinDivConstant
                            result.append(float(_Temperature))
                            _Temperature = int(_Temperature)
                        elif Key.lower() in ['f', 'fahrenheit']:
                            _Temperature = fahrenMethod(target = _Temperature, status = 'to kelvin&celsius')
                            _Temperature *= rankinDivConstant
                            result.append(float(_Temperature))
                            _Temperature = int(_Temperature)
                        elif Key.lower() in ['r', 'rankin']:
                            result.append(float(_Temperature))
                            _Temperature = int(_Temperature)
                        else:
                            result.append('KNE') # KNE: Key Not Exist
                    return result

        raise   TypeError(Key, _Temperature)# _KeyTypeError


print(Temperature.Rankin([1,2,3], Key = 'c'))