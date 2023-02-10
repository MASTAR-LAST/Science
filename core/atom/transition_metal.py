"""
   TODO: Make a docstring
"""
try:
    from .abc23 import Atom
    from .atomBase.atoms_base import AtomsTransMetal
    from .errors.ECUam import _AtomicError
except ImportError:
    from abc23 import Atom
    from atomBase.atoms_base import AtomsTransMetal
    from errors.ECUam import _AtomicError

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
    def getAtoms(cls) -> list[str]:
        """
        THE FUNCTION:

                This function is giving you a describe the atoms contained in this group

        """
        return AtomsTransMetal
