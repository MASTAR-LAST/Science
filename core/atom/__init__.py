"""
        Copyright 2023 Muhammed Alkohawaldeh

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""
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
