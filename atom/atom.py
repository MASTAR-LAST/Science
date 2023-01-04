#                                                                               Made by TWISTER_FROSTE
#   Date: 24/9/2022
from abc import ABCMeta, abstractmethod
# from lanthanide import Lanthanide
# from alkaliMetal import AlkaliMetal
# from metalloid import Metalloid
# from nobleGas import NobleGas
# from alkalineEarthMetal import AlkalineEarthMetal
# from actinide import Actinide
# from reactiveNonmetal import ReactiveNonmetal
# from transitionMetal import TranMetal
# from unknownChemicalProperties import UnknownChemicalProperties
# from postTransitionMetal import PostTransitionMetal
from atoms_base import AtomBase, Atoms_info
from atomic_error import _AtomicError, _UndefinedSymbolError
import time
import sys

"""
    TODO: Make your own error with 'Exception' like a class 
    go to this link https://www.programiz.com/python-programming/user-defined-exception

"""

#   MAKE MORE VAR TO PASS ALL ATOMS IN IT





########################################################################

########################################################################################################################################

class Atom(AtomBase):
    """
        FUNCTIONS:
                All functions in this class just need to call and don't take any argument

                    Available FUNCTIONS:
                                    FUNC 1: "getSymbol" this function's just return a symbol of the element that is in this case is object
                                    FUNC 2: "getProtons" this function's just return a symbol of the element that is in this case is object
                                    FUNC 3: "getNeutrons" this function's just return a symbol of the element that is in this case is object
                                    FUNC 4: "getElectrons" this function's just return a symbol of the element that is in this case is object
                                    FUNC 5: "getAtomicMass" this function's just return a symbol of the element that is in this case is object
                                    FUNC 6: "getAtomicNumber" this function's just return a symbol of the element that is in this case is object
                                    FUNC 7: "getGroup" this function's just return a symbol of the element that is in this case is object
                                    FUNC 8: "getElecConfig" this function's just return a symbol of the element that is in this case is object
                                    FUNC 9: "getElecPerShell" this function's just return a symbol of the element that is in this case is object
                                    FUNC 10: "getPhaseAtSTP" this function's just return a symbol of the element that is in this case is object
                                    FUNC 11: "getMeltingPoint" this function's just return a symbol of the element that is in this case is object                                    FUNC 1: "getSymbol" this function's just return a symbol of the element that is in this case is object
                                    FUNC 12: "getBoilingPoint" this function's just return a symbol of the element that is in this case is object
                                    FUNC 13: "getIsotopes" this function's just return a symbol of the element that is in this case is object
                                    FUNC 14: "getFullName" this function's just return a symbol of the element that is in this case is object

                    Available CASES:
                                NULL

        CREATED BY: TWISTER_FROSTE
        VERSION: 0.1.1(beta)
    
    """
    
    atomsNumber = 0
    
    def __init__(self, name: str | None, symbol: str | None, protons: int | None, neutrons: int | None, electrons: int | None, atomicMass: str | None, atomicNumber: int | None, group: str | None,
     electronConfiguration: str | None, electronsPerShell: list | None, phaseAtSTP: str | None, meltingPoint: str | None, boilingPoint: str | None, isotopes: list | None):

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
    def atoms_info(cls, the_atom_name: str) -> str:
        """
            This function is give you a whole info that you want
            about any atom just write the name or write all_info
            to get the all info about the all atoms.

        """
        # FIXME: The all_info return none in the end
        # FIXME: The symbol return none in the end
        if the_atom_name == 'all_info':
            for key, value in Atoms_info.items():
                print(key, value)
            
            return 

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
        
    # #       DO NOT F**KING FORGET TO DEBUGGING THIS F**KING FUNCTION
    # @classmethod 
    # def e_orbit(cls, element):
    #     cls.element = element

    #     e_dist = []
    #     Atomic_number_tmp = Atomic_Number[element]
    #     while Atomic_number_tmp != 0:

    #         if Atomic_number_tmp == 1:
    #             e_dist.append(1)
    #             break

    #         else:
    #             e_dist.append(2)
    #             Atomic_number_tmp -= 2

    #             if Atomic_number_tmp <= 0:
    #                 break

    #             else:
    #                 if (Atomic_number_tmp - 8) == 0:
    #                      e_dist.append(8)
    #                      break

    #                 elif (Atomic_number_tmp - 8) > 0:
    #                     e_dist.append(8)
    #                     Atomic_number_tmp -= 8

    #                     if Atomic_number_tmp <= 0:
    #                         break

    #                     elif Atomic_number_tmp > 0 and Atomic_number_tmp <= 8:
    #                         e_dist.append(Atomic_number_tmp)

    #                 elif (Atomic_number_tmp - 8) < 0:
    #                     break
    #         break
    #     print(e_dist)

# TEST FUNCTION
# Atoms.e_orbit("H")
    @property
    def getSymbol(self) -> str | None:
        return self.__symbol

    @property
    def getProtons(self) -> int | None:
        return self.__protons

    @property
    def getNeutrons(self) -> int | None:
        return self.__neutrons

    @property
    def getElectrons(self) -> int | None:
        return self.__electrons

    @property
    def getAtomicMass(self) -> str | None:
        return self.__atomicMass

    @property
    def getAtomicNumber(self) -> int | None:
        return self.__atomicNumber

    @property
    def getGroup(self) -> str | None:
        return self.__group

    @property
    def getElecConfig(self) -> str | None:
        return self.__electronConfiguration

    @property
    def getElecPerShell(self) -> list | None:
        return self.__electronsPerShell

    @property
    def getPhaseAtSTP(self) -> str | None:
        return self.__phaseAtSTP

    @property
    def getMeltingPoint(self) -> str | None:
        return self.__meltingPoint

    @property
    def getBoilingPoint(self) -> str | None:
        return self.__boilingPoint

    @property
    def getIsotopes(self) -> list | None:
        return self.__isotopes

    @property
    def getFullName(self) -> str | None:
        return self.__name

########################################################################################################################################


# عدد العناصر المعرف داخل المكتبة ككل 
# print(f"The atoms number is {Atom.atomsNumber} out of 118")
# #FIXME:     The result of this command is None Becuz there is something in the run.py file in the system.   
# print(TranMetal.getAtoms())


###################################################################################################################################################

Hydrogen = Atom("Hydrogen", "H", 1, 0, 1, '1.00784u', 1, 'Group 1 (alkali metals)', '1S^1', [1], 'Gas', '13.99 K (-259.16 C, -434.49 F)', '(H2) 20.271 K (-252.879 C, -423.182 F)', ['1H', '2H', '3H'])
Helium = Atom("Helium", "He", 2, 2, 2, "4.002602 u", 2, 'Group 18 (noble gases)', "1s^2", [2], 'Gas', "0.95 K (-272.20 °C, -457.96 °F) (at 2.5 MPa)", '	4.222 K (-268.928 °C, -452.070 °F)', ['2He', '3He', '4He'])
# Lithium = Atom()
# Beryllium = Atom()
# Boron = Atom()
# Carbon = Atom()
# Nitrogen = Atom()
# Oxygen = Atom()
# Fluorine = Atom()
# Neon = Atom()
# Sodium = Atom()
# Magnesium = Atom()
# Aluminium = Atom()
# Silicon = Atom()
# Phosphorus = Atom()
# Sulfur = Atom()
# Chlorine = Atom()
# Argon = Atom()
           #                                   أجعل لكل نوع من العناصل فئة خاصة مثلاً فئة الغازات النبيلة
# print(Hydrogen.getMeltingPoint())


#TranMetale = Transition Metal

# print(Temperature.Celsius(3,'r'))


# print(Temperature.Fahrenheit(23,'k'))
# print(Temperature.Kelvin(0,'F'))

# print(Atom.atoms_info('all_info'))
# print(Atom.atoms_info(56))
# print(Atom.atoms_info('symbol'))

# print(Atom.atoms_info("all_info"))