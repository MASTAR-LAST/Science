"""
TODO: MAKE A DOC FOR THIS FILE
"""

from .temperature_error import _TemperatureError, _UndefinedStateError, _KeyTypeError
from typing import Union
from decimal import Decimal

def fahrenMethod(target, status: str | None) -> Decimal:
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
            All functions take two arguments (Temperature, Key)

                Available FUNCTIONS:
                            Func 1:  Kelvin(here but the number of temperature, here but the scale key).
                            Func 2:  Fahrenheit(here but the number of temperature, here but the scale key).
                            Func 3:  Celsius(here but the number of temperature, here but the scale key).

                Available CASES:
                            Case 1:  Use the scale key 'K or k' if the temperature number from Kelvin. 
                            Case 2:  Use the scale key 'F or f' if the temperature number from Fahrenheit.
                            Case 3:  Use the scale key 'C or c' if the temperature number from Celsius.

         USES:
            If you want to switch between temperature gauges,
            Use the name of the scale you want to convert to,
            then put the temperature and the symbol of the scale from which this temperature came.

        
        CREATED BY: Muhammed Alkohawaldeh
        CLASS VERSION: 0.0.1(beta)
    
    """

    global kelvinConstant
    kelvinConstant = Decimal('273.15')

   #TODO:   عدل على الدالة __init__ لكي تسمح بصنع مقاييس حرارة مختلفة بالاسم الذي تريد بالطريقة التي تريد 
    def __init__(self, Temperature, Key):
        self.__Temperature = Temperature
        self.__Key = Key
        
        # Not sure about it yet
    def __str__(self):
        return self.__Temperature
        

    @staticmethod
    def Kelvin(Temperature: Union[int, float], Key: str) -> float:
        """
            This function converts the entered temperature into Kelvin
        
        """
        if type(Key) != str:
            raise _KeyTypeError(Key)

        Temperature = float(Temperature)
        Temperature = Decimal(f'{Temperature}')
        if Key in ['K', 'k', 'Kelvin']:
            return float(Temperature)
        elif Key in ['C', 'c', 'Celsius']:
            return float(Temperature + kelvinConstant)
        elif Key in ['F', 'f', 'Fahrenheit']:
            Temperature = fahrenMethod(target = Temperature, status = 'to kelvin&celsius')
            Temperature += kelvinConstant 
            return float(Temperature)

        raise _TemperatureError(Key)


    @staticmethod
    def Celsius(Temperature: Union[int, float], Key: str) -> float:
        """
            This function converts the entered temperature into Celsius
        
        """
        if type(Key) != str:
            raise _KeyTypeError(Key)

        Temperature = float(Temperature)
        Temperature = Decimal(f'{Temperature}')
        if Key in ['K', 'k', 'Kelvin']:
            return float(Temperature - kelvinConstant)
        elif Key in ['C', 'c', 'Celsius']:
            return float(Temperature)
        elif Key in ['F', 'f', 'Fahrenheit']:
            return float(fahrenMethod(target = Temperature, status = 'to kelvin&celsius'))
       
        raise _TemperatureError(Key)


    @staticmethod
    def Fahrenheit(Temperature: Union[int, float], Key: str) -> float:
        """
            This function converts the entered temperature into Fahrenheit
        
        """
        if type(Key) != str:
            raise _KeyTypeError(Key)
            
        Temperature = float(Temperature)
        Temperature = Decimal(f'{Temperature}')
        if Key in ['K', 'k', 'Kelvin']:
            Temperature -= kelvinConstant # transformed from Kelvin to Celsius
            Temperature = fahrenMethod(target = Temperature, status = 'to fehren') # transformed from Celsius to Fahrenheit
            return float(Temperature)
        elif Key in ['C', 'c', 'Celsius']:
            return float(fahrenMethod(target = Temperature, status = 'to fehren')) # transformed from Celsius to Fahrenheit
        elif Key in ['F', 'f', 'Fahrenheit']:
            return float(Temperature)
       
        raise _TemperatureError(Key)
