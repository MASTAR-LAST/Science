"""
TODO: MAKE A DOC FOR THIS FILE
"""
__all__ = ['Temperature']
try:
    from typing import Union, Optional
    from decimal import Decimal
    from .errors.ECUtm import _InstabilityError, _UndefinedStateError, _KeyTypeError, _TemperatureError
except ImportError:
    from typing import Union
    from decimal import Decimal
    from errors.ECUtm import _InstabilityError, _UndefinedStateError, _KeyTypeError, _TemperatureError

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
        
    raise _UndefinedStateError(status)


class Temperature:
    """
        FUNCTIONS:
            All functions take two arguments (_Temperature, Key)

                Available FUNCTIONS:
                            Func 1:  Kelvin(here but the number of temperature, here but the scale key).
                            Func 2:  Fahrenheit(here but the number of temperature, here but the scale key).
                            Func 3:  Celsius(here but the number of temperature, here but the scale key).

                Available CASES:
                            Case 1:  Use the scale key 'Kelvin or k' if the temperature number from Kelvin. 
                            Case 2:  Use the scale key 'Fahrenheit or f' if the temperature number from Fahrenheit.
                            Case 3:  Use the scale key 'Celsius or c' if the temperature number from Celsius.

         USES:
            If you want to switch between temperature gauges,
            Use the name of the scale you want to convert to,
            then put the temperature and the symbol of the scale from which this temperature came.

        
        CREATED BY: Muhammed Alkohawaldeh
        CLASS VERSION: 0.1.0-pre-Alpha
    
    """
        
        # Not sure about it yet
    def __str__(self):
        return self.__Temperature
        
    
    @staticmethod
    def Kelvin(_Temperature: super_listup, *, Key: key_list ='celsius') -> Union[float, list[float]]:
        """
            This function converts the entered temperature into Kelvin
        
        """
        if type(Key) == None:
            Key = 'celsius'
            Temperature.Kelvin(_Temperature, Key)

        if type(Key) == list and type(_Temperature) == list:

            if type(_Temperature[0]) not in [int, float] and type(Key[0]) != str:

                _Temperature = list(map(int, _Temperature))
                Key = list(map(str, Key))
                Temperature.Kelvin(_Temperature, Key)

            if type(_Temperature[0]) not in [int, float]:
                    _Temperature = list(map(int, _Temperature))
                    Temperature.Kelvin(_Temperature, Key)

            if type(Key[0]) != str:
                Key = list(map(str, Key))
                Temperature.Kelvin(_Temperature, Key)

            else:

                    if len(_Temperature) != len(Key):
                        raise _InstabilityError(len(_Temperature), len(Key))

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

        elif type(Key) == str and type(_Temperature) in [int, float]:  

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
        
            raise _TemperatureError(Key)

        elif type(Key) == str and type(_Temperature):

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

        raise _KeyTypeError(Key, _Temperature)

    @staticmethod
    def Celsius(_Temperature: super_listup, *, Key: key_list ='celsius') -> float:
        """
            This function converts the entered temperature into Celsius
        
        """
        if type(Key) == None:
            Key = 'celsius'
            Temperature.Celsius(_Temperature, Key)

        if type(Key) == list and type(_Temperature) == list:

            if type(_Temperature[0]) not in [int, float] and type(Key[0]) != str:

                _Temperature = list(map(int, _Temperature))
                Key = list(map(str, Key))
                Temperature.Celsius(_Temperature, Key)

            if type(_Temperature[0]) not in [int, float]:
                    _Temperature = list(map(int, _Temperature))
                    Temperature.Celsius(_Temperature, Key)
                    
            if type(Key[0]) != str:
                Key = list(map(str, Key))
                Temperature.Celsius(_Temperature, Key)

            else:
                    if len(_Temperature) != len(Key):
                        raise _InstabilityError(len(_Temperature), len(Key))

                    result: list[int] = []
                    dummy_tm: list[int] = _Temperature
                    dummy_key: list[str] = Key
                    for i in range(len(dummy_tm)):
                        _Temperature = dummy_tm[i]
                        Key = dummy_key[i]
                        _Temperature = float(_Temperature)
                        _Temperature = Decimal(f'{_Temperature}')

                        if Key.lower() in ['k', 'kelvin']:
                            ex = float(_Temperature - kelvinConstant)
                            result.append(ex)
                            _Temperature = int(_Temperature)
                        elif Key.lower() in ['c', 'celsius']:
                            _Temperature = float(_Temperature)
                            result.append(_Temperature)
                            _Temperature = int(_Temperature)
                        elif Key.lower() in ['f', 'fahrenheit']:
                            _Temperature = float(fahrenMethod(target = _Temperature, status = 'to kelvin&celsius'))
                            result.append(_Temperature)
                            _Temperature = int(_Temperature)
                        elif Key.lower() in ['r', 'rankin']:
                            _Temperature -= rankinStatConstant
                            _Temperature *= rankinRedivConstant
                            _Temperature = float(_Temperature)
                            result.append(_Temperature)
                            _Temperature = int(_Temperature)
                        else:
                            result.append('KNE') # KNE: Key Not Exist
                    return result

        elif type(Key) == str and type(_Temperature) in [int, float]:  

            _Temperature = float(_Temperature)
            _Temperature = Decimal(f'{_Temperature}')

            if Key.lower() in ['k', 'kelvin']:
                return float(_Temperature - kelvinConstant)

            elif Key.lower() in ['c', 'celsius']:
                return float(_Temperature)

            elif Key.lower() in ['f', 'fahrenheit']:
                return float(fahrenMethod(target = _Temperature, status = 'to kelvin&celsius'))

            elif Key.lower() in ['r', 'rankin']:
                _Temperature -= rankinStatConstant
                _Temperature *= rankinRedivConstant
                return float(_Temperature)
        
            raise _TemperatureError(Key)

        elif type(Key) == str and type(_Temperature) == list:

                    result: list[int] = []
                    dummy_tm: list[int] = _Temperature
                    dummy_key: str = Key
                    for i in range(len(dummy_tm)):
                        _Temperature = dummy_tm[i]
                        Key = dummy_key
                        _Temperature = float(_Temperature)
                        _Temperature = Decimal(f'{_Temperature}')

                        if Key.lower() in ['k', 'kelvin']:
                            ex = float(_Temperature - kelvinConstant)
                            result.append(ex)
                            _Temperature = int(_Temperature)
                        elif Key.lower() in ['c', 'celsius']:
                            _Temperature = float(_Temperature)
                            result.append(_Temperature)
                            _Temperature = int(_Temperature)
                        elif Key.lower() in ['f', 'fahrenheit']:
                            _Temperature = float(fahrenMethod(target = _Temperature, status = 'to kelvin&celsius'))
                            result.append(_Temperature)
                            _Temperature = int(_Temperature)
                        elif Key.lower() in ['r', 'rankin']:
                            _Temperature -= rankinStatConstant
                            _Temperature *= rankinRedivConstant
                            _Temperature = float(_Temperature)
                            result.append(_Temperature)
                            _Temperature = int(_Temperature)
                        else:
                            result.append('KNE') # KNE: Key Not Exist
                    return result

        raise _KeyTypeError(Key, _Temperature)

    @staticmethod
    def Fahrenheit(_Temperature: super_listup, *, Key: key_list ='celsius') -> float:
        """
            This function converts the entered temperature into Fahrenheit
        
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
                        raise _InstabilityError(len(_Temperature), len(Key))

                    result: list[int] = []
                    dummy_tm: list[int] = _Temperature
                    dummy_key: list[str] = Key
                    for i in range(len(dummy_tm)):
                        _Temperature = dummy_tm[i]
                        Key = dummy_key[i]
                        _Temperature = float(_Temperature)
                        _Temperature = Decimal(f'{_Temperature}')

                        if Key.lower() in ['k', 'kelvin']:
                            _Temperature -= kelvinConstant # transformed from Kelvin to Celsius
                            _Temperature = float(fahrenMethod(target = _Temperature, status = 'to fehren')) # transformed from Celsius to Fahrenheit
                            result.append(_Temperature)
                            _Temperature = int(_Temperature)
                        elif Key.lower() in ['c', 'celsius']:
                            _Temperature = float(fahrenMethod(target = _Temperature, status = 'to fehren')) # transformed from Celsius to Fahrenheit
                            result.append(_Temperature)
                            _Temperature = int(_Temperature)
                        elif Key.lower() in ['f', 'fahrenheit']:
                            _Temperature = float(_Temperature)
                            result.append(_Temperature)
                            _Temperature = int(_Temperature)
                        elif Key.lower() in ['r', 'rankin']:
                            _Temperature -= rankinStatConstant
                            _Temperature *= rankinRedivConstant
                            _Temperature = float(fahrenMethod(target = _Temperature, status = 'to fehren'))
                            result.append(_Temperature)
                            _Temperature = int(_Temperature)
                        else:
                            result.append('KNE') # KNE: Key Not Exist
                    return result

        elif type(Key) == str and type(_Temperature) in [int, float]:  

            _Temperature = float(_Temperature)
            _Temperature = Decimal(f'{_Temperature}')

            if Key.lower() in ['k', 'kelvin']:
                _Temperature -= kelvinConstant # transformed from Kelvin to Celsius
                _Temperature = fahrenMethod(target = _Temperature, status = 'to fehren') # transformed from Celsius to Fahrenheit
                return float(_Temperature)

            elif Key.lower() in ['c', 'celsius']:
                _Temperature = float(fahrenMethod(target = _Temperature, status = 'to fehren')) 
                return _Temperature

            elif Key.lower() in ['f', 'fahrenheit']:
                return float(_Temperature)
            
            elif Key.lower() in ['r', 'rankin']:
                _Temperature -= rankinStatConstant
                _Temperature *= rankinRedivConstant
                _Temperature = float(fahrenMethod(target = _Temperature, status = 'to fehren')) 
                return _Temperature
        
            raise _TemperatureError(Key)

        elif type(Key) == str and type(_Temperature) == list:

                    result: list[int] = []
                    dummy_tm: list[int] = _Temperature
                    dummy_key: str = Key
                    for i in range(len(dummy_tm)):
                        _Temperature = dummy_tm[i]
                        Key = dummy_key
                        _Temperature: float = float(_Temperature)
                        _Temperature: Decimal = Decimal(f'{_Temperature}')

                        if Key.lower() in ['k', 'kelvin']:
                            _Temperature -= kelvinConstant # transformed from Kelvin to Celsius
                            _Temperature = float(fahrenMethod(target = _Temperature, status = 'to fehren')) # transformed from Celsius to Fahrenheit
                            result.append(_Temperature)
                            _Temperature = int(_Temperature)
                        elif Key.lower() in ['c', 'celsius']:
                            _Temperature = float(fahrenMethod(target = _Temperature, status = 'to fehren')) # transformed from Celsius to Fahrenheit
                            result.append(_Temperature)
                            _Temperature = int(_Temperature)
                        elif Key.lower() in ['f', 'fahrenheit']:
                            _Temperature = float(_Temperature)
                            result.append(_Temperature)
                            _Temperature = int(_Temperature)
                        elif Key.lower() in ['r', 'rankin']:
                            _Temperature -= rankinStatConstant
                            _Temperature *= rankinRedivConstant
                            _Temperature = float(fahrenMethod(target = _Temperature, status = 'to fehren'))
                            result.append(_Temperature)
                            _Temperature = int(_Temperature)
                        else:
                            result.append('KNE') # KNE: Key Not Exist
                    return result

        raise _KeyTypeError(Key, _Temperature)


    @staticmethod
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
                        raise _InstabilityError(len(_Temperature), len(Key))

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
        
            raise _TemperatureError(Key)

        elif type(Key) == str and type(_Temperature) == list:

                    result: list[int] = []
                    dummy_tm: list[int] = _Temperature
                    dummy_key: str = Key
                    for i in range(len(dummy_tm)):
                        _Temperature = dummy_tm[i]
                        Key = dummy_key
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

        raise   _KeyTypeError(Key, _Temperature)


print(Temperature.Fahrenheit([1,2,3], Key = 'K'))

