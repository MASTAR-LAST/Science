try:
    from .atom import Actinide
    from .atom import AlkaliMetal
    from .atom import AlkalineEarthMetal
    from .atom import ReactiveNonmetal
    from .atom import TranMetal
    from .atom import UnknownChemicalProperties
    from .atom import NobleGas
    from .atom import Metalloid
    from .atom import PostTransitionMetal
    from .atom import Lanthanide
except ImportError:
    from atom.actinide import Actinide
    from atom.alkali_metal import AlkaliMetal
    from atom.alkaline_earth_metal import AlkalineEarthMetal
    from atom.reactive_nonmetal import ReactiveNonmetal
    from atom.transition_metal import TranMetal
    from atom.unknown_chemical_properties import UnknownChemicalProperties
    from atom.noble_gas import NobleGas
    from atom.metalloid import Metalloid
    from atom.post_transition_metal import PostTransitionMetal
    from atom.lanthanide import Lanthanide

###################################################################################################################################################
#                                                               ReactiveNonmetal Atoms                                                            #
###################################################################################################################################################


Hydrogen: ReactiveNonmetal = ReactiveNonmetal(name = "Hydrogen", 
                            symbol = "H", 
                            protons = 1,
                            neutrons = 0,
                            electrons = 1, 
                            atomicMass ='1.00784 u',
                            atomicNumber = 1, 
                            group = 'Group 1 (alkali metals)', 
                            electronConfiguration = '1S^1',
                            electronsPerShell = [1], 
                            phaseAtSTP = 'Gas', 
                            meltingPoint = '13.99 K (-259.16 °C, -434.49 °F)', 
                            boilingPoint = '20.271 K (-252.879 C, -423.182 F)', 
                            isotopes = ['{1}H', '{2}H', '{3}H'])

Carbon: ReactiveNonmetal = ReactiveNonmetal(name = "Carbon", 
                            symbol = "C", 
                            protons = 6,
                            neutrons = 6,
                            electrons = 6, 
                            atomicMass ='12.0107 u',
                            atomicNumber = 6, 
                            group = 'Group 14 (carbon group)', 
                            electronConfiguration = '2s^2 2p^2',
                            electronsPerShell = [2, 4], 
                            phaseAtSTP = 'Solid', 
                            meltingPoint = '3,823.15 K (3550 °C, 6422 °F)', 
                            boilingPoint = '259.82 K (4,827 C, 8,721 F)', 
                            isotopes = ['{8}C', '{9}C', '{10}C', '{11}C', '{12}C', '{13}C', '{14}C', '{15}C', '{16}C', '{17}C', '{18}C', '{19}C', '{20}C', '{21}C', '{22}C', '{23}C'])

Nitrogen: ReactiveNonmetal = ReactiveNonmetal(name = "Nitrogen", 
                            symbol = "N", 
                            protons = 7,
                            neutrons = 7,
                            electrons = 7, 
                            atomicMass ='14.0067u',
                            atomicNumber = 7, 
                            group = 'Group 15 (pnictogens)', 
                            electronConfiguration = '2s^2 2p^3',
                            electronsPerShell = [2, 5], 
                            phaseAtSTP = 'Gas', 
                            meltingPoint = '(N2) 63.23[2] K (-209.86 °C, -345.75 °F)', 
                            boilingPoint = '(N2) 77.355 K (-195.795 °C, -320.431 °F)', 
                            isotopes = ['{10}N', '{11}N', '{12}N', '{13}N', '{14}N', '{15}N', '{16}N', '{17}N', '{18}N', '{19}N', '{20}N', '{21}N', '{22}N', '{23}N', '{24}N', '{25}N'])

Oxygen: ReactiveNonmetal = ReactiveNonmetal(name = "Oxygen", 
                            symbol = "O", 
                            protons = 8,
                            neutrons = 8,
                            electrons = 8, 
                            atomicMass ='15.999u',
                            atomicNumber = 8, 
                            group = 'Group 16 (chalcogens)', 
                            electronConfiguration = '2s^2 2p^4',
                            electronsPerShell = [2, 6], 
                            phaseAtSTP = 'Gas', 
                            meltingPoint = '(O2) 54.36 K (-218.79 °C, -361.82 °F)', 
                            boilingPoint = '(O2) 90.188 K (-182.962 °C, -297.332 °F)', 
                            isotopes = ['{10}O', '{11}O', '{12}O', '{13}O', '{14}O', '{15}O', '{16}O', '{17}O', '{18}O', '{19}O', '{20}O', '{21}O', '{22}O', '{23}O', '{24}O', '{25}O', '{26}O'])

Fluorine: ReactiveNonmetal = ReactiveNonmetal(name = "Fluorine", 
                            symbol = "F", 
                            protons = 9,
                            neutrons = 9,
                            electrons = 9, 
                            atomicMass ='18.9984032u',
                            atomicNumber = 9, 
                            group = 'Group 17 (halogens)', 
                            electronConfiguration = '2s^2 2p^5',
                            electronsPerShell = [2, 7], 
                            phaseAtSTP = 'Gas', 
                            meltingPoint = '(F2) 53.48 K (-219.67 °C, -363.41 °F)', 
                            boilingPoint = '(F2) 85.03 K (-188.11 °C, -306.60 °F)', 
                            isotopes = ['{13}F', '{14}F', '{15}F', '{16}F', '{17}F', '{18}F', '{19}F', '{20}F', '{21}F', '{22}F', '{23}F', '{24}F', '{25}F', '{26}F', '{27}F', '{28}F', '{29}F', '{30}F', '{31}F'])

Phosphorus: ReactiveNonmetal = ReactiveNonmetal(name = "Phosphorus", 
                            symbol = "P", 
                            protons = 15,
                            neutrons = 15,
                            electrons = 15, 
                            atomicMass ='30.973762u',
                            atomicNumber = 15, 
                            group = 'Group 15 (pnictogens)', 
                            electronConfiguration = '3s^2 3p^3',
                            electronsPerShell = [2, 8, 5], 
                            phaseAtSTP = 'Solid', 
                            meltingPoint = 'white: 317.3 K (44.15 °C, 111.5 °F) red: ~860 K (~590 °C, ~1090 °F)', 
                            boilingPoint = 'white: 553.7 K (280.5 °C, 536.9 °F)', 
                            isotopes = ['{26}P', '{27}P', '{28}P', '{29}P', '{30}P', '{31}P', '{32}P', '{33}P', '{34}P', '{35}P', '{36}P', '{37}P', '{38}P', '{39}P', '{40}P', '{41}P', '{42}P', '{43}P' '{44}P', '{45}P', '{46}P', '{47}P'])

Sulfur: ReactiveNonmetal = ReactiveNonmetal(name = "Sulfur", 
                            symbol = "S", 
                            protons = 16,
                            neutrons = 16,
                            electrons = 16, 
                            atomicMass ='32.065u',
                            atomicNumber = 16, 
                            group = 'Group 16 (chalcogens)', 
                            electronConfiguration = '3s^2 3p^4',
                            electronsPerShell = [2, 8, 6], 
                            phaseAtSTP = 'Solid', 
                            meltingPoint = '388.36 K (115.21 °C, 239.38 °F)', 
                            boilingPoint = '717.8 K (444.6 °C, 832.3 °F)', 
                            isotopes = ['{27}S', '{28}S', '{29}S', '{30}S', '{31}S', '{32}S', '{33}S', '{34}S', '{35}S', '{36}S', '{37}S', '{38}S', '{39}S', '{40}S', '{41}S', '{42}S', '{43}S' '{44}S', '{45}S', '{46}S', '{47}S', '{48}S', '{49}S'])

Chlorine: ReactiveNonmetal = ReactiveNonmetal(name = "Chlorine", 
                            symbol = "Cl", 
                            protons = 17,
                            neutrons = 17,
                            electrons = 17, 
                            atomicMass ='35.453u',
                            atomicNumber = 17, 
                            group = 'Group 17 (halogens)', 
                            electronConfiguration = '3s^2 3p^5',
                            electronsPerShell = [2, 8, 7], 
                            phaseAtSTP = 'Gas', 
                            meltingPoint = '(Cl2) 171.6 K (-101.5 °C, -150.7 °F)', 
                            boilingPoint = '(Cl2) 239.11 K (-34.04 °C, -29.27 °F)', 
                            isotopes = ['{28}Cl', '{29}Cl', '{30}Cl', '{31}Cl', '{32}Cl', '{33}Cl', '{34}Cl', '{35}Cl', '{36}Cl', '{37}Cl', '{38}Cl', '{39}Cl', '{40}Cl', '{41}Cl', '{42}Cl', '{43}Cl' '{44}Cl', '{45}Cl', '{46}Cl', '{47}Cl', '{48}Cl', '{49}Cl', '{50}Cl', '{51}Cl', '{52}Cl'])

Selenium: ReactiveNonmetal = ReactiveNonmetal(name = "Selenium", 
                            symbol = "Se", 
                            protons = 34,
                            neutrons = 34,
                            electrons = 34, 
                            atomicMass ='78.96u',
                            atomicNumber = 34, 
                            group = 'Group 16 (chalcogens)', 
                            electronConfiguration = '3d^10 4s^2 4p^4',
                            electronsPerShell = [2, 8, 18, 6], 
                            phaseAtSTP = 'Solid', 
                            meltingPoint = '494 K (221 °C, 430 °F)', 
                            boilingPoint = '958 K (685 °C, 1265 °F)', 
                            isotopes = ['{65}Se', '{66}Se', '{67}Se', '{68}Se', '{69}Se', '{70}Se', '{71}Se', '{72}Se', '{73}Se', '{74}Se', '{75}Se', '{76}Se', '{77}Se', '{78}Se', '{79}Se', '{80}Se' '{81}Se', '{82}Se', '{83}Se', '{84}Se', '{85}Se', '{86}Se', '{87}Se', '{88}Se', '{89}Se', '{90}Se', '{91}Se', '{92}Se', '{93}Se', '{94}Se'])

Bromine: ReactiveNonmetal = ReactiveNonmetal(name = "Bromine", 
                            symbol = "Br", 
                            protons = 35,
                            neutrons = 35,
                            electrons = 35, 
                            atomicMass ='79.904u',
                            atomicNumber = 35, 
                            group = 'Group 17 (halogens)', 
                            electronConfiguration = '3d^10 4s^2 4p^5',
                            electronsPerShell = [2, 8, 18, 7], 
                            phaseAtSTP = 'Liquid', 
                            meltingPoint = '(Br2) 265.8 K (-7.2 °C, 19 °F)', 
                            boilingPoint = '(Br2) 332.0 K (58.8 °C, 137.8 °F)', 
                            isotopes = ['{68}Br', '{69}Br', '{70}Br', '{71}Br', '{72}Br', '{73}Br', '{74}Br', '{75}Br', '{76}Br', '{77}Br', '{78}Br', '{79}Br', '{80}Br' '{81}Br', '{82}Br', '{83}Br', '{84}Br', '{85}Br', '{86}Br', '{87}Br', '{88}Br', '{89}Br', '{90}Br', '{91}Br', '{92}Br', '{93}Br', '{94}Br', '{95}Br', '{96}Br', '{97}Br', '{98}Br', '{101}Br'])

Iodine: ReactiveNonmetal = ReactiveNonmetal(name = "Iodine", 
                            symbol = "I", 
                            protons = 53,
                            neutrons = 53,
                            electrons = 53, 
                            atomicMass ='126.90447u',
                            atomicNumber = 53, 
                            group = 'Group 17 (halogens)', 
                            electronConfiguration = '4d^10 5s^2 5p^5',
                            electronsPerShell = [2, 8, 18, 18, 7], 
                            phaseAtSTP = 'Solid', 
                            meltingPoint = '(I2) 386.85 K (113.7 °C, 236.66 °F)', 
                            boilingPoint = '(I2) 457.4 K (184.3 °C, 363.7 °F)', 
                            isotopes = ['{108}I', '{109}I', '{110}I', '{111}I', '{112}I', '{113}I', '{114}I', '{115}I', '{116}I', '{117}I', '{118}I', '{119}I', '{120}I' '{121}I', '{122}', '{123}I', '{124}I', '{125}I', '{126}I', '{127}I', '{128}I', '{129}I', '{130}I', '{131}I', '{132}I', '{133}I', '{134}I', '{135}I', '{136}I', '{137}I', '{138}I', '{139}I', '{140}I', '{141}I', '{142}I', '{143}I', '{144}I'])

#           Shurtcuts  :)

H: ReactiveNonmetal = Hydrogen
C: ReactiveNonmetal = Carbon
N: ReactiveNonmetal = Nitrogen
O: ReactiveNonmetal = Oxygen
F: ReactiveNonmetal = Fluorine
P: ReactiveNonmetal = Phosphorus
S: ReactiveNonmetal = Sulfur
Cl: ReactiveNonmetal = Chlorine
Se: ReactiveNonmetal = Selenium
Br: ReactiveNonmetal = Bromine
I: ReactiveNonmetal = Iodine
###################################################################################################################################################
#                                                               Actinide Atoms                                                                    #
###################################################################################################################################################

Actinium: Actinide = Actinide(name = "Actinium", 
                            symbol = "Ac", 
                            protons = 89,
                            neutrons = 89,
                            electrons = 89, 
                            atomicMass ='227u',
                            atomicNumber = 89, 
                            group = 'f-block groups (no number)', 
                            electronConfiguration = '6d^1 7s^2',
                            electronsPerShell = [2, 8, 18, 32, 18, 9, 2], 
                            phaseAtSTP = 'Solid', 
                            meltingPoint = '1500 K (1227 °C, 2240 °F) (estimated)', 
                            boilingPoint = '3500±300 K (3200±300 °C, 5800±500 °F) (extrapolated)', 
                            isotopes = ['{204}Ac', '{205}Ac', '{206}Ac', '{207}Ac', '{208}Ac', '{209}Ac', '{210}Ac', '{211}Ac', '{212}Ac', '{213}Ac', '{214}Ac', '{215}Ac', '{216}Ac', '{217}Ac', '{218}Ac', '{219}Ac', '{220}Ac' '{221}Ac', '{222}Ac', '{223}Ac', '{224}Ac', '{225}Ac', '{226}Ac', '{227}Ac', '{228}Ac', '{229}Ac', '{230}Ac', '{231}Ac', '{232}Ac', '{233}Ac', '{234}Ac', '{235}Ac', '{236}Ac'])

Thorium: Actinide = Actinide(name = "Thorium", 
                            symbol = "Th", 
                            protons = 90,
                            neutrons = 90,
                            electrons = 90, 
                            atomicMass ='232.03806u',
                            atomicNumber = 90, 
                            group = 'f-block groups (no number)', 
                            electronConfiguration = '6d^2 7s^2',
                            electronsPerShell = [2, 8, 18, 32, 18, 10, 2], 
                            phaseAtSTP = 'Solid', 
                            meltingPoint = '2023 K (1750 °C, 3182 °F)', 
                            boilingPoint = '5061 K (4788 °C, 8650 °F)', 
                            isotopes = ['{207}Th', '{208}Th', '{209}Th', '{210}Th', '{211}Th', '{212}Th', '{213}Th', '{214}Th', '{215}Th', '{216}Th', '{217}Th', '{218}Th', '{219}Th', '{220}Th', '{221}Th', '{222}Th', '{223}Th', '{224}Th', '{225}Th', '{226}Th', '{227}Th', '{228}Th', '{229}Th', '{230}Th', '{231}Th', '{232}Th', '{233}Th', '{234}Th', '{235}Th', '{236}Th', '{237}Th', '{238}Th'])

Protactinium: Actinide = Actinide(name = "Protactinium", 
                            symbol = "Pa", 
                            protons = 91,
                            neutrons = 91,
                            electrons = 91, 
                            atomicMass ='231.03588u',
                            atomicNumber = 91, 
                            group = 'f-block groups (no number)', 
                            electronConfiguration = '5f^2 6d^1 7s^2',
                            electronsPerShell = [2, 8, 18, 32, 20, 9, 2], 
                            phaseAtSTP = 'Solid', 
                            meltingPoint = '1841 K (1568 °C, 2854 °F)', 
                            boilingPoint = '4300 K (4027 °C, 7280 °F)', 
                            isotopes = ['{211}Pa', '{212}Pa', '{213}Pa', '{214}Pa', '{215}Pa', '{216}Pa', '{217}Pa', '{218}Pa', '{219}Pa', '{220}Pa', '{221}Pa', '{222}Pa', '{223}Pa', '{224}Pa', '{225}Pa', '{226}Pa', '{227}Pa', '{228}Pa', '{229}Pa', '{230}Pa', '{231}Pa', '{232}Pa', '{233}Pa', '{234}Pa', '{235}Pa', '{236}Pa', '{237}Pa', '{238}Pa', '{239}Pa'])

Uranium: Actinide = Actinide(name = "Uranium", 
                            symbol = "U", 
                            protons = 92,
                            neutrons = 92,
                            electrons = 92, 
                            atomicMass ='238.02891u',
                            atomicNumber = 92, 
                            group = 'f-block groups (no number)', 
                            electronConfiguration = '5f^3 6d^1 7s^2',
                            electronsPerShell = [2, 8, 18, 32, 21, 9, 2], 
                            phaseAtSTP = 'Solid', 
                            meltingPoint = '1405.3 K (1132.2 °C, 2070 °F)', 
                            boilingPoint = '4404 K (4131 °C, 7468 °F)', 
                            isotopes = ['{214}U', '{215}U', '{216}U', '{217}U', '{218}U', '{219}U', '{220}U', '{221}U', '{222}U', '{223}U', '{224}U', '{225}U', '{226}U', '{227}U', '{228}U', '{229}U', '{230}U', '{231}U', '{232}U', '{233}U', '{234}U', '{235}U', '{236}U', '{237}U', '{238}U', '{239}U', '{240}U', '{241}U', '{242}U'])

Neptunium: Actinide = Actinide(name = "Neptunium", 
                            symbol = "Np", 
                            protons = 93,
                            neutrons = 93,
                            electrons = 93, 
                            atomicMass ='237.0482u',
                            atomicNumber = 93, 
                            group = 'f-block groups (no number)', 
                            electronConfiguration = '5f^4 6d^1 7s^2',
                            electronsPerShell = [2, 8, 18, 32, 22, 9, 2], 
                            phaseAtSTP = 'Solid', 
                            meltingPoint = '912±3 K (639±3 °C, 1182±5 °F)', 
                            boilingPoint = '4447 K (4174 °C, 7545 °F) (extrapolated)', 
                            isotopes = ['{219}Np', '{220}Np', '{221}Np', '{222}Np', '{223}Np', '{224}Np', '{225}Np', '{226}Np', '{227}Np', '{228}Np', '{229}Np', '{230}Np', '{231}Np', '{232}Np', '{233}Np', '{234}Np', '{235}Np', '{236}Np', '{237}Np', '{238}Np', '{239}Np', '{240}Np', '{241}Np', '{242}Np', '{243}Np', '{244}Np'])

Plutonium: Actinide = Actinide(name = "Plutonium", 
                            symbol = "Pu", 
                            protons = 94,
                            neutrons = 94,
                            electrons = 94, 
                            atomicMass ='244u',
                            atomicNumber = 94, 
                            group = 'f-block groups (no number)', 
                            electronConfiguration = '5f^6 7s^2',
                            electronsPerShell = [2, 8, 18, 32, 24, 8, 2], 
                            phaseAtSTP = 'Solid', 
                            meltingPoint = '912.5 K (639.4 °C, 1182.9 °F)', 
                            boilingPoint = '3505 K (3228 °C, 5842 °F)', 
                            isotopes = ['{228}Pu', '{229}Pu', '{230}Pu', '{231}Pu', '{232}Pu', '{233}Pu', '{234}Pu', '{235}Pu', '{236}Pu', '{237}Pu', '{238}Pu', '{239}Pu', '{240}Pu', '{241}Pu', '{242}Pu', '{243}Pu', '{244}Pu', '{245}Pu', '{246}Pu', '{247}Pu'])

Americium: Actinide = Actinide(name = "Americium", 
                            symbol = "Am", 
                            protons = 95,
                            neutrons = 95,
                            electrons = 95, 
                            atomicMass ='243u',
                            atomicNumber = 95, 
                            group = 'f-block groups (no number)', 
                            electronConfiguration = '5f^7 7s^2',
                            electronsPerShell = [2, 8, 18, 32, 25, 8, 2],
                            phaseAtSTP = 'Solid', 
                            meltingPoint = '1449 K (1176 °C, 2149 °F)', 
                            boilingPoint = '2880 K (2607 °C, 4725 °F) (calculated)', 
                            isotopes = ['{223}Am', '{224}Am', '{225}Am', '{226}Am', '{227}Am', '{228}Am', '{229}Am', '{230}Am', '{231}Am', '{232}Am', '{233}Am', '{234}Am', '{235}Am', '{236}Am', '{237}Am', '{238}Am', '{239}Am', '{240}Am', '{241}Am', '{242}Am', '{243}Am', '{244}Am', '{245}Am', '{246}Am', '{247}Am'])

Curium: Actinide = Actinide(name = "Curium", 
                            symbol = "Cm", 
                            protons = 96,
                            neutrons = 96,
                            electrons = 96, 
                            atomicMass ='247u',
                            atomicNumber = 96, 
                            group = 'f-block groups (no number)', 
                            electronConfiguration = '5f^7 6d^1 7s^2',
                            electronsPerShell = [2, 8, 18, 32, 25, 9, 2], 
                            phaseAtSTP = 'Solid', 
                            meltingPoint = '1613 K (1340 °C, 2444 °F)', 
                            boilingPoint = '3383 K (3110 °C, 5630 °F)', 
                            isotopes = ['{233}Cm', '{234}Cm', '{235}Cm', '{236}Cm', '{237}Cm', '{238}Cm', '{239}Cm', '{240}Cm', '{241}Cm', '{242}Cm', '{243}Cm', '{244}Cm', '{245}Cm', '{246}Cm', '{247}Cm', '{248}Cm', '{249}Cm', '{250}Cm', '{251}Cm'])

Berkelium: Actinide = Actinide(name = "Berkelium", 
                            symbol = "Bk", 
                            protons = 97,
                            neutrons = 97,
                            electrons = 97, 
                            atomicMass ='247u',
                            atomicNumber = 97, 
                            group = 'f-block groups (no number)', 
                            electronConfiguration = '5f^9 7s^2',
                            electronsPerShell = [2, 8, 18, 32, 27, 8, 2], 
                            phaseAtSTP = 'Solid', 
                            meltingPoint = 'beta: 1259 K (986 °C, 1807 °F)', 
                            boilingPoint = 'beta: 2900 K (2627 °C, 4760 °F)', 
                            isotopes = ['{233}Bk', '{234}Bk', '{235}Bk', '{236}Bk', '{237}Bk', '{238}Bk', '{239}Bk', '{240}Bk', '{241}Bk', '{242}Bk', '{243}Bk', '{244}Bk', '{245}Bk', '{246}Bk', '{247}Bk', '{248}Bk', '{249}Bk', '{250}Bk', '{251}Bk', '{252}Bk', '{253}Bk'])

Californium: Actinide = Actinide(name = "Californium", 
                            symbol = "Cf", 
                            protons = 98,
                            neutrons = 98,
                            electrons = 98, 
                            atomicMass ='251u',
                            atomicNumber = 98, 
                            group = 'f-block groups (no number)', 
                            electronConfiguration = '5f^7 6d^1 7s^2',
                            electronsPerShell = [2, 8, 18, 32, 25, 9, 2], 
                            phaseAtSTP = 'Solid', 
                            meltingPoint = '1613 K (1340 °C, 2444 °F)', 
                            boilingPoint = '3383 K (3110 °C, 5630 °F)', 
                            isotopes = ['{237}Cf', '{238}Cf', '{239}Cf', '{240}Cf', '{241}Cf', '{242}Cf', '{243}Cf', '{244}Cf', '{245}Cf', '{246}Cf', '{247}Cf', '{248}Cf', '{249}Cf', '{250}Cf', '{251}Cf', '{252}Cf', '{253}Cf', '{254}Cf', '{255}Cf', '{256}Cf'])

Einsteinium: Actinide = Actinide(name = "Einsteinium", 
                            symbol = "Es", 
                            protons = 99,
                            neutrons = 99,
                            electrons = 99, 
                            atomicMass ='252u',
                            atomicNumber = 99, 
                            group = 'f-block groups (no number)', 
                            electronConfiguration = '5f^11 7s^2',
                            electronsPerShell = [2, 8, 18, 32, 29, 8, 2], 
                            phaseAtSTP = 'Solid', 
                            meltingPoint = '1133 K (860 °C, 1580 °F)', 
                            boilingPoint = '1269 K (996 °C, 1825 °F) (estimated)', 
                            isotopes = ['{240}Es', '{241}Es', '{242}Es', '{243}Es', '{244}Es', '{245}Es', '{246}Es', '{247}Es', '{248}Es', '{249}Es', '{250}Es', '{251}Es', '{252}Es', '{253}Es', '{254}Es', '{255}Es', '{256}Es', '{257}Es'])

Fermium: Actinide = Actinide(name = "Fermium", 
                            symbol = "Fm", 
                            protons = 100,
                            neutrons = 100,
                            electrons = 100, 
                            atomicMass ='257u',
                            atomicNumber = 100, 
                            group = 'f-block groups (no number)', 
                            electronConfiguration = '5f^12 7s^2',
                            electronsPerShell = [2, 8, 18, 32, 30, 8, 2], 
                            phaseAtSTP = 'Solid (predicted)', 
                            meltingPoint = '1800 K (1527 °C, 2781 °F) (predicted)', 
                            boilingPoint = 'Unknown', 
                            isotopes = ['{241}Fm', '{242}Fm', '{243}Fm', '{244}Fm', '{245}Fm', '{246}Fm', '{247}Fm', '{248}Fm', '{249}Fm', '{250}Fm', '{251}Fm', '{252}Fm', '{253}Fm', '{254}Fm', '{255}Fm', '{256}Fm', '{257}Fm', '{258}Fm', '{259}Fm', '{260}Fm'])

Mendelevium: Actinide = Actinide(name = "Mendelevium", 
                            symbol = "Md", 
                            protons = 101,
                            neutrons = 101,
                            electrons = 101, 
                            atomicMass ='258u',
                            atomicNumber = 101, 
                            group = 'f-block groups (no number)', 
                            electronConfiguration = '5f^13 7s^2',
                            electronsPerShell = [2, 8, 18, 32, 31, 8, 2], 
                            phaseAtSTP = 'Solid (predicted)', 
                            meltingPoint = '1100 K (827 °C, 1521 °F) (predicted)', 
                            boilingPoint = 'Unknown', 
                            isotopes = ['{244}Md', '{245}Md', '{246}Md', '{247}Md', '{248}Md', '{249}Md', '{250}Md', '{251}Md', '{252}Md', '{253}Md', '{254}Md', '{255}Md', '{256}Md', '{257}Md', '{258}Md', '{259}Md', '{260}Md'])

Nobelium: Actinide = Actinide(name = "Nobelium", 
                            symbol = "No", 
                            protons = 102,
                            neutrons = 102,
                            electrons = 102, 
                            atomicMass ='259u',
                            atomicNumber = 102, 
                            group = 'f-block groups (no number)', 
                            electronConfiguration = '5f^14 7s^2',
                            electronsPerShell = [2, 8, 18, 32, 32, 8, 2], 
                            phaseAtSTP = 'Solid (predicted)', 
                            meltingPoint = '1100 K (827 °C, 1521 °F) (predicted)', 
                            boilingPoint = 'Unknown', 
                            isotopes = ['{249}No', '{250}No', '{251}No', '{252}No', '{253}No', '{254}No', '{255}No', '{256}No', '{257}No', '{258}No', '{259}No', '{260}No', '{262}No'])

Lawrencium: Actinide = Actinide(name = "Lawrencium", 
                            symbol = "Lr", 
                            protons = 103,
                            neutrons = 103,
                            electrons = 103, 
                            atomicMass ='262 u',
                            atomicNumber = 103, 
                            group = 'f-block groups (no number)', 
                            electronConfiguration = '5f^14 7s^2 7p^1',
                            electronsPerShell = [2, 8, 18, 32, 32, 8, 3], 
                            phaseAtSTP = 'Solid (predicted)', 
                            meltingPoint = '1900 K (1627 °C, 2961 °F) (predicted)', 
                            boilingPoint = 'Unknown', 
                            isotopes = ['{251}Lr', '{252}Lr', '{253}Lr', '{254}Lr', '{255}Lr', '{256}Lr', '{257}Lr', '{258}Lr', '{259}Lr', '{260}Lr', '{261}Lr', '{262}Lr', '{264}Lr', '{266}Lr'])

Ac:Actinide = Actinium
Th:Actinide = Thorium
Pa:Actinide = Protactinium
U:Actinide = Uranium
Np:Actinide = Neptunium
Pu:Actinide = Plutonium
Am:Actinide = Americium
Cm:Actinide = Curium
Bk:Actinide = Berkelium
Cf:Actinide = Californium
Es:Actinide = Einsteinium
Fm:Actinide = Fermium
Md:Actinide = Mendelevium
No:Actinide = Nobelium
Lr:Actinide = Lawrencium

###################################################################################################################################################
#                                                               AlkaliMetal Atoms                                                                 #
###################################################################################################################################################
