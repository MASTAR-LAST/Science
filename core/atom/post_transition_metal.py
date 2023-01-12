try:
   from .abc23 import Atom
   from .atomic_error import _AtomicError
   from sys import *
   from types import *
except ImportError:
   from abc23 import Atom
   from atomic_error import _AtomicError
   from sys import *
   from types import *

class PostTransitionMetal(Atom):

     # TODO:     Make Functions&Methods for this class, make sure it has a get atoms method.
     # TODO:     Don't forget to make a list that have all atoms that in this class.  
     def __init__(self, name, symbol, protons, neutrons, electrons, atomicMass, atomicNumber, group,
     electronConfiguration, electronsPerShell, phaseAtSTP, meltingPoint, boilingPoint, isotopes):

        super().__init__(name, symbol, protons, neutrons, electrons, atomicMass, atomicNumber, group,
     electronConfiguration, electronsPerShell, phaseAtSTP, meltingPoint, boilingPoint, isotopes)