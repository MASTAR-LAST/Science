"""
Science.constants
=================

This file contains all mathematical and physical constants.

These are some well-known constants
-----------------------------------

"""


from __future__ import annotations

import math as _math
from typing import overload

import numpy as _np
import scipy as sc

__all__ = [
    'yotta', 'zebi', 'zepto', 'zero_Celsius', 'zetta', 'sroot2',
    'sroot3', 'sroot5', 'EULER_MASCHERONI_CONSTANT', 'GOLDEN_RATIO',
    'KRONECKERS_CONSTANT', 'BERNSTEINS_CONSTANT', 'GAUSS_KUZMIN_WIRSING_CONSTANT',
    'HAFNER_SARNAK_MCCURLEY_CONSTANT', 'LANDAUS_CONSTANT', 'OMEGA_CONSTANT',
    'GOLOMB_DICKMAN_CONSTANT', 'CAHENS_CONSTANT', 'TWIN_PRIME_CONSTANT',
    'LAPLACE_LIMIT', 'EMBREE_TREFETHEN_CONSTANT', 'LANDAU_RAMANUJAN_CONSTANT',
    'BRUNS_CONSTANT_FOR_PRIME_QUADRUPLETS', 'CATALANS_CONSTANT', 'LEGENDRES_CONSTANT',
    'VISWANATHS_CONSTANT', 'APÉRYS_CONSTANT', 'CONWAYS_CONSTANT', 'MILLS_CONSTANT',
    'PLASTIC_CONSTANT', 'RAMANUJAN_SOLDNER_CONSTANT', 'BACKHOUSES_CONSTANT',
    'PORTERS_CONSTANT', 'LIEBS_SQUARE_ICE_CONSTANT', 'ERDŐS_BORWEIN_CONSTANT',
    'NIVENS_CONSTANT', 'BRUNS_CONSTANT_FOR_TWIN_PRIMES', 'UNIVERSAL_PARABOLIC_CONSTANT',
    'FEIGENBAUM_CONSTANT', 'SIERPIŃSKIS_CONSTANT', 'KHINCHINS_CONSTANT',
    'FRANSÉN_ROBINSON_CONSTANT', 'LÉVYS_CONSTANT', 'RECIPROCAL_FIBONACCI_CONSTANT',
    'FEIGENBAUM_CONSTANT'
]


pi: float =  3.14159265358979323846264338327950288
e: float = 2.71828182845904523536028747135266249
sroot2: float = 1.41421356237309504880168872420969807
sroot3: float = 1.73205080756887729352744634150587236
sroot5: float = 2.23606797749978969640917366873127623
EULER_MASCHERONI_CONSTANT: float = 0.57721566490153286060651209008240243
GOLDEN_RATIO: float = 1.61803398874989484820458683436563811
#ander development <---ToT--->
# DE_BRUIJN_NEWMAN_CONSTANT = ''
KRONECKERS_CONSTANT: float = 0.26149721284764278375542683860869585
BERNSTEINS_CONSTANT: float = 0.28016949902386913303
GAUSS_KUZMIN_WIRSING_CONSTANT: float = 0.30366300289873265859744812190155623
HAFNER_SARNAK_MCCURLEY_CONSTANT: float = 0.35323637185499598454351655043268201
LANDAUS_CONSTANT: float = 0.5
OMEGA_CONSTANT: float = 0.56714329040978387299996866221035554
GOLOMB_DICKMAN_CONSTANT: float = 0.62432998854355087099293638310083724
CAHENS_CONSTANT: float = 0.6434105462
TWIN_PRIME_CONSTANT: float = 0.66016181584686957392781211001455577
LAPLACE_LIMIT: float = 0.66274341934918158097474209710925290
EMBREE_TREFETHEN_CONSTANT: float = 0.70258
LANDAU_RAMANUJAN_CONSTANT: float = 0.76422365358922066299069873125009232
BRUNS_CONSTANT_FOR_PRIME_QUADRUPLETS: float = 0.87058838
CATALANS_CONSTANT: float = 0.91596559417721901505460351493238411
LEGENDRES_CONSTANT: float = 1
VISWANATHS_CONSTANT: float = 1.13198824
APÉRYS_CONSTANT: float = 1.20205690315959428539973816151144999
CONWAYS_CONSTANT: float = 1.30357726903429639125709911215255189
MILLS_CONSTANT: float = 1.30637788386308069046861449260260571
PLASTIC_CONSTANT: float = 1.32471795724474602596090885447809734
RAMANUJAN_SOLDNER_CONSTANT: float = 1.45136923488338105028396848589202744
BACKHOUSES_CONSTANT: float = 1.45607494858268967139959535111654356
PORTERS_CONSTANT: float = 1.4670780794
LIEBS_SQUARE_ICE_CONSTANT: float = 1.5396007178
ERDŐS_BORWEIN_CONSTANT: float = 1.60669515241529176378330152319092458
NIVENS_CONSTANT: float = 1.70521114010536776428855145343450816
BRUNS_CONSTANT_FOR_TWIN_PRIMES: float = 1.902160583104
UNIVERSAL_PARABOLIC_CONSTANT: float = 2.29558714939263807403429804918949039
FEIGENBAUM_CONSTANT: float = 2.50290787509589282228390287321821578
SIERPIŃSKIS_CONSTANT: float = 2.58498175957925321706589358738317116
KHINCHINS_CONSTANT: float = 2.68545200106530644530971483548179569
FRANSÉN_ROBINSON_CONSTANT: float = 2.80777024202851936522150118655777293
LÉVYS_CONSTANT: float = 3.27582291872181115978768188245384386
RECIPROCAL_FIBONACCI_CONSTANT: float = 3.35988566624317755317201130291892717
FEIGENBAUM_CONSTANT: float = 4.66920160910299067185320382046620161


# mathematical constants
golden = golden_ratio = (1 + _math.sqrt(5)) / 2

# SI prefixes
yotta = 1e24
zetta = 1e21
exa = 1e18
peta = 1e15
tera = 1e12
giga = 1e9
mega = 1e6
kilo = 1e3
hecto = 1e2
deka = 1e1
deci = 1e-1
centi = 1e-2
milli = 1e-3
micro = 1e-6
nano = 1e-9
pico = 1e-12
femto = 1e-15
atto = 1e-18
zepto = 1e-21
yocto = 1e-24

# binary prefixes
kibi = 2**10
mebi = 2**20
gibi = 2**30
tebi = 2**40
pebi = 2**50
exbi = 2**60
zebi = 2**70
yobi = 2**80

# mass in kg
gram = 1e-3
metric_ton = 1e3
grain = 64.79891e-6
lb = pound = 7000 * grain  # avoirdupois
# blob = slinch = pound * g / 0.0254  # lbf*s**2/in (added in 1.0.0)
# slug = blob / 12  # lbf*s**2/foot (added in 1.0.0)
oz = ounce = pound / 16
stone = 14 * pound
long_ton = 2240 * pound
short_ton = 2000 * pound

troy_ounce = 480 * grain  # only for metals / gems
troy_pound = 12 * troy_ounce
carat = 200e-6

# m_e = electron_mass = _cd('electron mass')
# m_p = proton_mass = _cd('proton mass')
# m_n = neutron_mass = _cd('neutron mass')
# m_u = u = atomic_mass = _cd('atomic mass constant')

# angle in rad
degree = pi / 180
arcmin = arcminute = degree / 60
arcsec = arcsecond = arcmin / 60

# time in second
minute = 60.0
hour = 60 * minute
day = 24 * hour
week = 7 * day
year = 365 * day
Julian_year = 365.25 * day

# length in meter
inch = 0.0254
foot = 12 * inch
yard = 3 * foot
mile = 1760 * yard
mil = inch / 1000
pt = point = inch / 72  # typography
survey_foot = 1200.0 / 3937
survey_mile = 5280 * survey_foot
nautical_mile = 1852.0
fermi = 1e-15
angstrom = 1e-10
micron = 1e-6
au = astronomical_unit = 149597870700.0
# light_year = Julian_year * c
parsec = au / arcsec

# pressure in pascal
# atm = atmosphere = _cd('standard atmosphere')
bar = 1e5
# torr = mmHg = atm / 760
# psi = pound * g / (inch * inch)

# area in meter**2
hectare = 1e4
acre = 43560 * foot**2

# volume in meter**3
litre = liter = 1e-3
gallon = gallon_US = 231 * inch**3  # US
# pint = gallon_US / 8
fluid_ounce = fluid_ounce_US = gallon_US / 128
bbl = barrel = 42 * gallon_US  # for oil

gallon_imp = 4.54609e-3  # UK
fluid_ounce_imp = gallon_imp / 160

# speed in meter per second
kmh = 1e3 / hour
mph = mile / hour
mach = speed_of_sound = 340.5  # approx value at 15 degrees in 1 atm. Is this a common value?
knot = nautical_mile / hour

# temperature in kelvin
zero_Celsius = 273.15
degree_Fahrenheit = 1/1.8  # only for differences

# energy in joule
# eV = electron_volt = elementary_charge  # * 1 Volt
calorie = calorie_th = 4.184
calorie_IT = 4.1868
erg = 1e-7
Btu_th = pound * degree_Fahrenheit * calorie_th / gram
Btu = Btu_IT = pound * degree_Fahrenheit * calorie_IT / gram
ton_TNT = 1e9 * calorie_th
# Wh = watt_hour

# power in watt
# hp = horsepower = 550 * foot * pound * g

# force in newton
dyn = dyne = 1e-5
# lbf = pound_force = pound * g