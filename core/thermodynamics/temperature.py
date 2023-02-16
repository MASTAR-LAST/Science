"""
 Temperature class
==================
            All functions take two arguments (`_Temperature`, `Key`)

                Available FUNCTIONS:
                --------------------
                            `Func 1`:  Kelvin(here but the number of temperature, here but the scale key).
                            `Func 2`:  Fahrenheit(here but the number of temperature, here but the scale key).
                            `Func 3`:  Celsius(here but the number of temperature, here but the scale key).

                Available CASES:
                ----------------
                            `Case 1`:  Use the scale key `'Kelvin or k'` if the temperature number from `Kelvin`. 
                            `Case 2`:  Use the scale key `'Fahrenheit or f'` if the temperature number from `Fahrenheit`.
                            `Case 3`:  Use the scale key `'Celsius or c'` if the temperature number from `Celsius`.

         USES:
         -----
            If you want to switch between temperature gauges,
            Use the name of the scale you want to convert to,
            then put the temperature and the symbol of the scale from which this temperature came.

        
        CREATED BY: `Muhammed Alkohawaldeh`
        ----------------------------------
        CLASS VERSION: `0.1.0-pre-Alpha`
        --------------------------------

        Copyright 2023 Muhammed Alkohawaldeh

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""

try:
    from typing import Union, Optional
    # from types import NoneType
    from decimal import Decimal
    from .tester import speedTest
    from .errors.ECUtm import _InstabilityError, _UndefinedStateError, _KeyTypeError, _TemperatureError
except ImportError:
    from typing import Union
    # from types import NoneType
    from decimal import Decimal 
    from errors.ECUtm import _InstabilityError, _UndefinedStateError, _KeyTypeError, _TemperatureError
    from tester import speedTest

global kelvinConstant, rankinDivConstant, rankinRedivConstant, rankinStatConstant
kelvinConstant: Decimal = Decimal('273.15')
rankinStatConstant: Decimal = Decimal('491.67')
rankinRedivConstant: Decimal = Decimal('0.55555555555')
rankinDivConstant: Decimal = Decimal('1.8')

NoneType = type(None)
listup = list[Union[int, float]]
super_listup = Union[int, float, listup]
key_list = Optional[Union[str, list[str]]]

def fahrenMethod(target: Union[int, float], status: str) -> Decimal:
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
        Temperature class
        ==================
            All functions take two arguments (`_Temperature`, `Key`)

                Available FUNCTIONS:
                --------------------
                            `Func 1`:  Kelvin(here but the number of temperature, here but the scale key).
                            `Func 2`:  Fahrenheit(here but the number of temperature, here but the scale key).
                            `Func 3`:  Celsius(here but the number of temperature, here but the scale key).

                Available CASES:
                ----------------
                            `Case 1`:  Use the scale key `'Kelvin or k'` if the temperature number from `Kelvin`. 
                            `Case 2`:  Use the scale key `'Fahrenheit or f'` if the temperature number from `Fahrenheit`.
                            `Case 3`:  Use the scale key `'Celsius or c'` if the temperature number from `Celsius`.

         USES:
         -----
            If you want to switch between temperature gauges,
            Use the name of the scale you want to convert to,
            then put the temperature and the symbol of the scale from which this temperature came.

        
        CREATED BY: `Muhammed Alkohawaldeh`
        ----------------------------------
        CLASS VERSION: `0.1.0-pre-Alpha`
        --------------------------------
    
    """
        
        # Not sure about it yet
    def __str__(self):
        return self.__Temperature
        
    @staticmethod
    def Kelvin(_Temperature: super_listup, *, Key: key_list ='celsius') -> Union[float, list[float]]:
        """
            This function converts the entered temperature `into Kelvin`.

            It's take two args:
            -----------------
                        Key: as `Key = 'any key'` | Temperature
                        
            Types of args:
            -------------
                        Key as `List[string]` or `string`.
                        Temperature as `List[Integer]`, `Integer`, `List[Float]`, `string of integer`, `string of floats` or `floats`.

            Examples:
            ---------
                >>> import scince as sc
                >>> #  Correct 
                >>> print(sc.Temperature.Kelvin(345, Key='f'))
                >>> print(sc.Temperature.Kelvin([435, 343, 531], Key='f'))
                >>> print(sc.Temperature.Kelvin([435, 343, 531], Key=['f', 'f', 'f']))
                >>> print(sc.Temperature.Kelvin([435, 343, 531], Key=['f', 'k', 'c']))

                >>> #  incorrect
                >>> print(sc.Temperature.Kelvin(234, Key=['f', 'k', 'c']))
                >>> print(sc.Temperature.Kelvin([234], Key=['f', 'k', 'c']))
                >>> print(sc.Temperature.Kelvin(234, Key=['f']))
                >>> print(sc.Temperature.Kelvin([435, 343, 531], Key=['f']))
                >>> print(sc.Temperature.Kelvin([435, 343, 531], Key=['f']))

            Notice:
            ------
                If the key is of the type of a list of texts, 
                then the temperatures must be of the type of a list of numbers of the same length,
                and vice versa is not true.
        """
        if type(Key) == NoneType:
            Key = 'celsius'
            Temperature.Kelvin(_Temperature, Key = Key)

        if type(Key) == list and type(_Temperature) == list:

            if type(_Temperature[0]) not in [int, float] and type(Key[0]) != str:

                _Temperature = list(map(int, _Temperature))
                Key = list(map(str, Key))
                Temperature.Kelvin(_Temperature, Key = Key)

            if type(_Temperature[0]) not in [int, float]:
                    _Temperature = list(map(int, _Temperature))
                    Temperature.Kelvin(_Temperature, Key = Key)

            if type(Key[0]) != str:
                Key = list(map(str, Key))
                Temperature.Kelvin(_Temperature, Key = Key)

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
                            result.append('Undefined') # KNE: Key Not Exist
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
                            result.append('Undefined') # KNE: Key Not Exist
                    return result

        raise _KeyTypeError(Key, _Temperature)

    @staticmethod
    def Celsius(_Temperature: super_listup, *, Key: key_list ='celsius') -> float:
        """
            This function converts the entered temperature into Celsius
            
            It's take two args:
            -----------------
                        Key: as `Key = 'any key'` | Temperature
                        
            Types of args:
            -------------
                        Key as `List[string]` or `string`.
                        Temperature as `List[Integer]`, `Integer`, `List[Float]`, `string of integer`, `string of floats` or `floats`.

            Examples:
            ---------
                >>> import scince as sc
                >>> #  Correct 
                >>> print(sc.Temperature.Celsius(345, Key='f'))
                >>> print(sc.Temperature.Celsius([435, 343, 531], Key='f'))
                >>> print(sc.Temperature.Celsius([435, 343, 531], Key=['f', 'f', 'f']))
                >>> print(sc.Temperature.Celsius([435, 343, 531], Key=['f', 'k', 'c']))

                >>> #  incorrect
                >>> print(sc.Temperature.Celsius(234, Key=['f', 'k', 'c']))
                >>> print(sc.Temperature.Celsius([234], Key=['f', 'k', 'c']))
                >>> print(sc.Temperature.Celsius(234, Key=['f']))
                >>> print(sc.Temperature.Celsius([435, 343, 531], Key=['f']))
                >>> print(sc.Temperature.Celsius([435, 343, 531], Key=['f']))

            Notice:
            ------
                If the key is of the type of a list of texts, 
                then the temperatures must be of the type of a list of numbers of the same length,
                and vice versa is not true.
        """
        if type(Key) == NoneType:
            Key = 'celsius'
            Temperature.Celsius(_Temperature, Key = Key)

        if type(Key) == list and type(_Temperature) == list:

            if type(_Temperature[0]) not in [int, float] and type(Key[0]) != str:

                _Temperature = list(map(int, _Temperature))
                Key = list(map(str, Key))
                Temperature.Celsius(_Temperature, Key = Key)

            if type(_Temperature[0]) not in [int, float]:
                    _Temperature = list(map(int, _Temperature))
                    Temperature.Celsius(_Temperature, Key = Key)
                    
            if type(Key[0]) != str:
                Key = list(map(str, Key))
                Temperature.Celsius(_Temperature, Key = Key)

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
                            result.append('Undefined') # KNE: Key Not Exist
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

            if type(_Temperature[0]) not in [int, float]:
                    _Temperature = list(map(int, _Temperature))
                    Temperature.Celsius(_Temperature, Key = Key)

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
                    result.append('Undefined') # KNE: Key Not Exist
            return result

        raise _KeyTypeError(Key, _Temperature)

    @staticmethod
    def Fahrenheit(_Temperature: super_listup, *, Key: key_list ='celsius') -> float:
        """
            This function converts the entered temperature into Fahrenheit

            It's take two args:
            -----------------
                        Key: as `Key = 'any key'` | Temperature
                        
            Types of args:
            -------------
                        Key as `List[string]` or `string`.
                        Temperature as `List[Integer]`, `Integer`, `List[Float]`, `string of integer`, `string of floats` or `floats`.

            Examples:
            ---------
                >>> import scince as sc
                >>> #  Correct 
                >>> print(sc.Temperature.Fahrenheit(345, Key='f'))
                >>> print(sc.Temperature.Fahrenheit([435, 343, 531], Key='f'))
                >>> print(sc.Temperature.Fahrenheit([435, 343, 531], Key=['f', 'f', 'f']))
                >>> print(sc.Temperature.Fahrenheit([435, 343, 531], Key=['f', 'k', 'c']))

                >>> #  incorrect
                >>> print(sc.Temperature.Fahrenheit(234, Key=['f', 'k', 'c']))
                >>> print(sc.Temperature.Fahrenheit([234], Key=['f', 'k', 'c']))
                >>> print(sc.Temperature.Fahrenheit(234, Key=['f']))
                >>> print(sc.Temperature.Fahrenheit([435, 343, 531], Key=['f']))
                >>> print(sc.Temperature.Fahrenheit([435, 343, 531], Key=['f']))

            Notice:
            ------
                If the key is of the type of a list of texts, 
                then the temperatures must be of the type of a list of numbers of the same length,
                and vice versa is not true.
        """
        if type(Key) == NoneType:
            Key = 'celsius'
            Temperature.Fahrenheit(_Temperature, Key = Key)

        if type(Key) == list and type(_Temperature) == list:

            if type(_Temperature[0]) not in [int, float] and type(Key[0]) != str:

                _Temperature = list(map(int, _Temperature))
                Key = list(map(str, Key))
                Temperature.Fahrenheit(_Temperature, Key = Key)

            if type(_Temperature[0]) not in [int, float]:
                    _Temperature = list(map(int, _Temperature))
                    Temperature.Fahrenheit(_Temperature, Key = Key)
                    
            if type(Key[0]) != str:
                Key = list(map(str, Key))
                Temperature.Fahrenheit(_Temperature, Key = Key)

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
                            result.append('Undefined') # KNE: Key Not Exist
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

            if type(_Temperature[0]) not in [int, float]:
                    _Temperature = list(map(int, _Temperature))
                    Temperature.Fahrenheit(_Temperature, Key = Key)

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
                    result.append('Undefined') # KNE: Key Not Exist
            return result

        raise _KeyTypeError(Key, _Temperature)


    @staticmethod
    def Rankin(_Temperature: super_listup, *, Key: key_list ='celsius') -> float:
        """
            This function converts the entered temperature into Rankin

            It's take two args:
            -----------------
                        Key: as `Key = 'any key'` | Temperature
                        
            Types of args:
            -------------
                        Key as `List[string]` or `string`.
                        Temperature as `List[Integer]`, `Integer`, `List[Float]`, `string of integer`, `string of floats` or `floats`.

            Examples:
            ---------
                >>> import scince as sc
                >>> #  Correct 
                >>> print(sc.Temperature.Rankin(345, Key='f'))
                >>> print(sc.Temperature.Rankin([435, 343, 531], Key='f'))
                >>> print(sc.Temperature.Rankin([435, 343, 531], Key=['f', 'f', 'f']))
                >>> print(sc.Temperature.Rankin([435, 343, 531], Key=['f', 'k', 'c']))

                >>> #  incorrect
                >>> print(sc.Temperature.Rankin(234, Key=['f', 'k', 'c']))
                >>> print(sc.Temperature.Rankin([234], Key=['f', 'k', 'c']))
                >>> print(sc.Temperature.Rankin(234, Key=['f']))
                >>> print(sc.Temperature.Rankin([435, 343, 531], Key=['f']))
                >>> print(sc.Temperature.Rankin([435, 343, 531], Key=['f']))

            Notice:
            ------
                If the key is of the type of a list of texts, 
                then the temperatures must be of the type of a list of numbers of the same length,
                and vice versa is not true.
        """
        if type(Key) == NoneType:
            Key = 'celsius'
            Temperature.Rankin(_Temperature, Key = Key)

        if type(Key) == list and type(_Temperature) == list:

            if type(_Temperature[0]) not in [int, float] and type(Key[0]) != str:

                _Temperature = list(map(int, _Temperature))
                Key = list(map(str, Key))
                Temperature.Rankin(_Temperature, Key = Key)

            if type(_Temperature[0]) not in [int, float]:
                    _Temperature = list(map(int, _Temperature))
                    Temperature.Rankin(_Temperature, Key = Key)
                    
            if type(Key[0]) != str:
                Key = list(map(str, Key))
                Temperature.Rankin(_Temperature, Key = Key)

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
                            result.append('Undefined') # KNE: Key Not Exist
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

            if type(_Temperature[0]) not in [int, float]:
                    _Temperature = list(map(int, _Temperature))
                    Temperature.Rankin(_Temperature, Key = Key)

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
                    result.append('Undefined') # KNE: Key Not Exist
            return result

        raise   _KeyTypeError(Key, _Temperature)


# __all__ = ['Temperature', 'Kelvin', 'Celsius', 'Fahrenheit', 'Rankin']
# for i in range(100000):
#     f = i

# print(Temperature.Kelvin(1234.324234325, Key = "kelvin"))