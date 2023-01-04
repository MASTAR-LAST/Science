"""
Science
=======

Provides:

1. All information about all existing atoms.
2. All equations related to thermodynamics.
3. Convert between all temperature scales.
4. Building simple atomic interactions between all possible atoms in the form of a symbolic or verbal equation.

How to use it
-------------

ex.

The docstring examples assume that `science` has been imported as `sc`:

    >>> import science as sc

Code for converting a thermometer from Celsius to Kelvin:

    >>> import science as sc
    >>> result = sc.Temperature.Kelvin(13,'c')
    >>> print(result)

For more details, please refer `https://github.com/MASTAR-LAST/Science` and see README.md file.

"""
import numpy
try:
    from .atom import *
    from .thermodynamics import *

except ImportError:
    pass