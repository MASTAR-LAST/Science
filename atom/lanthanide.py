from atom import Atom
from atoms_base import AtomBase
from atomic_error import _AtomicError
from sys import *
from types import *


class Lanthanide(Atom, AtomBase):

     # TODO:     Make Functions&Methods for this class, make sure it has a get atoms method.
     # TODO:     Don't forget to make a list that have all atoms that in this class. 
     def __init__(self, name, symbol, protons, neutrons, electrons, atomicMass, atomicNumber, group,
     electronConfiguration, electronsPerShell, phaseAtSTP, meltingPoint, boilingPoint, isotopes):

        super().__init__(name, symbol, protons, neutrons, electrons, atomicMass, atomicNumber, group,
     electronConfiguration, electronsPerShell, phaseAtSTP, meltingPoint, boilingPoint, isotopes)

fg = Lanthanide(name=None, symbol= None,group= None, atomicMass= None,atomicNumber= None, electronConfiguration=None, electrons=None, electronsPerShell=None, boilingPoint=None, neutrons=None, phaseAtSTP=None, protons=None, meltingPoint=None, isotopes=None)

