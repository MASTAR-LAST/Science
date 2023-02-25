"""
        Copyright 2023 Muhammed Alkohawaldeh

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""

#                                                                               Made by TWISTER_FROSTE
#   Date: 24/9/2022
try:
    from .atomBase.atoms_base import AtomBase, Atoms_info
    from .errors.ECUam import _AtomicError, _UndefinedSymbolError
    from typing import Union
except ImportError:
    from atomBase.atoms_base import AtomBase, Atoms_info
    from errors.ECUam import _AtomicError, _UndefinedSymbolError
    from typing import Union
"""
    TODO: Make your own error with 'Exception' like a class 
    go to this link https://www.programiz.com/python-programming/user-defined-exception

"""

#   MAKE MORE VAR TO PASS ALL ATOMS IN IT





########################################################################

########################################################################################################################################

class Atom(AtomBase):
    """
        Atom class
        ==========
                    Available FUNCTIONS:
                    --------------------
                                    `FUNC 1`: `"getSymbol"` this function's just return a symbol of the element that is in this case is object
                                    `FUNC 2`: `"getProtons"` this function's just return a symbol of the element that is in this case is object
                                    `FUNC 3`: `"getNeutrons"` this function's just return a symbol of the element that is in this case is object
                                    `FUNC 4`: `"getElectrons"` this function's just return a symbol of the element that is in this case is object
                                    `FUNC 5`: `"getAtomicMass"` this function's just return a symbol of the element that is in this case is object
                                    `FUNC 6`: `"getAtomicNumber"` this function's just return a symbol of the element that is in this case is object
                                    `FUNC 7`: `"getGroup"` this function's just return a symbol of the element that is in this case is object
                                    `FUNC 8`: `"getElecConfig"` this function's just return a symbol of the element that is in this case is object
                                    `FUNC 9`: `"getElecPerShell"` this function's just return a symbol of the element that is in this case is object
                                    `FUNC 10`: `"getPhaseAtSTP"` this function's just return a symbol of the element that is in this case is object
                                    `FUNC 11`: `"getMeltingPoint"` this function's just return a symbol of the element that is in this case is object
                                    `FUNC 12`: `"getBoilingPoint"` this function's just return a symbol of the element that is in this case is object
                                    `FUNC 13`: `"getIsotopes"` this function's just return a symbol of the element that is in this case is object
                                    `FUNC 14`: `"getFullName"` this function's just return a symbol of the element that is in this case is object

                    Available CASES:
                    ---------------
                                `'NULL'`

        CREATED BY: `Muhammed Alkohawaldeh`
        -----------------------------------
        CLASS VERSION: `0.1.0-Pre-Alpha`
        ----------------------------
    
    """
    
    atomsNumber: int = 0
    
    def __init__(
     self,
     name: Union[str, None],
     symbol: Union[str, None],
     protons: Union[int, None], 
     neutrons: Union[int, None], 
     electrons: Union[int, None], 
     atomicMass: Union[str, None], 
     atomicNumber: Union[int, None], 
     group: Union[str, None],
     electronConfiguration: Union[str, None], 
     electronsPerShell: Union[list, None], 
     phaseAtSTP: Union[str, None], 
     meltingPoint: Union[str, None], 
     boilingPoint: Union[str, None], 
     isotopes: Union[list, None]
     
     ):

        self.__name = name
        self.__group = group
        self.__symbol = symbol
        self.__protons = protons
        self.__neutrons = neutrons 
        self.__electrons = electrons
        self.__atomicMass = atomicMass
        self.__meltingPoint = meltingPoint
        self.__atomicNumber = atomicNumber
        self.__boilingPoint = boilingPoint
        self.__phaseAtSTP = phaseAtSTP
        self.__isotopes = isotopes
        self.__electronsPerShell = electronsPerShell
        self.__electronConfiguration = electronConfiguration
        Atom.atomsNumber += 1


    @classmethod
    def atoms_info(cls, the_atom_name: str) -> Union[str, None]:
        """
            This function is give you a whole info that you want
            about any atom just write the name or write `all_info`
            to get the all info about the all atoms or `symbol`
            to get just the symbol for whole atoms.

        """
        # FIXME: The all_info return none in the end
        # FIXME: The symbol return none in the end
        if the_atom_name == 'all_info':
            for key, value in Atoms_info.items():
                print(key, value)
            
            return ...

        elif the_atom_name == 'symbol':
                temp = 1
                for key in Atoms_info:
                    print(f'Atom_{temp} : {key}')
                    temp += 1            

        elif the_atom_name in Atoms_info:
            return Atoms_info.get(the_atom_name)

        else:
            raise _UndefinedSymbolError(the_atom_name)

    def __str__(self):
        return f' Full Name: {self.__name},\n Symbol: {self.__symbol},\n Protons Number: {self.__protons},\n Neutrons Number: {self.__neutrons},\n Atomic Mass: {self.__atomicMass},\n Group: {self.__group},\n Electron Configuration: {self.__electronConfiguration},\n Electrons Per Shell: {self.__electronsPerShell},\n Phase at STP: {self.__phaseAtSTP},\n Melting Point: {self.__meltingPoint},\n Boiling Point: {self.__boilingPoint},\n Isotopes: {self.__isotopes}'
        
    @property
    def getSymbol(self) -> Union[str, None]:
        return self.__symbol

    @property
    def getProtons(self) -> Union[int, None]:
        return self.__protons

    @property
    def getNeutrons(self) -> Union[int, None]:
        return self.__neutrons

    @property
    def getElectrons(self) -> Union[int, None]:
        return self.__electrons

    @property
    def getAtomicMass(self) -> Union[str, None]:
        return self.__atomicMass

    @property
    def getAtomicNumber(self) -> Union[int, None]:
        return self.__atomicNumber

    @property
    def getGroup(self) -> Union[str, None]:
        return self.__group

    @property
    def getElecConfig(self) -> Union[str, None]:
        return self.__electronConfiguration

    @property
    def getElecPerShell(self) -> Union[list, None]:
        return self.__electronsPerShell

    @property
    def getPhaseAtSTP(self) -> Union[str, None]:
        return self.__phaseAtSTP

    @property
    def getMeltingPoint(self) -> Union[str, None]:
        return self.__meltingPoint

    @property
    def getBoilingPoint(self) -> Union[str, None]:
        return self.__boilingPoint

    @property
    def getIsotopes(self) -> Union[list, None]:
        return self.__isotopes

    @property
    def getFullName(self) -> Union[str, None]:
        return self.__name

    def __add__(self, other):
        
        if self.__electronsPerShell[-1] < 4 and other.__electronsPerShell[-1] < 4:
            return "These two atoms can not being connicting"
        


########################################################################################################################################


# عدد العناصر المعرف داخل المكتبة ككل 
# print(f"The atoms number is {Atom.atomsNumber} out of 118")


########################################################################################################################################