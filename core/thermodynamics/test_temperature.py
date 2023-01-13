try: 
   from temperature import Temperature as tm
   from temperature_error import (_KeyTypeError, _TemperatureError, _UndefinedStateError)
except ImportError:
   from .temperature import Temperature as tm
   from .temperature_error import (_KeyTypeError, _TemperatureError, _UndefinedStateError)
import unittest

#     Celisius Tests

class TestCelsius(unittest.TestCase):
    
   def test_Fahrenheit_to_Celsius(self):
    #Test Celsius input/output Temperature when the KEY is Fahrenheit
      self.assertEqual(tm.Celsius(23,'F'), -5)
      self.assertEqual(tm.Celsius(0.5,'F'), -17.5) 
      self.assertEqual(tm.Celsius(0,'F'), -17.77777777777778)
      self.assertEqual(tm.Celsius(-0.4,'F'), -18)
      self.assertEqual(tm.Celsius(-4,'F'), -20)

   def test_Celsius_to_Celsius(self):
    #Test Celsius input/output Temperature when the KEY is Celsius
      self.assertEqual(tm.Celsius(23,'C'), 23)
      self.assertEqual(tm.Celsius(0.5,'C'), 0.5) 
      self.assertEqual(tm.Celsius(0,'C'), 0)
      self.assertEqual(tm.Celsius(-0.4,'C'), -0.4)
      self.assertEqual(tm.Celsius(-4,'C'), -4)

   def test_Kelvin_to_Celsius(self):
    #Test Celsius input/output Temperature when the KEY is Celsius
      self.assertEqual(tm.Celsius(23,'K'), -250.15)
      self.assertEqual(tm.Celsius(0.5,'K'), -272.65) 
      self.assertEqual(tm.Celsius(0,'K'), -273.15)
      self.assertEqual(tm.Celsius(-0.4,'K'), -273.55)
      self.assertEqual(tm.Celsius(-4,'K'), -277.15)

   def test_Celsius_Key_Type_error_raise(self):
    #Test Celsius input/output Temperature that must raise _KeyTypeError
      self.assertRaises(_KeyTypeError, tm.Celsius, 23, 7)
      self.assertRaises(_KeyTypeError, tm.Celsius, 23, 7j)    
      self.assertRaises(_KeyTypeError, tm.Celsius, 23, True)    
      self.assertRaises(_KeyTypeError, tm.Celsius, 23, False)    
      self.assertRaises(_KeyTypeError, tm.Celsius, 23, 7.7)    
      self.assertRaises(_KeyTypeError, tm.Celsius, 23, None)
      self.assertRaises(_KeyTypeError, tm.Celsius, 23, [3])    
      self.assertRaises(_KeyTypeError, tm.Celsius, 23, {23})
      self.assertRaises(_KeyTypeError, tm.Celsius, 23, (98,23)) 
      self.assertRaises(_KeyTypeError, tm.Celsius, 23, set([98]))

   def test_Celsius_Type_error_raise(self):
    #Test Celsius input/output Temperature that must raise _KeyTypeError
      self.assertRaises(TypeError, tm.Celsius, False, 'R')
      self.assertRaises(TypeError, tm.Celsius, True, 'K')    
      self.assertRaises(TypeError, tm.Celsius, 7j, 'F')    
      self.assertRaises(TypeError, tm.Celsius, None, 'C')    
      self.assertRaises(TypeError, tm.Celsius, [3], 'R')    
      self.assertRaises(TypeError, tm.Celsius, {23}, 'K')
      self.assertRaises(TypeError, tm.Celsius, (98,23), 'F') 
      self.assertRaises(TypeError, tm.Celsius, set([98]), 'C')

###########################################################################################

#     Fahrenheit Tests 

class TestFahrenheit(unittest.TestCase):

   def test_Fahrenheit_to_Fahrenheit(self):
    #Test Fahrenheit input/output Temperature when the Key is Fahrenheit
      self.assertEqual(tm.Fahrenheit(23,'F'), 23)
      self.assertEqual(tm.Fahrenheit(0.5,'F'), 0.5)
      self.assertEqual(tm.Fahrenheit(0,'F'), 0)
      self.assertEqual(tm.Fahrenheit(-0.4, 'F'), -0.4)
      self.assertEqual(tm.Fahrenheit(-4,'F'), -4)

   def test_Celsius_to_Fahrenheit(self):
    #Test Fahrenheit input/output Temperature when the Key is Celsius
      self.assertEqual(tm.Fahrenheit(23,'C'), 73.4)
      self.assertEqual(tm.Fahrenheit(0.5,'C'), 32.9)
      self.assertEqual(tm.Fahrenheit(0,'C'), 32)
      self.assertEqual(tm.Fahrenheit(-0.4, 'C'), 31.28)
      self.assertEqual(tm.Fahrenheit(-4,'C'), 24.8)

   def test_Kelvin_to_Fahrenheit(self):
    #Test Fahrenheit input/output Temperature when the Key is Kelvin
      self.assertEqual(tm.Fahrenheit(23,'K'), -418.27)
      self.assertEqual(tm.Fahrenheit(0.5,'K'), -458.77)
      self.assertEqual(tm.Fahrenheit(0,'K'), -459.67)
      self.assertEqual(tm.Fahrenheit(-0.4,'K'), -460.39)
      self.assertEqual(tm.Fahrenheit(-4,'K'), -466.87)

   def test_Fahrenheit_Key_Type_error_raise(self):
    #Test Fahrenheit input/output Temperature that must raise _KeyTypeError
      self.assertRaises(_KeyTypeError, tm.Fahrenheit, 23, 7j)    
      self.assertRaises(_KeyTypeError, tm.Fahrenheit, 23, 7)
      self.assertRaises(_KeyTypeError, tm.Fahrenheit, 23, True)    
      self.assertRaises(_KeyTypeError, tm.Fahrenheit, 23, False)    
      self.assertRaises(_KeyTypeError, tm.Fahrenheit, 23, 7.7)    
      self.assertRaises(_KeyTypeError, tm.Fahrenheit, 23, None)
      self.assertRaises(_KeyTypeError, tm.Fahrenheit, 23, [3])    
      self.assertRaises(_KeyTypeError, tm.Fahrenheit, 23, {23})
      self.assertRaises(_KeyTypeError, tm.Fahrenheit, 23, (98,23)) 
      self.assertRaises(_KeyTypeError, tm.Fahrenheit, 23, set([98]))

   def test_Fahrenheit_Type_error_raise(self):
    #Test Fahrenheit input/output Temperature that must raise _KeyTypeError
      self.assertRaises(TypeError, tm.Fahrenheit, False, 'R')
      self.assertRaises(TypeError, tm.Fahrenheit, True, 'K')    
      self.assertRaises(TypeError, tm.Fahrenheit, 7j, 'F')    
      self.assertRaises(TypeError, tm.Fahrenheit, None, 'C')    
      self.assertRaises(TypeError, tm.Fahrenheit, [3], 'R')    
      self.assertRaises(TypeError, tm.Fahrenheit, {23}, 'K')
      self.assertRaises(TypeError, tm.Fahrenheit, (98,23), 'F') 
      self.assertRaises(TypeError, tm.Fahrenheit, set([98]), 'C')    

#####################################################################################

#     Kelvin Tests

class TestKelvin(unittest.TestCase):

   def test_Fahrenheit_to_Kelvin(self):
    #Test Kelvin input/output Temperature when the Key is Fahrenheit
      self.assertEqual(tm.Kelvin(23,'F'), 268.15)
      self.assertEqual(tm.Kelvin(0.5,'F'), 255.65)
      self.assertEqual(tm.Kelvin(0,'F'), 255.37222222222223)
      self.assertEqual(tm.Kelvin(-0.4, 'F'), 255.15)
      self.assertEqual(tm.Kelvin(-4,'F'), 253.15)

   def test_Celsius_to_Kelvin(self):
    #Test Kelvin input/output Temperature when the Key is Celsius
      self.assertEqual(tm.Kelvin(23,'C'), 296.15)
      self.assertEqual(tm.Kelvin(0.5,'C'), 273.65)
      self.assertEqual(tm.Kelvin(0,'C'), 273.15)
      self.assertEqual(tm.Kelvin(-0.4,'C'), 272.75)
      self.assertEqual(tm.Kelvin(-4,'C'), 269.15)

   def test_Kelvin_to_Kelvin(self):
    #Test Kelvin input/output Temperature when the Key is Kelvin
      self.assertEqual(tm.Kelvin(23,'K'), 23)
      self.assertEqual(tm.Kelvin(0.5,'K'), 0.5)
      self.assertEqual(tm.Kelvin(0,'K'), 0)
      self.assertEqual(tm.Kelvin(-0.4,'K'), -0.4)
      self.assertEqual(tm.Kelvin(-4,'K'), -4)

   def test_Kelvin_Key_Type_error_raise(self):
    #Test Kelvin input/output Temperature that must raise _KeyTypeError
      self.assertRaises(_KeyTypeError, tm.Kelvin, 23, 7)
      self.assertRaises(_KeyTypeError, tm.Kelvin, 23, 7j)    
      self.assertRaises(_KeyTypeError, tm.Kelvin, 23, True)    
      self.assertRaises(_KeyTypeError, tm.Kelvin, 23, False)    
      self.assertRaises(_KeyTypeError, tm.Kelvin, 23, 7.7)    
      self.assertRaises(_KeyTypeError, tm.Kelvin, 23, None)
      self.assertRaises(_KeyTypeError, tm.Kelvin, 23, [3])    
      self.assertRaises(_KeyTypeError, tm.Kelvin, 23, {23})
      self.assertRaises(_KeyTypeError, tm.Kelvin, 23, (98,23)) 
      self.assertRaises(_KeyTypeError, tm.Kelvin, 23, set([98]))

   def test_Kelvin_Type_error_raise(self):
    #Test Kelvin input/output Temperature that must raise _KeyTypeError
      self.assertRaises(TypeError, tm.Kelvin, False, 'R')
      self.assertRaises(TypeError, tm.Kelvin, True, 'K')    
      self.assertRaises(TypeError, tm.Kelvin, 7j, 'F')    
      self.assertRaises(TypeError, tm.Kelvin, None, 'C')    
      self.assertRaises(TypeError, tm.Kelvin, [3], 'R')    
      self.assertRaises(TypeError, tm.Kelvin, {23}, 'K')
      self.assertRaises(TypeError, tm.Kelvin, (98,23), 'F') 
      self.assertRaises(TypeError, tm.Kelvin, set([98]), 'C') 

###########################################################################

#           Rankin Tests

class TestRankin(unittest.TestCase):

   def test_Fahrenheit_to_Rankin(self):
    #Test Rankin input/output Temperature when the Key is Fahrenheit
      self.assertEqual(tm.Rankin(23,'F'), -9)
      self.assertEqual(tm.Rankin(0.5,'F'), -31.5)
      self.assertEqual(tm.Rankin(0,'F'), -32.0)
      self.assertEqual(tm.Rankin(-0.4, 'F'), -32.4)
      self.assertEqual(tm.Rankin(-4,'F'), -36)

   def test_Celsius_to_Rankin(self):
    #Test Rankin input/output Temperature when the Key is Celsius
      self.assertEqual(tm.Rankin(23,'C'), 533.07)
      self.assertEqual(tm.Rankin(0.5,'C'), 492.57)
      self.assertEqual(tm.Rankin(0,'C'), 491.67)
      self.assertEqual(tm.Rankin(-0.4,'C'), 490.95)
      self.assertEqual(tm.Rankin(-4,'C'), 484.47)

   def test_Kelvin_to_Rankin(self):
    #Test Rankin input/output Temperature when the Key is Kelvin
      self.assertEqual(tm.Rankin(23,'K'), 41.4)
      self.assertEqual(tm.Rankin(0.5,'K'), 0.9)
      self.assertEqual(tm.Rankin(0,'K'), 0)
      self.assertEqual(tm.Rankin(-0.4,'K'), -0.72)
      self.assertEqual(tm.Rankin(-4,'K'), -7.2)

   def test_Rankin_to_Rankin(self):
    #Test Rankin input/output Temperature when the Key is Rankin
      self.assertEqual(tm.Rankin(23,'R'), 23)
      self.assertEqual(tm.Rankin(0.5,'R'), 0.5)
      self.assertEqual(tm.Rankin(0,'R'), 0)
      self.assertEqual(tm.Rankin(-0.4,'R'), -0.4)
      self.assertEqual(tm.Rankin(-4,'R'), -4)

   def test_Rankin_Temperature_error_raise(self):
    #Test Rankin input/output Temperature that must raise _TemperatureError
      self.assertRaises(_TemperatureError, tm.Rankin, 23, 't')
      self.assertRaises(_TemperatureError, tm.Rankin, 23, '')

   def test_Rankin_Key_Type_error_raise(self):
    #Test Rankin input/output Temperature that must raise _KeyTypeError
      self.assertRaises(_KeyTypeError, tm.Rankin, 23, 7)
      self.assertRaises(_KeyTypeError, tm.Rankin, 23, 7j)    
      self.assertRaises(_KeyTypeError, tm.Rankin, 23, True)    
      self.assertRaises(_KeyTypeError, tm.Rankin, 23, False)    
      self.assertRaises(_KeyTypeError, tm.Rankin, 23, 7.7)    
      self.assertRaises(_KeyTypeError, tm.Rankin, 23, None)
      self.assertRaises(_KeyTypeError, tm.Rankin, 23, [3])    
      self.assertRaises(_KeyTypeError, tm.Rankin, 23, {23})
      self.assertRaises(_KeyTypeError, tm.Rankin, 23, (98,23)) 
      self.assertRaises(_KeyTypeError, tm.Rankin, 23, set([98]))

   def test_Rankin_Type_error_raise(self):
    #Test Rankin input/output Temperature that must raise _KeyTypeError
      self.assertRaises(TypeError, tm.Rankin, False, 'R')
      self.assertRaises(TypeError, tm.Rankin, True, 'K')    
      self.assertRaises(TypeError, tm.Rankin, 7j, 'F')    
      self.assertRaises(TypeError, tm.Rankin, None, 'C')    
      self.assertRaises(TypeError, tm.Rankin, [3], 'R')    
      self.assertRaises(TypeError, tm.Rankin, {23}, 'K')
      self.assertRaises(TypeError, tm.Rankin, (98,23), 'F') 
      self.assertRaises(TypeError, tm.Rankin, set([98]), 'C') 


if __name__ == '__main__':
   unittest.main()