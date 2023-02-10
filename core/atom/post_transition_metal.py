try:
   from .abc23 import Atom
   from .atomBase.atoms_base import AtomsPostTransitionMetal
   from .errors.ECUam import _AtomicError
   from sys import *
   from types import *
except ImportError:
   from abc23 import Atom
   from atomBase.atoms_base import AtomsPostTransitionMetal
   from errors.ECUam import _AtomicError
   from sys import *
   from types import *

class PostTransitionMetal(Atom):

     # TODO:     Make Functions&Methods for this class, make sure it has a get atoms method.
     # TODO:     Don't forget to make a list that have all atoms that in this class.  
     def __init__(self, name, symbol, protons, neutrons, electrons, atomicMass, atomicNumber, group,
     electronConfiguration, electronsPerShell, phaseAtSTP, meltingPoint, boilingPoint, isotopes):

        super().__init__(name, symbol, protons, neutrons, electrons, atomicMass, atomicNumber, group,
     electronConfiguration, electronsPerShell, phaseAtSTP, meltingPoint, boilingPoint, isotopes)
        
     @classmethod
     def getAtoms(cls) -> list[str]:
        """
        THE FUNCTION:

                This function is giving you a describe the atoms contained in this group

        """
        return AtomsPostTransitionMetal