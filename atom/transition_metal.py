
from __init__ import Atom
from atomic_error import _AtomicError
from sys import *
from types import *
AtomsTransMetal = ["Scandium(Sc)", "Titanium(Ti)", "Vanadium(V)", "Chromium(Cr)", "Manganese(Mn)",
                   "Iron(Fe)", "Cobalt(Co)", "Nickel(Ni)", "Copper(Cu)", "Yttrium(Y)", "Zirconium(Zr)",
                   "Niobium(Nb)", "Molybdenum(Mo)", "Technetium(Tc)", "Ruthenium(Ru)", "Rhodium(Rh)",
                   "Palladium(Pd)", "Silver(Ag)", "Hafnium(Hf)", "Tantalum(Ta)", "Tungsten(W)", "Rhenium(Re)", 
                   "Osmium(Os)", "Iridium(Ir)", "Platinum(Pt)", "Gold(Au)", "Rutherfordium(Rf)", "Dubnium(Db)",
                   "Seaborgium(Sg)", "Bohrium(Bh)", "Hassium(Hs)"]

class TranMetal(Atom):

    """
        TODO: MAKE A DISCREBTION FOR THIS METHOD

    """

    #               Not finish 
    def __init__(self, name, symbol, protons, neutrons, electrons, atomicMass, atomicNumber, group,
     electronConfiguration, electronsPerShell, phaseAtSTP, meltingPoint, boilingPoint, isotopes):

        super().__init__(name, symbol, protons, neutrons, electrons, atomicMass, atomicNumber, group,
     electronConfiguration, electronsPerShell, phaseAtSTP, meltingPoint, boilingPoint, isotopes)

    @classmethod
    def getAtoms(cls):
        """
        THE FUNCTION:

                This function is giving you a describe the atoms contained in this group

        """
        return AtomsTransMetal