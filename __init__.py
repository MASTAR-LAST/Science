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

For more details, please refer `<https://github.com/MASTAR-LAST/Science>` and see also `README.md` file.

Atomic Classes
------------

`Atom class:`
                FUNCTIONS:

                    `Available FUNCTIONS`:
                                    `FUNC 1`: "getSymbol" this function's just return a symbol of the element that is in this case is object
                                    `FUNC 2`: "getProtons" this function's just return a symbol of the element that is in this case is object
                                    `FUNC 3`: "getNeutrons" this function's just return a symbol of the element that is in this case is object
                                    `FUNC 4`: "getElectrons" this function's just return a symbol of the element that is in this case is object
                                    `FUNC 5`: "getAtomicMass" this function's just return a symbol of the element that is in this case is object
                                    `FUNC 6`: "getAtomicNumber" this function's just return a symbol of the element that is in this case is object
                                    `FUNC 7`: "getGroup" this function's just return a symbol of the element that is in this case is object
                                    `FUNC 8`: "getElecConfig" this function's just return a symbol of the element that is in this case is object
                                    `FUNC 9`: "getElecPerShell" this function's just return a symbol of the element that is in this case is object
                                    `FUNC 10`: "getPhaseAtSTP" this function's just return a symbol of the element that is in this case is object
                                    `FUNC 11`: "getMeltingPoint" this function's just return a symbol of the element that is in this case is object
                                    `FUNC 12`: "getBoilingPoint" this function's just return a symbol of the element that is in this case is object
                                    `FUNC 13`: "getIsotopes" this function's just return a symbol of the element that is in this case is object
                                    `FUNC 14`: "getFullName" this function's just return a symbol of the element that is in this case is object

                    `Available CASES`:
                                NULL

Thermodynamic Classes
-------------------

`Temperature class:`
                   FUNCTIONS:
                            All functions take two arguments (Temperature, Key)

                        `Available FUNCTIONS`:
                                    `Func 1`:  Kelvin(here but the number of temperature, here but the scale key).
                                    `Func 2`:  Fahrenheit(here but the number of temperature, here but the scale key).
                                    `Func 3`:  Celsius(here but the number of temperature, here but the scale key).

                        `Available CASES`:
                                    `Case 1`:  Use the scale key 'K or k' if the temperature number from Kelvin. 
                                    `Case 2`:  Use the scale key 'F or f' if the temperature number from Fahrenheit.
                                    `Case 3`:  Use the scale key 'C or c' if the temperature number from Celsius.

                    `USES`:
                        If you want to switch between temperature gauges,
                        Use the name of the scale you want to convert to,
                        then put the temperature and the symbol of the scale from which this temperature came.


"""

try:
    from .core import Hydrogen, H, Actinium, Selenium, Se, Sulfur, S, Carbon, C, Chlorine, Cl, Fluorine, F, Bromine, Br, Nitrogen, N, Iodine, I, Oxygen, O, Phosphorus, P, Thorium, Th, Protactinium, Pa, Uranium, U, Neptunium, Np, Plutonium, Pu, Americium, Am, Curium, Cm, Berkelium, Bk, Einsteinium, Es, Fermium, Fm, Mendelevium, Md, Nobelium, Np, Lawrencium, Lr
    from .core import *
    from .version import __version__, __full_version__

except ImportError:
    from core import Hydrogen, H, Actinium, Selenium, Se, Sulfur, S, Carbon, C, Chlorine, Cl, Fluorine, F, Bromine, Br, Nitrogen, N, Iodine, I, Oxygen, O, Phosphorus, P, Thorium, Th, Protactinium, Pa, Uranium, U, Neptunium, Np, Plutonium, Pu, Americium, Am, Curium, Cm, Berkelium, Bk, Einsteinium, Es, Fermium, Fm, Mendelevium, Md, Nobelium, Np, Lawrencium, Lr
    from core import *
    from version import __version__, __full_version__
