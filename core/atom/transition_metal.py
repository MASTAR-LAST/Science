"""
   TODO: Make a docstring
"""
try:
    from .abc23 import Atom
    from .errors.ECUam import _AtomicError
except ImportError:
    from abc23 import Atom
    from errors.ECUam import _AtomicError

AtomsTransMetal: list[str] = ["Scandium(Sc)", "Titanium(Ti)", "Vanadium(V)", "Chromium(Cr)",
      "Manganese(Mn)", "Iron(Fe)", "Cobalt(Co)", "Nickel(Ni)", "Copper(Cu)", "Yttrium(Y)", "Zirconium(Zr)",
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
    def get_atoms(cls):
        """
        THE FUNCTION:

                This function is giving you a describe the atoms contained in this group

        """
        #FIXME: This function must return all the element "NOT PRINT THEM"
        yield AtomsTransMetal[0]
        yield AtomsTransMetal[1]
        yield AtomsTransMetal[2]
        yield AtomsTransMetal[3]
        yield AtomsTransMetal[4]
        yield AtomsTransMetal[5]
        yield AtomsTransMetal[6]
        yield AtomsTransMetal[7]
        yield AtomsTransMetal[8]
        yield AtomsTransMetal[9]
        yield AtomsTransMetal[10]
        yield AtomsTransMetal[11]
        yield AtomsTransMetal[12]
        yield AtomsTransMetal[13]
        yield AtomsTransMetal[14]
        yield AtomsTransMetal[15]
        yield AtomsTransMetal[16]
        yield AtomsTransMetal[17]
        yield AtomsTransMetal[18]
        yield AtomsTransMetal[19]
        yield AtomsTransMetal[20]
        yield AtomsTransMetal[21]
        yield AtomsTransMetal[22]
        yield AtomsTransMetal[23]
        yield AtomsTransMetal[24]
        yield AtomsTransMetal[25]
        yield AtomsTransMetal[26]
        yield AtomsTransMetal[27]
        yield AtomsTransMetal[28]
        yield AtomsTransMetal[29]
        yield AtomsTransMetal[30]

# for i in TranMetal.getAtoms():
#    # print(b for b in TranMetal.getAtoms())
#    print(TranMetal.getAtoms())

# print(next(TranMetal.getAtoms()))
# print(TranMetal.get_atoms.__doc__)
# print(next(TranMetal.getAtoms()))
# for i in TranMetal.getAtoms():

#    print(i)
