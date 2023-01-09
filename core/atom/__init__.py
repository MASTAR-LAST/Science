
if __name__ == "__main__":
    from abc23 import Atom
    from actinide import Actinide
    from alkali_metal import AlkaliMetal
    from alkaline_earth_metal import AlkalineEarthMetal
    from lanthanide import Lanthanide
    from metalloid import Metalloid
    from noble_gas import NobleGas
    from post_transition_metal import PostTransitionMetal
    from reactive_nonmetal import ReactiveNonmetal
    from transition_metal import TranMetal
    from unknown_chemical_properties import UnknownChemicalProperties

else:
    from .abc23 import Atom
    from .actinide import Actinide
    from .alkali_metal import AlkaliMetal
    from .alkaline_earth_metal import AlkalineEarthMetal
    from .lanthanide import Lanthanide
    from .metalloid import Metalloid
    from .noble_gas import NobleGas
    from .post_transition_metal import PostTransitionMetal
    from .reactive_nonmetal import ReactiveNonmetal
    from .transition_metal import TranMetal
    from .unknown_chemical_properties import UnknownChemicalProperties
