#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8
"""@brief Scientific Constants
@file science_data.py
@package pybooster.science_data
@author Devyn Collier Johnson <DevynCJohnson@Gmail.com>
@copyright LGPLv3
@version 2016.03.25

@section DESCRIPTION
All molar-mass constants are in grams per mole.

@section LICENSE
GNU Lesser General Public License v3
Copyright (c) Devyn Collier Johnson, All rights reserved.

The PyBooster Library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3.0 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library.
"""


__all__ = [
    'ATOM_MOLAR_MASS',
    'MOLECULE_MOLAR_MASS',
    'SMILES',
    'ALPHA_PARTICLE_MASS',
    'ALPHA_PARTICLE_MASS_ENERGY_EQUIVALENT',
    'ALPHA_PARTICLE_MASS_ENERGY_EQUIVALENT_MEV',
    'ALPHA_PARTICLE_MASS_AMU',
    'ALPHA_PARTICLE_MOLAR_MASS',
    'ALPHA_PARTICLE_ELECTRON_MASS_RATIO',
    'ALPHA_PARTICLE_PROTON_MASS_RATIO',
    'ANGSTROM_STAR',
    'ATOMIC_MASS_CONSTANT',
    'ATOMIC_MASS_CONSTANT_ENERGY_EQUIVALENT',
    'ATOMIC_MASS_CONSTANT_ENERGY_EQUIVALENT_MEV',
    'ATOMIC_MASS_UNIT_ELECTRON_VOLT_RELATIONSHIP',
    'ATOMIC_MASS_UNIT_HARTREE_RELATIONSHIP',
    'ATOMIC_MASS_UNIT_HERTZ_RELATIONSHIP',
    'ATOMIC_MASS_UNIT_INVERSE_METER_RELATIONSHIP',
    'ATOMIC_MASS_UNIT_JOULE_RELATIONSHIP',
    'ATOMIC_MASS_UNIT_KELVIN_RELATIONSHIP',
    'ATOMIC_MASS_UNIT_KILOGRAM_RELATIONSHIP',
    'ATOMIC_UNIT_OF_1ST_HYPERPOLARIZABILITY',
    'ATOMIC_UNIT_OF_2ND_HYPERPOLARIZABILITY',
    'ATOMIC_UNIT_OF_ACTION',
    'ATOMIC_UNIT_OF_CHARGE',
    'ATOMIC_UNIT_OF_CHARGE_DENSITY',
    'ATOMIC_UNIT_OF_CURRENT',
    'ATOMIC_UNIT_OF_ELECTRIC_DIPOLE_MOMENT',
    'ATOMIC_UNIT_OF_ELECTRIC_FIELD',
    'ATOMIC_UNIT_OF_ELECTRIC_FIELD_GRADIENT',
    'ATOMIC_UNIT_OF_ELECTRIC_POLARIZABILITY',
    'ATOMIC_UNIT_OF_ELECTRIC_POTENTIAL',
    'ATOMIC_UNIT_OF_ELECTRIC_QUADRUPOLE_MOMENT',
    'ATOMIC_UNIT_OF_ENERGY',
    'ATOMIC_UNIT_OF_FORCE',
    'ATOMIC_UNIT_OF_LENGTH',
    'ATOMIC_UNIT_OF_MAGNETIC_DIPOLE_MOMENT',
    'ATOMIC_UNIT_OF_MAGNETIC_FLUX_DENSITY',
    'ATOMIC_UNIT_OF_MAGNETIZABILITY',
    'ATOMIC_UNIT_OF_MASS',
    'ATOMIC_UNIT_OF_PERMITTIVITY',
    'ATOMIC_UNIT_OF_TIME',
    'ATOMIC_UNIT_OF_VELOCITY',
    'AVOGADRO_CONSTANT',
    'BOHR_MAGNETON',
    'BOHR_MAGNETON_IN_EV',
    'BOHR_MAGNETON_IN_HZ',
    'BOHR_MAGNETON_IN_TESLA',
    'BOHR_MAGNETON_IN_K',
    'BOHR_RADIUS',
    'BOLTZMANN_CONSTANT',
    'BOLTZMANN_CONSTANT_IN_EV',
    'BOLTZMANN_CONSTANT_IN_HZ',
    'BOLTZMANN_CONSTANT_IN_KELVIN',
    'CHARACTERISTIC_IMPEDANCE_OF_VACUUM',
    'CLASSICAL_ELECTRON_RADIUS',
    'COMPTON_WAVELENGTH',
    'COMPTON_WAVELENGTH_OVER_2_PI',
    'CONDUCTANCE_QUANTUM',
    'CONVENTIONAL_VALUE_OF_JOSEPHSON_CONSTANT',
    'CONVENTIONAL_VALUE_OF_VON_KLITZING_CONSTANT',
    'CU_X_UNIT',
    'DEUTERON_G_FACTOR',
    'DEUTERON_MAGNETIC_MOMENT',
    'DEUTERON_MAGNETIC_MOMENT_TO_BOHR_MAGNETON_RATIO',
    'DEUTERON_MAGNETIC_MOMENT_TO_NUCLEAR_MAGNETON_RATIO',
    'DEUTERON_MASS',
    'DEUTERON_MASS_ENERGY_EQUIVALENT',
    'DEUTERON_MASS_ENERGY_EQUIVALENT_IN_MEV',
    'DEUTERON_MASS_IN_U',
    'DEUTERON_MOLAR_MASS',
    'DEUTERON_RMS_CHARGE_RADIUS',
    'DEUTERON_ELECTRON_MAGNETIC_MOMENT_RATIO',
    'DEUTERON_ELECTRON_MASS_RATIO',
    'DEUTERON_NEUTRON_MAGNETIC_MOMENT_RATIO',
    'DEUTERON_PROTON_MAGNETIC_MOMENT_RATIO',
    'DEUTERON_PROTON_MASS_RATIO',
    'ELECTRIC_CONSTANT',
    'ELECTRON_CHARGE_TO_MASS_QUOTIENT',
    'ELECTRON_G_FACTOR',
    'ELECTRON_GYROMAGNETIC_RATIO',
    'ELECTRON_GYROMAGNETIC_RATIO_OVER_2_PI',
    'ELECTRON_MAGNETIC_MOMENT',
    'ELECTRON_MAGNETIC_MOMENT_ANOMALY',
    'ELECTRON_MAGNETIC_MOMENT_TO_BOHR_MAGNETON_RATIO',
    'ELECTRON_MAGNETIC_MOMENT_TO_NUCLEAR_MAGNETON_RATIO',
    'ELECTRON_MASS',
    'ELECTRON_MASS_ENERGY_EQUIVALENT',
    'ELECTRON_MASS_ENERGY_EQUIVALENT_IN_MEV',
    'ELECTRON_MASS_IN_U',
    'ELECTRON_MOLAR_MASS',
    'ELECTRON_TO_ALPHA_PARTICLE_MASS_RATIO',
    'ELECTRON_TO_SHIELDED_HELION_MAGNETIC_MOMENT_RATIO',
    'ELECTRON_TO_SHIELDED_PROTON_MAGNETIC_MOMENT_RATIO',
    'ELECTRON_VOLT',
    'ELECTRON_VOLT_ATOMIC_MASS_UNIT_RELATIONSHIP',
    'ELECTRON_VOLT_HARTREE_RELATIONSHIP',
    'ELECTRON_VOLT_HERTZ_RELATIONSHIP',
    'ELECTRON_VOLT_INVERSE_METER_RELATIONSHIP',
    'ELECTRON_VOLT_JOULE_RELATIONSHIP',
    'ELECTRON_VOLT_KELVIN_RELATIONSHIP',
    'ELECTRON_VOLT_KILOGRAM_RELATIONSHIP',
    'ELECTRON_DEUTERON_MAGNETIC_MOM_RATIO',
    'ELECTRON_DEUTERON_MASS_RATIO',
    'ELECTRON_HELION_MASS_RATIO',
    'ELECTRON_MUON_MAGNETIC_MOMENT_RATIO',
    'ELECTRON_MUON_MASS_RATIO',
    'ELECTRON_NEUTRON_MAGNETIC_MOMENT_RATIO',
]


ATOM_MOLAR_MASS = {  # NOTE: All molar masses are in grams per mole
    r'hydrogen': r'1.008',
    r'helium': r'4.002602',
    r'lithium': r'6.94',
    r'beryllium': r'9.012182',
    r'boron': r'10.81',
    r'carbon': r'12.011',
    r'nitrogen': r'14.007',
    r'oxygen': r'15.999',
    r'fluorine': r'18.9984032',
    r'neon': r'20.1797',
    r'sodium': r'22.98976928',
    r'magnesium': r'24.3050',
    r'aluminium': r'26.9815386',
    r'silicon': r'28.085',
    r'phosphorus': r'30.973762',
    r'sulfur': r'32.06',
    r'chlorine': r'35.45',
    r'argon': r'39.948',
    r'potassium': r'39.0983',
    r'calcium': r'40.078',
    r'scandium': r'44.955912',
    r'titanium': r'47.867',
    r'vanadium': r'50.9415',
    r'chromium': r'51.9961',
    r'manganese': r'54.938045',
    r'iron': r'55.845',
    r'cobalt': r'58.933195',
    r'nickel': r'58.6934',
    r'copper': r'63.546',
    r'zinc': r'65.38',
    r'gallium': r'69.723',
    r'germanium': r'72.63',
    r'arsenic': r'74.92160',
    r'selenium': r'78.96',
    r'bromine': r'79.904',
    r'krypton': r'83.798',
    r'rubidium': r'85.4678',
    r'strontium': r'87.62',
    r'yttrium': r'88.90585',
    r'zirconium': r'91.224',
    r'niobium': r'92.90638',
    r'molybdenum': r'95.96',
    r'technetium': r'98',
    r'ruthenium': r'101.07',
    r'rhodium': r'102.90550',
    r'palladium': r'106.42',
    r'silver': r'107.8682',
    r'cadmium': r'112.411',
    r'indium': r'114.818',
    r'tin': r'118.710',
    r'antimony': r'121.760',
    r'tellurium': r'127.60',
    r'iodine': r'126.90447',
    r'xenon': r'131.293',
    r'caesium': r'132.9054519',
    r'barium': r'137.327',
    r'lanthanum': r'138.90547',
    r'cerium': r'140.116',
    r'praseodymium': r'140.90765',
    r'neodymium': r'144.242',
    r'promethium': r'145',
    r'samarium': r'150.36',
    r'europium': r'151.964',
    r'gadolinium': r'157.25',
    r'terbium': r'158.92535',
    r'dysprosium': r'162.500',
    r'holmium': r'164.93032',
    r'erbium': r'167.259',
    r'thulium': r'168.93421',
    r'ytterbium': r'173.054',
    r'lutetium': r'174.9668',
    r'hafnium': r'178.49',
    r'tantalum': r'180.94788',
    r'tungsten': r'183.84',
    r'rhenium': r'186.207',
    r'osmium': r'190.23',
    r'iridium': r'192.217',
    r'platinum': r'195.084',
    r'gold': r'196.966569',
    r'mercury': r'200.59',
    r'thallium': r'204.38',
    r'lead': r'207.2',
    r'bismuth': r'208.98040',
    r'polonium': r'209',
    r'astatine': r'210',
    r'radon': r'222',
    r'francium': r'223',
    r'radium': r'226',
    r'actinium': r'227',
    r'thorium': r'232.03806',
    r'protactinium': r'231.03588',
    r'uranium': r'238.02891',
    r'neptunium': r'237',
    r'plutonium': r'244',
    r'americium': r'243',
    r'curium': r'247',
    r'berkelium': r'247',
    r'californium': r'251',
    r'einsteinium': r'252',
    r'fermium': r'257',
    r'mendelevium': r'258',
    r'nobelium': r'259',
    r'lawrencium': r'262',
    r'rutherfordium': r'267',
    r'dubnium': r'268',
    r'seaborgium': r'269',
    r'bohrium': r'270',
    r'hassium': r'269',
    r'meitnerium': r'278',
    r'darmstadtium': r'281',
    r'roentgenium': r'281',
    r'copernicium': r'285',
    r'ununtrium': r'286',
    r'flerovium': r'289',
    r'ununpentium': r'288',
    r'livermorium': r'293',
    r'ununseptium': r'294',
    r'ununoctium': r'294',
}


MOLECULE_MOLAR_MASS = {  # NOTE: All molar masses are in grams per mole
    r'meth': r'149.2337',
    r'methamphetamine': r'149.2337',
    r'methylamphetamine': r'149.2337',
    r'water': r'18.01528',
}


SMILES = {
    r'cysteine': r'C(C(C(=O)O)N)S',
    r'dinitrogen': r'N#N',
    r'melatonin': r'CC(=O)NCCC1=CNc2c1cc(OC)cc2',
    r'meth': r'N(C(Cc1ccccc1)C)C',
    r'methionine': r'CSCCC(C(=O)O)N',
    r'methyl_isocyanate': r'CN=C=O',
    r'nicotine': r'CN1CCC[C@H]1c2cccnc2',
    r'selenocysteine': r'O=C(O)[C@@H](N)C[SeH]',
    r'serotonin': r'c1cc2c(cc1O)c(c[nH]2)CCN',
    r'tryptophan': r'c1ccc2c(c1)c(c[nH]2)C[C@@H](C(=O)O)N',
    r'vanillin': r'O=Cc1ccc(O)c(OC)c1',
    r'water': r'O',
}


ALPHA_PARTICLE_MASS = r'6.64465675*10^-27 kg'
ALPHA_PARTICLE_MASS_ENERGY_EQUIVALENT = r'5.97191967*10^-10 J'
ALPHA_PARTICLE_MASS_ENERGY_EQUIVALENT_MEV = r'3727.37924 MeV'
ALPHA_PARTICLE_MASS_AMU = r'4.00150617913 amu'
ALPHA_PARTICLE_MOLAR_MASS = r'0.00400150617912 kg mol^-1'
ALPHA_PARTICLE_ELECTRON_MASS_RATIO = r'7294.2995361'
ALPHA_PARTICLE_PROTON_MASS_RATIO = r'3.97259968933'
ANGSTROM_STAR = r'1.0001495*10^-10 m'
ATOMIC_MASS_CONSTANT = r'1.660538921*10^-27 kg'
ATOMIC_MASS_CONSTANT_ENERGY_EQUIVALENT = r'1.492417954*10^-10 J'
ATOMIC_MASS_CONSTANT_ENERGY_EQUIVALENT_MEV = r'931.494061 MeV'
ATOMIC_MASS_UNIT_ELECTRON_VOLT_RELATIONSHIP = r'931494061.0 eV'
ATOMIC_MASS_UNIT_HARTREE_RELATIONSHIP = r'34231776.845 E_h'
ATOMIC_MASS_UNIT_HERTZ_RELATIONSHIP = r'2.2523427168*10^23 Hz'
ATOMIC_MASS_UNIT_INVERSE_METER_RELATIONSHIP = r'7.5130066042*10^14 m^-1'
ATOMIC_MASS_UNIT_JOULE_RELATIONSHIP = r'1.492417954*10^10 J'
ATOMIC_MASS_UNIT_KELVIN_RELATIONSHIP = r'1.08095408*10^13 K'
ATOMIC_MASS_UNIT_KILOGRAM_RELATIONSHIP = r'1.660538921*10^13 K'
ATOMIC_UNIT_OF_1ST_HYPERPOLARIZABILITY = r'3.206361449*10^53 C^3 m^3 J^-2'
ATOMIC_UNIT_OF_2ND_HYPERPOLARIZABILITY = r'6.23538054e-65 C^4 m^4 J^-3'
ATOMIC_UNIT_OF_ACTION = r'1.054571726e-34 J s'
ATOMIC_UNIT_OF_CHARGE = r'1.602176565e-19 C'
ATOMIC_UNIT_OF_CHARGE_DENSITY = r'1.081202338e+12 C m^-3'
ATOMIC_UNIT_OF_CURRENT = r'0.00662361795 A'
ATOMIC_UNIT_OF_ELECTRIC_DIPOLE_MOMENT = r'8.47835326e-30 C m'
ATOMIC_UNIT_OF_ELECTRIC_FIELD = r'5.14220652e+11 V m^-1'
ATOMIC_UNIT_OF_ELECTRIC_FIELD_GRADIENT = r'9.717362e+21 V m^-2'
ATOMIC_UNIT_OF_ELECTRIC_POLARIZABILITY = r'1.6487772754e-41 C^2 m^2 J^-1'
ATOMIC_UNIT_OF_ELECTRIC_POTENTIAL = r'27.21138505 V'
ATOMIC_UNIT_OF_ELECTRIC_QUADRUPOLE_MOMENT = r'4.486551331e-40 C m^2'
ATOMIC_UNIT_OF_ENERGY = r'4.35974434e-18 J'
ATOMIC_UNIT_OF_FORCE = r'8.23872278e-08 N'
ATOMIC_UNIT_OF_LENGTH = r'5.2917721092e-11 m'
ATOMIC_UNIT_OF_MAGNETIC_DIPOLE_MOMENT = r'1.854801936e-23 J T^-1'
ATOMIC_UNIT_OF_MAGNETIC_FLUX_DENSITY = r'235051.7464 T'
ATOMIC_UNIT_OF_MAGNETIZABILITY = r'7.891036607e-29 J T^-2'
ATOMIC_UNIT_OF_MASS = r'9.10938291e-31 kg'
ATOMIC_UNIT_OF_PERMITTIVITY = r'1.11265005605e-10 F m^-1'
ATOMIC_UNIT_OF_TIME = r'2.4188843265e-17 s'
ATOMIC_UNIT_OF_VELOCITY = r'2187691.26379 m s^-1'
AVOGADRO_CONSTANT = r'6.02214129e+23 mol^-1'
BOHR_MAGNETON = r'9.27400968e-24 J T^-1'
BOHR_MAGNETON_IN_EV = r'5.7883818066e-05 eV T^-1'
BOHR_MAGNETON_IN_HZ = r'13996245550.0 Hz T^-1'
BOHR_MAGNETON_IN_TESLA = r'46.6864498 m^-1 T^-1'
BOHR_MAGNETON_IN_K = r'0.67171388 K T^-1'
BOHR_RADIUS = r'5.2917721092*10^-11 m'
BOLTZMANN_CONSTANT = r'1.3806488e-23 J K^-1'
BOLTZMANN_CONSTANT_IN_EV = r'8.6173324e-05 eV K^-1'
BOLTZMANN_CONSTANT_IN_HZ = r'20836618000.0 Hz K^-1'
BOLTZMANN_CONSTANT_IN_KELVIN = r'69.503476 m^-1 K^-1'
CHARACTERISTIC_IMPEDANCE_OF_VACUUM = r'376.730313462 ohm'
CLASSICAL_ELECTRON_RADIUS = r'2.8179403267e-15 m'
COMPTON_WAVELENGTH = r'2.4263102389e-12 m'
COMPTON_WAVELENGTH_OVER_2_PI = r'3.86159268e-13 m'
CONDUCTANCE_QUANTUM = r'7.7480917346e-05 S'
CONVENTIONAL_VALUE_OF_JOSEPHSON_CONSTANT = r'4.835979e+14 Hz V^-1'
CONVENTIONAL_VALUE_OF_VON_KLITZING_CONSTANT = r'25812.807 ohm'
CU_X_UNIT = r'1.00207697e-13 m'
DEUTERON_G_FACTOR = r'0.8574382308'
DEUTERON_MAGNETIC_MOMENT = r'4.33073489e-27 J T^-1'
DEUTERON_MAGNETIC_MOMENT_TO_BOHR_MAGNETON_RATIO = r'0.0004669754556'
DEUTERON_MAGNETIC_MOMENT_TO_NUCLEAR_MAGNETON_RATIO = r'0.8574382308'
DEUTERON_MASS = r'3.34358348e-27 kg'
DEUTERON_MASS_ENERGY_EQUIVALENT = r'3.00506297e-10 J'
DEUTERON_MASS_ENERGY_EQUIVALENT_IN_MEV = r'1875.612859 MeV'
DEUTERON_MASS_IN_U = r'2.01355321271 u'
DEUTERON_MOLAR_MASS = r'0.00201355321271 kg mol^-1'
DEUTERON_RMS_CHARGE_RADIUS = r'2.1424e-15 m'
DEUTERON_ELECTRON_MAGNETIC_MOMENT_RATIO = r'-0.0004664345537'
DEUTERON_ELECTRON_MASS_RATIO = r'3670.4829652'
DEUTERON_NEUTRON_MAGNETIC_MOMENT_RATIO = r'-0.44820652'
DEUTERON_PROTON_MAGNETIC_MOMENT_RATIO = r'0.307012207'
DEUTERON_PROTON_MASS_RATIO = r'1.99900750097'
ELECTRIC_CONSTANT = r'8.85418781762e-12 F m^-1'
ELECTRON_CHARGE_TO_MASS_QUOTIENT = r'-1.758820088e+11 C kg^-1'
ELECTRON_G_FACTOR = r'-2.00231930436'
ELECTRON_GYROMAGNETIC_RATIO = r'1.760859708e+11 s^-1 T^-1'
ELECTRON_GYROMAGNETIC_RATIO_OVER_2_PI = r'28024.95266 MHz T^-1'
ELECTRON_MAGNETIC_MOMENT = r'-9.2847643e-24 J T^-1'
ELECTRON_MAGNETIC_MOMENT_ANOMALY = r'0.00115965218076'
ELECTRON_MAGNETIC_MOMENT_TO_BOHR_MAGNETON_RATIO = r'-1.00115965218'
ELECTRON_MAGNETIC_MOMENT_TO_NUCLEAR_MAGNETON_RATIO = r'-1838.2819709'
ELECTRON_MASS = r'9.10938291e-31 kg'
ELECTRON_MASS_ENERGY_EQUIVALENT = r'8.18710506e-14 J'
ELECTRON_MASS_ENERGY_EQUIVALENT_IN_MEV = r'0.510998928 MeV'
ELECTRON_MASS_IN_U = r'0.00054857990946 u'
ELECTRON_MOLAR_MASS = r'5.4857990946e-07 kg mol^-1'
ELECTRON_TO_ALPHA_PARTICLE_MASS_RATIO = r'0.000137093355578'
ELECTRON_TO_SHIELDED_HELION_MAGNETIC_MOMENT_RATIO = r'864.058257'
ELECTRON_TO_SHIELDED_PROTON_MAGNETIC_MOMENT_RATIO = r'-658.2275971'
ELECTRON_VOLT = r'1.602176565e-19 J'
ELECTRON_VOLT_ATOMIC_MASS_UNIT_RELATIONSHIP = r'1.07354415e-09 u'
ELECTRON_VOLT_HARTREE_RELATIONSHIP = r'0.03674932379 E_h'
ELECTRON_VOLT_HERTZ_RELATIONSHIP = r'2.417989348e+14 Hz'
ELECTRON_VOLT_INVERSE_METER_RELATIONSHIP = r'806554.429 m^-1'
ELECTRON_VOLT_JOULE_RELATIONSHIP = r'1.602176565e-19 J'
ELECTRON_VOLT_KELVIN_RELATIONSHIP = r'11604.519 K'
ELECTRON_VOLT_KILOGRAM_RELATIONSHIP = r'1.782661845e-36 kg'
ELECTRON_DEUTERON_MAGNETIC_MOM_RATIO = r'-2143.923498'
ELECTRON_DEUTERON_MASS_RATIO = r'0.00027244371095'
ELECTRON_HELION_MASS_RATIO = r'0.00018195430761'
ELECTRON_MUON_MAGNETIC_MOMENT_RATIO = r'206.7669896'
ELECTRON_MUON_MASS_RATIO = r'0.00483633166'
ELECTRON_NEUTRON_MAGNETIC_MOMENT_RATIO = r'960.9205'
