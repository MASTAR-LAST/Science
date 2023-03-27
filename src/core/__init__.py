try:
    from .storecore import Hydrogen, H, Actinium, Selenium, Se, Sulfur, S, Carbon, C, Chlorine, Cl, Fluorine, F, Bromine, Br, Nitrogen, N, Iodine, I, Oxygen, O, Phosphorus, P, Thorium, Th, Protactinium, Pa, Uranium, U, Neptunium, Np, Plutonium, Pu, Americium, Am, Curium, Cm, Berkelium, Bk, Einsteinium, Es, Fermium, Fm, Mendelevium, Md, Nobelium, Np, Lawrencium, Lr
    # from .atom import atoms_info
    from .thermodynamics import *

except ImportError:
    from storecore import Hydrogen, H, Actinium, Selenium, Se, Sulfur, S, Carbon, C, Chlorine, Cl, Fluorine, F, Bromine, Br, Nitrogen, N, Iodine, I, Oxygen, O, Phosphorus, P, Thorium, Th, Protactinium, Pa, Uranium, U, Neptunium, Np, Plutonium, Pu, Americium, Am, Curium, Cm, Berkelium, Bk, Einsteinium, Es, Fermium, Fm, Mendelevium, Md, Nobelium, Np, Lawrencium, Lr
    # from atom import atoms_info
    from thermodynamics import *
