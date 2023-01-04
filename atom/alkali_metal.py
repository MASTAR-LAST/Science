from __init__ import Atom
from atomic_error import _AtomicError
from sys import *
from types import *

AtomsAlkaliMetal = ["Hydrogen(H)", "Lithium(Li)", "Sodium(Na)", "Potassium(K)", "Rubidium(Rb)", "Caesium(Cs)", "Francium(Fr)"]

class AlkaliMetal(Atom):

    """
        TODO: MAKE A DISCREBTION FOR THIS METHOD

    """

     # TODO:     Make Functions&Methods for this class, make sure it has a get atoms method.
     # TODO:     Don't forget to make a list that have all atoms that in this class. 
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
        return AtomsAlkaliMetal