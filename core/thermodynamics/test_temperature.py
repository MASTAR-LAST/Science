try: 
   from temperature import Temperature as tm
   from errors.ECUtm import (_KeyTypeError, _TemperatureError, _UndefinedStateError, _InstabilityError)
   import unittest
except ImportError:
   from .temperature import Temperature as tm
   from .errors.ECUtm import (_KeyTypeError, _TemperatureError, _UndefinedStateError, _InstabilityError)
   import unittest

#    TODO: Celisius Tests

class TestCelsius(unittest.TestCase):
    
   def test_Fahrenheit_to_Celsius(self):
    #Test Celsius input/output Temperature when the KEY is Fahrenheit
      self.assertEqual(tm.Celsius(23,Key='F'), -5)
      self.assertEqual(tm.Celsius(0.5,Key='F'), -17.5) 
      self.assertEqual(tm.Celsius(0,Key='F'), -17.77777777777778)
      self.assertEqual(tm.Celsius(-0.4,Key='F'), -18)
      self.assertEqual(tm.Celsius(-4,Key='F'), -20)

   def test_Celsius_to_Celsius(self):
    #Test Celsius input/output Temperature when the KEY is Celsius
      self.assertEqual(tm.Celsius(23,Key='C'), 23)
      self.assertEqual(tm.Celsius(0.5,Key='C'), 0.5) 
      self.assertEqual(tm.Celsius(0,Key='C'), 0)
      self.assertEqual(tm.Celsius(-0.4,Key='C'), -0.4)
      self.assertEqual(tm.Celsius(-4,Key='C'), -4)

   def test_Kelvin_to_Celsius(self):
    #Test Celsius input/output Temperature when the KEY is Celsius
      self.assertEqual(tm.Celsius(23,Key='K'), -250.15)
      self.assertEqual(tm.Celsius(0.5,Key='K'), -272.65) 
      self.assertEqual(tm.Celsius(0,Key='K'), -273.15)
      self.assertEqual(tm.Celsius(-0.4,Key='K'), -273.55)
      self.assertEqual(tm.Celsius(-4,Key='K'), -277.15)

   def test_Celsius_Key_Type_error_raise(self):
    #Test Celsius input/output Temperature that must raise _KeyTypeError
      self.assertRaises(_KeyTypeError, tm.Celsius, 23, Key=7)
      self.assertRaises(_KeyTypeError, tm.Celsius, 23, Key=7j)    
      self.assertRaises(_KeyTypeError, tm.Celsius, 23, Key=True)    
      self.assertRaises(_KeyTypeError, tm.Celsius, 23, Key=False)    
      self.assertRaises(_KeyTypeError, tm.Celsius, 23, Key=7.7)    
      self.assertRaises(_KeyTypeError, tm.Celsius, 23, Key=[3])    
      self.assertRaises(_KeyTypeError, tm.Celsius, 23, Key={23})
      self.assertRaises(_KeyTypeError, tm.Celsius, 23, Key=(98,23)) 
      self.assertRaises(_KeyTypeError, tm.Celsius, 23, Key={98})

   def test_Celsius_Type_error_raise(self):
    #Test Celsius input/output Temperature that must raise _KeyTypeError
      self.assertRaises(_KeyTypeError, tm.Celsius, False, Key='R')
      self.assertRaises(_KeyTypeError, tm.Celsius, True, Key='K')    
      self.assertRaises(_KeyTypeError, tm.Celsius, 7j, Key='F')    
      self.assertRaises(_KeyTypeError, tm.Celsius, None, Key='C')    
      self.assertRaises(_KeyTypeError, tm.Celsius, {23}, Key='K')
      self.assertRaises(_KeyTypeError, tm.Celsius, (98,23), Key='F') 
      self.assertRaises(_KeyTypeError, tm.Celsius, {98}, Key='C')

###########################################################################################

#     Fahrenheit Tests 

class TestFahrenheit(unittest.TestCase):

   def test_Fahrenheit_to_Fahrenheit(self):
    #Test Fahrenheit input/output Temperature when the Key is Fahrenheit
      self.assertEqual(tm.Fahrenheit(23,Key='F'), 23)
      self.assertEqual(tm.Fahrenheit(0.5,Key='F'), 0.5)
      self.assertEqual(tm.Fahrenheit(0,Key='F'), 0)
      self.assertEqual(tm.Fahrenheit(-0.4,Key='F'), -0.4)
      self.assertEqual(tm.Fahrenheit(-4,Key='F'), -4)

   def test_Celsius_to_Fahrenheit(self):
    #Test Fahrenheit input/output Temperature when the Key is Celsius
      self.assertEqual(tm.Fahrenheit(23,Key='C'), 73.4)
      self.assertEqual(tm.Fahrenheit(0.5,Key='C'), 32.9)
      self.assertEqual(tm.Fahrenheit(0,Key='C'), 32)
      self.assertEqual(tm.Fahrenheit(-0.4,Key='C'), 31.28)
      self.assertEqual(tm.Fahrenheit(-4,Key='C'), 24.8)

   def test_Kelvin_to_Fahrenheit(self):
    #Test Fahrenheit input/output Temperature when the Key is Kelvin
      self.assertEqual(tm.Fahrenheit(23,Key='K'), -418.27)
      self.assertEqual(tm.Fahrenheit(0.5,Key='K'), -458.77)
      self.assertEqual(tm.Fahrenheit(0,Key='K'), -459.67)
      self.assertEqual(tm.Fahrenheit(-0.4,Key='K'), -460.39)
      self.assertEqual(tm.Fahrenheit(-4,Key='K'), -466.87)

   def test_Fahrenheit_Key_Type_error_raise(self):
    #Test Fahrenheit input/output Temperature that must raise _KeyTypeError
      self.assertRaises(_KeyTypeError, tm.Fahrenheit, 23, Key=7j)    
      self.assertRaises(_KeyTypeError, tm.Fahrenheit, 23, Key=7)
      self.assertRaises(_KeyTypeError, tm.Fahrenheit, 23, Key=True)    
      self.assertRaises(_KeyTypeError, tm.Fahrenheit, 23, Key=False)    
      self.assertRaises(_KeyTypeError, tm.Fahrenheit, 23, Key=7.7)    
      self.assertRaises(_KeyTypeError, tm.Fahrenheit, 23, Key=[3])    
      self.assertRaises(_KeyTypeError, tm.Fahrenheit, 23, Key={23})
      self.assertRaises(_KeyTypeError, tm.Fahrenheit, 23, Key=(98,23)) 
      self.assertRaises(_KeyTypeError, tm.Fahrenheit, 23, Key={98})

   def test_Fahrenheit_Type_error_raise(self):
    #Test Fahrenheit input/output Temperature that must raise _KeyTypeError
      self.assertRaises(_KeyTypeError, tm.Fahrenheit, False, Key='R')
      self.assertRaises(_KeyTypeError, tm.Fahrenheit, True, Key='K')    
      self.assertRaises(_KeyTypeError, tm.Fahrenheit, 7j, Key='F')    
      self.assertRaises(_KeyTypeError, tm.Fahrenheit, None, Key='C')    
      self.assertRaises(_KeyTypeError, tm.Fahrenheit, {23}, Key='K')
      self.assertRaises(_KeyTypeError, tm.Fahrenheit, (98,23), Key='F') 
      self.assertRaises(_KeyTypeError, tm.Fahrenheit, {98}, Key='C')    

#####################################################################################

#     Kelvin Tests

class TestKelvin(unittest.TestCase):

   def test_Fahrenheit_to_Kelvin(self):
    #Test Kelvin input/output Temperature when the Key is Fahrenheit
      self.assertEqual(tm.Kelvin(23,Key='F'), 268.15)
      self.assertEqual(tm.Kelvin(0.5,Key='F'), 255.65)
      self.assertEqual(tm.Kelvin(0,Key='F'), 255.37222222222223)
      self.assertEqual(tm.Kelvin(-0.4,Key='F'), 255.15)
      self.assertEqual(tm.Kelvin(-4,Key='F'), 253.15)

   def test_Celsius_to_Kelvin(self):
    #Test Kelvin input/output Temperature when the Key is Celsius
      self.assertEqual(tm.Kelvin(23,Key='C'), 296.15)
      self.assertEqual(tm.Kelvin(0.5,Key='C'), 273.65)
      self.assertEqual(tm.Kelvin(0,Key='C'), 273.15)
      self.assertEqual(tm.Kelvin(-0.4,Key='C'), 272.75)
      self.assertEqual(tm.Kelvin(-4,Key='C'), 269.15)

   def test_Kelvin_to_Kelvin(self):
    #Test Kelvin input/output Temperature when the Key is Kelvin
      self.assertEqual(tm.Kelvin(23,Key='K'), 23)
      self.assertEqual(tm.Kelvin(0.5,Key='K'), 0.5)
      self.assertEqual(tm.Kelvin(0,Key='K'), 0)
      self.assertEqual(tm.Kelvin(-0.4,Key='K'), -0.4)
      self.assertEqual(tm.Kelvin(-4,Key='K'), -4)

   def test_Kelvin_Key_Type_error_raise(self):
    #Test Kelvin input/output Temperature that must raise _KeyTypeError
      self.assertRaises(_KeyTypeError, tm.Kelvin, 23, Key=7)
      self.assertRaises(_KeyTypeError, tm.Kelvin, 23, Key=7j)    
      self.assertRaises(_KeyTypeError, tm.Kelvin, 23, Key=True)    
      self.assertRaises(_KeyTypeError, tm.Kelvin, 23, Key=False)    
      self.assertRaises(_KeyTypeError, tm.Kelvin, 23, Key=7.7)    
      self.assertRaises(_KeyTypeError, tm.Kelvin, 23, Key=[3])    
      self.assertRaises(_KeyTypeError, tm.Kelvin, 23, Key={23})
      self.assertRaises(_KeyTypeError, tm.Kelvin, 23, Key=(98,23)) 
      self.assertRaises(_KeyTypeError, tm.Kelvin, 23, Key={98})

   def test_Kelvin_Type_error_raise(self):
    #Test Kelvin input/output Temperature that must raise _KeyTypeError
      self.assertRaises(_KeyTypeError, tm.Kelvin, False, Key='R')
      self.assertRaises(_KeyTypeError, tm.Kelvin, True, Key='K')    
      self.assertRaises(_KeyTypeError, tm.Kelvin, 7j, Key='F')    
      self.assertRaises(_KeyTypeError, tm.Kelvin, None, Key='C')    
      self.assertRaises(_KeyTypeError, tm.Kelvin, {23}, Key='K')
      self.assertRaises(_KeyTypeError, tm.Kelvin, (98,23), Key='F') 
      self.assertRaises(_KeyTypeError, tm.Kelvin, {98}, Key='C') 

###########################################################################

#           Rankin Tests

class TestRankin(unittest.TestCase):

   def test_Fahrenheit_to_Rankin(self):
    #Test Rankin input/output Temperature when the Key is Fahrenheit
      self.assertEqual(tm.Rankin(23,Key='F'), -9)
      self.assertEqual(tm.Rankin(0.5,Key='F'), -31.5)
      self.assertEqual(tm.Rankin(0,Key='F'), -32.0)
      self.assertEqual(tm.Rankin(-0.4,Key='F'), -32.4)
      self.assertEqual(tm.Rankin(-4,Key='F'), -36)

   def test_Celsius_to_Rankin(self):
    #Test Rankin input/output Temperature when the Key is Celsius
      self.assertEqual(tm.Rankin(23,Key='C'), 533.07)
      self.assertEqual(tm.Rankin(0.5,Key='C'), 492.57)
      self.assertEqual(tm.Rankin(0,Key='C'), 491.67)
      self.assertEqual(tm.Rankin(-0.4,Key='C'), 490.95)
      self.assertEqual(tm.Rankin(-4,Key='C'), 484.47)

   def test_Kelvin_to_Rankin(self):
    #Test Rankin input/output Temperature when the Key is Kelvin
      self.assertEqual(tm.Rankin(23,Key='K'), 41.4)
      self.assertEqual(tm.Rankin(0.5,Key='K'), 0.9)
      self.assertEqual(tm.Rankin(0,Key='K'), 0)
      self.assertEqual(tm.Rankin(-0.4,Key='K'), -0.72)
      self.assertEqual(tm.Rankin(-4,Key='K'), -7.2)

   def test_Rankin_to_Rankin(self):
    #Test Rankin input/output Temperature when the Key is Rankin
      self.assertEqual(tm.Rankin(23,Key='R'), 23)
      self.assertEqual(tm.Rankin(0.5,Key='R'), 0.5)
      self.assertEqual(tm.Rankin(0,Key='R'), 0)
      self.assertEqual(tm.Rankin(-0.4,Key='R'), -0.4)
      self.assertEqual(tm.Rankin(-4,Key='R'), -4)

   def test_Rankin_Temperature_error_raise(self):
    #Test Rankin input/output Temperature that must raise _TemperatureError
      self.assertRaises(_TemperatureError, tm.Rankin, 23, Key='t')
      self.assertRaises(_TemperatureError, tm.Rankin, 23, Key='')

   def test_Rankin_KeyType_error_raise_Key(self):
    #Test Rankin input/output Temperature that must raise _KeyTypeError
      self.assertRaises(_KeyTypeError, tm.Rankin, 23, Key=7)
      self.assertRaises(_KeyTypeError, tm.Rankin, 23, Key=7j)    
      self.assertRaises(_KeyTypeError, tm.Rankin, 23, Key=True)    
      self.assertRaises(_KeyTypeError, tm.Rankin, 23, Key=False)    
      self.assertRaises(_KeyTypeError, tm.Rankin, 23, Key=7.7)    
      self.assertRaises(_KeyTypeError, tm.Rankin, 23, Key=[3])    
      self.assertRaises(_KeyTypeError, tm.Rankin, 23, Key={23})
      self.assertRaises(_KeyTypeError, tm.Rankin, 23, Key=(98,23)) 
      self.assertRaises(_KeyTypeError, tm.Rankin, 23, Key={98})

   def test_Rankin_KeyType_error_raise_temp(self):
    #Test Rankin input/output Temperature that must raise _KeyTypeError
      self.assertRaises(_KeyTypeError, tm.Rankin, False, Key='R')
      self.assertRaises(_KeyTypeError, tm.Rankin, True, Key='K')    
      self.assertRaises(_KeyTypeError, tm.Rankin, 7j, Key='F')    
      self.assertRaises(_KeyTypeError, tm.Rankin, None, Key='C')    
      self.assertRaises(_KeyTypeError, tm.Rankin, {23}, Key='K')
      self.assertRaises(_KeyTypeError, tm.Rankin, (98,23), Key='F') 
      self.assertRaises(_KeyTypeError, tm.Rankin, {98}, Key='C') 


if __name__ == '__main__':
   unittest.main()