#                                                                        Made by TWISTER_FROSTE (AKA Muhammed alkohawaldeh)
#   Date: 24/9/2022
from abc import ABCMeta, abstractmethod

"""
    TODO: Make your own error with 'Exception' like a class 
    go to this link https://www.programiz.com/python-programming/user-defined-exception

"""

#                   General Atomic lists 
Atoms_info = {"H": ("Hydrogen", "Atomic Number : 1"), "He": ("Helium", "Atomic Number : 2"), "Li": ("Lithium", "Atomic Number : 3"),"Be": ("Beryllium", "Atomic Number : 4"),
        "B": ("Boron", "Atomic Number : 5"),"C": ("Carbon", "Atomic Number : 6"), "N": ("Nitrogen", "Atomic Number : 7"),"O": ("Oxygen", "Atomic Number : 8"),
        "F": ("Fluorine", "Atomic Number : 9"), "Ne": ("Neon", "Atomic Number : 10"), "Na": ("Sodium", "Atomic Number : 11"), "Mg": ("Magnesium", "Atomic Number : 12"),
        "Al": ("Aluminium", "Atomic Number : 13"), "Si": ("Silicon", "Atomic Number : 14"), "P": ("Phosphorus", "Atomic Number : 15"), "S": ("Sulfur", "Atomic Number : 16"),
        "Cl": ("Chlorine", "Atomic Number : 17"), "Ar": ("Argon", "Atomic Number : 18"), "K": ("Potassium", "Atomic Number : 19"), "Ca": ("Calcium", "Atomic Number : 20"),
        "Sc": ("Scandium", "Atomic Number : 21"), "Ti": ("Titanium", "Atomic Number : 22"), "V": ("Vanadium", "Atomic Number : 23"), "Cr": ("Chromium", "Atomic Number : 24"),
        "Mn": ("Manganese", "Atomic Number : 25"), "Fe": ("Iron", "Atomic Number : 26"), "Co": ("Cobalt", "Atomic Number : 27"), "Ni": ("Nickel", "Atomic Number : 28"),
        "Cu": ("Copper", "Atomic Number : 29"), "Zn": ("Zinc", "Atomic Number : 30"), "Ga": ("Gallium", "Atomic Number : 31"), "Ge": ("Germanium", "Atomic Number : 32"),
        "As": ("Arsenic", "Atomic Number : 33"), "Se": ("Selenium", "Atomic Number : 34"), "Br": ("Bromine", "Atomic Number : 35"), "Kr": ("Krypton", "Atomic Number : 36"),
        "Rb": ("Rubidium", "Atomic Number : 37"), "Sr": ("Strontium", "Atomic Number : 38"), "Y": ("Yttrium", "Atomic Number : 39"), "Zr": ("Zirconium", "Atomic Number : 40"),
        "Nb": ("Niobium", "Atomic Number : 41"), "Mo": ("Molybdenum", "Atomic Number : 42"), "Tc": ("Technetium", "Atomic Number : 43"), "Ru": ("Ruthenium", "Atomic Number : 44"),
        "Rh": ("Rhodium", "Atomic Number : 45"), "Pd": ("Palladium", "Atomic Number : 46"), "Ag": ("Silver", "Atomic Number : 47"), "Cd": ("Cadmium", "Atomic Number : 48"),
        "In": ("Indium", "Atomic Number : 49"), "Sn": ("Tin", "Atomic Number : 50"), "Sb": ("Antimony", "Atomic Number : 51"), "Te": ("Tellurium", "Atomic Number : 52"),
        "I": ("Iodine", "Atomic Number : 53"), "Xe": ("Xenon", "Atomic Number : 54"), "Cs": ("Caesium", "Atomic Number : 55"), "Ba": ("Barium", "Atomic Number : 56"),
        "La": ("Lanthanum", "Atomic Number : 57"), "Ce": ("Cerium", "Atomic Number : 58"), "Pr": ("Praseodymium", "Atomic Number : 59"), "Nd": ("Neodymium", "Atomic Number : 60"),
        "Pm": ("Promethium", "Atomic Number : 61"), "Sm": ("Samarium", "Atomic Number : 62"), "Eu": ("Europium", "Atomic Number : 63"), "Gd": ("Gadolinium", "Atomic Number : 64"),
        "Tb": ("Terbium", "Atomic Number : 65"), "Dy": ("Dysprosium", "Atomic Number : 66"), "Ho": ("Holmium", "Atomic Number : 67"), "Er": ("Erbium", "Atomic Number : 68"),
        "Tm": ("Thulium", "Atomic Number : 69"), "Yb": ("Ytterbium", "Atomic Number : 70"), "Lu": ("Lutetium", "Atomic Number : 71"), "Hf": ("Hafnium", "Atomic Number : 72"),
        "Ta": ("Tantalum", "Atomic Number : 73"), "W": ("Tungsten", "Atomic Number : 74"), "Re": ("Rhenium", "Atomic Number : 75"), "Os": ("Osmium", "Atomic Number : 76"),
        "Ir": ("Iridium", "Atomic Number : 77"), "Pt": ("Platinum", "Atomic Number : 78"), "Au": ("Gold", "Atomic Number : 79"), "Hg": ("Mercury", "Atomic Number : 80"),
        "Tl": ("Thallium", "Atomic Number : 81"), "Pb": ("Lead", "Atomic Number : 82"), "Bi": ("Bismuth", "Atomic Number : 83"), "Po": ("Polonium", "Atomic Number : 84"),
        "At": ("Astatine", "Atomic Number : 85"), "Rn": ("Radon", "Atomic Number : 86"), "Fr": ("Francium", "Atomic Number : 87"), "Ra": ("Radium", "Atomic Number : 88"),
        "Ac": ("Actinium", "Atomic Number : 89"), "Th": ("Thorium", "Atomic Number : 90"), "Pa": ("Protactinium", "Atomic Number : 91"), "U": ("Uranium", "Atomic Number : 92"),
        "Np": ("Neptunium", "Atomic Number : 93"), "Pu": ("Plutonium", "Atomic Number : 94"), "Am": ("Americium", "Atomic Number : 95"), "Cm": ("Curium", "Atomic Number : 96"),
        "Bk": ("Berkelium", "Atomic Number : 97"), "Cf": ("Californium", "Atomic Number : 98"), "Es": ("Einsteinium", "Atomic Number : 99"), "Fm": ("Fermium", "Atomic Number : 100"),
        "Md": ("Mendelevium", "Atomic Number : bitcoin101"), "No": ("Nobelium", "Atomic Number : 102"), "Lr": ("Lawrencium", "Atomic Number : 103"), "Rf": ("Rutherfordium", "Atomic Number : 104"),
        "Db": ("Dubnium", "Atomic Number : 105"), "Sg": ("Seaborgium", "Atomic Number : 106"), "Bh": ("Bohrium", "Atomic Number : 107"), "Hs": ("Hassium", "Atomic Number : 108"),
        "Mt": ("Meitnerium", "Atomic Number : 109"), "Ds": ("Darmstadtium", "Atomic Number : 110"), "Rg": ("Roentgenium", "Atomic Number : 111"), "Cn": ("Copernicium", "Atomic Number : 112"),
        "Nh": ("Nihonium", "Atomic Number : 113"), "Fl": ("Flerovium", "Atomic Number : 114"), "Mc": ("Moscovium", "Atomic Number : 115"), "Lv": ("Livermorium", "Atomic Number : 116"),
        "Ts": ("Tennessine", "Atomic Number : 117"), "Og": ("Oganesson", "Atomic Number : 118")}

Atomic_Number: dict[str, int] = {"H": 1, "He": 2, "Li": 3, "Be": 4, "B": 5, "C": 6, "N": 7, "O": 8, "F": 9, "Ne": 10,
        "Na": 11, "Mg": 12, "Al": 13, "Si": 14, "P": 15, "S": 16, "Cl": 17, "Ar": 18, "K": 19, "Ca": 20,"Sc": 21, "Ti": 22,
        "V": 23, "Cr": 24, "Mn": 25, "Fe": 26, "Co": 27, "Ni": 28, "Cu": 29, "Zn": 30, "Ga": 31, "Ge": 32, "As": 33, "Se": 34,
        "Br": 35, "Kr": 36, "Rb": 37, "Sr": 38,"Y": 39, "Zr": 40, "Nb": 41, "Mo": 42, "Tc": 43, "Ru": 44, "Rh": 45, "Pd": 46,
        "Ag": 47,"Cd": 48, "In": 49, "Sn": 50, "Sb": 51, "Te": 52, "I": 53, "Xe": 54, "Cs": 55, "Ba": 56, "La": 57, "Ce": 58,
        "Pr": 59,"Nd": 60, "Pm": 61, "Sm": 62, "Eu": 63, "Gd": 64, "Tb": 65, "Dy": 66, "Ho": 67, "Er": 68, "Tm": 69, "Yb": 70,
        "Lu": 71, "Hf": 72, "Ta": 73, "W": 74, "Re": 75, "Os": 76,"Ir": 77, "Pt": 78, "Au": 79, "Hg": 80, "Tl": 81, "Pb": 82,
        "Bi": 83, "Po": 84, "At": 85, "Rn": 86, "Fr": 87, "Ra": 88, "Ac": 89, "Th": 90, "Pa": 91, "U": 92, "Np": 93, "Pu": 94,
        "Am": 95, "Cm": 96, "Bk": 97, "Cf": 98, "Es": 99, "Fm": 100, "Md": 101, "No": 102, "Lr": 103, "Rf": 104, "Db": 105,
        "Sg": 106, "Bh": 107, "Hs": 108, "Mt": 109, "Ds": 110, "Rg": 111, "Cn": 112, "Nh": 113, "Fl": 114, "Mc": 115, "Lv": 116,
        "Ts": 117, "Og": 118}

#                   Groups for the Periodic Table

AtomsTransMetal: list[str] = ["Scandium(Sc)", "Titanium(Ti)", "Vanadium(V)", "Chromium(Cr)", "Manganese(Mn)",
                   "Iron(Fe)", "Cobalt(Co)", "Nickel(Ni)", "Copper(Cu)", "Yttrium(Y)", "Zirconium(Zr)",
                   "Niobium(Nb)", "Molybdenum(Mo)", "Technetium(Tc)", "Ruthenium(Ru)", "Rhodium(Rh)",
                   "Palladium(Pd)", "Silver(Ag)", "Hafnium(Hf)", "Tantalum(Ta)", "Tungsten(W)", "Rhenium(Re)", 
                   "Osmium(Os)", "Iridium(Ir)", "Platinum(Pt)", "Gold(Au)", "Rutherfordium(Rf)", "Dubnium(Db)",
                   "Seaborgium(Sg)", "Bohrium(Bh)", "Hassium(Hs)"]

AtomsAlkaliMetal: list[str] = ["Hydrogen(H)", "Lithium(Li)", "Sodium(Na)", "Potassium(K)", "Rubidium(Rb)", "Caesium(Cs)", "Francium(Fr)"]

AtomsAlkalineEarthMetal: list[str] = ['Beryllium(Be)', 'Magnesium(Mg)', 'Calcium(Ca)', 'Strontium(Sr)', 'Barium(Ba)', 'Radium(Ra)']

AtomsActinide: list[str] = ['Actinium(Ac)', 'Thorium(Th)', 'Protactinium(Pa)', 'Uranium(U)', 'Neptunium(Np)', 'Plutonium(Pu)',
                             'Americium(Am)', 'Curium(Cm)', 'Berkelium(Bk)', 'Californium(Cf)', 'Einsteinium(Es)', 'Fermium(Fm)',
                               'Mendelevium(Md)', 'Nobelium(No)', 'Lawrencium(Lr)']

AtomsPostTransitionMetal: list[str] = ['Aluminium(Al)', 'Gallium(Ga)', 'Zinc(Zn)', 'Cadmium(Cd)', 'Indium(In)', 'Tin(Sn)',
                                        'Mercury(Hg)', 'Thallium(Tl)', 'Lead(Pb)', 'Bismuth(Bi)', 'Polonium(Po)', 'Astatine(At)']

AtomsMetalloid: list[str] = ['Boron(B)', 'Silicon(Si)', 'Germanium(Ge)', 'Arsenic(As)', 'Antimony(Sb)', 'Tellurium(Te)']

AtomsReactiveNonmetal: list[str] = ['Carbon(C)', 'Nitrogen(N)', 'Oxygen(O)', 'Fluorine(F)', 'Phosphorus(P)',
                                     'Sulfur(S)', 'Chlorine(Cl)', 'Selenium(Se)', 'Bromine(Br)', 'Iodine(I)']

AtomsNobleGas: list[str] = ['Helium(He)', 'Neon(Ne)', 'Argon(Ar)', 'Krypton(Kr)', 'Xenon(Xe)', 'Radon(Rn)']

AtomsLanthanide: list[str] = ['Lanthanum(La)', 'Cerium(Ce)', 'Praseodymium(Pr)', 'Neodymium(Nd)', 'Promethium(Pm)',
                            'Samarium(Sm)', 'Europium(Eu)', 'Gadolinium(Gd)', 'Terbium(Tb)', 'Dysprosium(Dy)', 'Holmium(Ho)',
                            'Erbium(Er)', 'Thulium(Tm)', 'Ytterbium(Yb)', 'Lutetium(Lu)']

AtomsUnknownChemProp: list[str] = ['Meitnerium(Mt)', 'Darmstadtium(Ds)', 'Roentgenium(Rg)', 'Copernicium(Cn)', 'Nihonium(Nh)',
                                    'Flerovium(Fl)', 'Moscovium(Mc)', 'Livermorium(Lv)', 'Tennessine(Ts)', 'Oganesson(Og)']

########################################################################


class AtomBase(metaclass=ABCMeta):

#     @abstractmethod
#     def atoms_info() -> None: ...
    @property
    @abstractmethod
    def symbol() -> None: ...
    @property
    @abstractmethod
    def protons() -> None: ... 
    @property
    @abstractmethod
    def neutrons() -> None:...
    @property
    @abstractmethod
    def electrons() -> None:...
    @property
    @abstractmethod
    def atomic_mass() -> None:...
    @property
    @abstractmethod
    def atomic_number() -> None:...
    @property
    @abstractmethod
    def group() -> None:...
    @property
    @abstractmethod
    def electron_configuration() -> None:...
    @property
    @abstractmethod
    def electrons_per_shell() -> None:...
    @property
    @abstractmethod
    def phase_at_STP() -> None:...
    @property
    @abstractmethod
    def melting_point() -> None:...
    @property
    @abstractmethod
    def boiling_point() -> None:...
    @property
    @abstractmethod
    def isotopes() -> None:...
    @property
    @abstractmethod
    def full_name()-> None:...
