try:
    from .storecore import Hydrogen, H, Actinium, Selenium, Se, Sulfur, S, Carbon, C, Chlorine, Cl, Fluorine, F, Bromine, Br, Nitrogen, N, Iodine, I, Oxygen, O, Phosphorus, P
    from .thermodynamics import *

except ImportError:
    from storecore import Hydrogen, H, Actinium, Selenium, Se, Sulfur, S, Carbon, C, Chlorine, Cl, Fluorine, F, Bromine, Br, Nitrogen, N, Iodine, I, Oxygen, O, Phosphorus, P
    from thermodynamics import *
