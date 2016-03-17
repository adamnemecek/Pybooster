#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8
"""
Created by Devyn Collier Johnson
<DevynCJohnson@Gmail.com>
LGPLv3 License
-- --
PyBooster - Various Extras for Python3
pybooster.science_data
-- --
Scientific Data
-- --
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
-- --
All molar masses are in grams per mole
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

__author__ = 'Devyn Collier Johnson'
__copyright__ = 'LGPLv3'
__version__ = '2016.03.09'


ATOM_MOLAR_MASS = {  # NOTE: All molar masses are in grams per mole
    'hydrogen': '1.008',
    'helium': '4.002602',
    'lithium': '6.94',
    'beryllium': '9.012182',
    'boron': '10.81',
    'carbon': '12.011',
    'nitrogen': '14.007',
    'oxygen': '15.999',
    'fluorine': '18.9984032',
    'neon': '20.1797',
    'sodium': '22.98976928',
    'magnesium': '24.3050',
    'aluminium': '26.9815386',
    'silicon': '28.085',
    'phosphorus': '30.973762',
    'sulfur': '32.06',
    'chlorine': '35.45',
    'argon': '39.948',
    'potassium': '39.0983',
    'calcium': '40.078',
    'scandium': '44.955912',
    'titanium': '47.867',
    'vanadium': '50.9415',
    'chromium': '51.9961',
    'manganese': '54.938045',
    'iron': '55.845',
    'cobalt': '58.933195',
    'nickel': '58.6934',
    'copper': '63.546',
    'zinc': '65.38',
    'gallium': '69.723',
    'germanium': '72.63',
    'arsenic': '74.92160',
    'selenium': '78.96',
    'bromine': '79.904',
    'krypton': '83.798',
    'rubidium': '85.4678',
    'strontium': '87.62',
    'yttrium': '88.90585',
    'zirconium': '91.224',
    'niobium': '92.90638',
    'molybdenum': '95.96',
    'technetium': '98',
    'ruthenium': '101.07',
    'rhodium': '102.90550',
    'palladium': '106.42',
    'silver': '107.8682',
    'cadmium': '112.411',
    'indium': '114.818',
    'tin': '118.710',
    'antimony': '121.760',
    'tellurium': '127.60',
    'iodine': '126.90447',
    'xenon': '131.293',
    'caesium': '132.9054519',
    'barium': '137.327',
    'lanthanum': '138.90547',
    'cerium': '140.116',
    'praseodymium': '140.90765',
    'neodymium': '144.242',
    'promethium': '145',
    'samarium': '150.36',
    'europium': '151.964',
    'gadolinium': '157.25',
    'terbium': '158.92535',
    'dysprosium': '162.500',
    'holmium': '164.93032',
    'erbium': '167.259',
    'thulium': '168.93421',
    'ytterbium': '173.054',
    'lutetium': '174.9668',
    'hafnium': '178.49',
    'tantalum': '180.94788',
    'tungsten': '183.84',
    'rhenium': '186.207',
    'osmium': '190.23',
    'iridium': '192.217',
    'platinum': '195.084',
    'gold': '196.966569',
    'mercury': '200.59',
    'thallium': '204.38',
    'lead': '207.2',
    'bismuth': '208.98040',
    'polonium': '209',
    'astatine': '210',
    'radon': '222',
    'francium': '223',
    'radium': '226',
    'actinium': '227',
    'thorium': '232.03806',
    'protactinium': '231.03588',
    'uranium': '238.02891',
    'neptunium': '237',
    'plutonium': '244',
    'americium': '243',
    'curium': '247',
    'berkelium': '247',
    'californium': '251',
    'einsteinium': '252',
    'fermium': '257',
    'mendelevium': '258',
    'nobelium': '259',
    'lawrencium': '262',
    'rutherfordium': '267',
    'dubnium': '268',
    'seaborgium': '269',
    'bohrium': '270',
    'hassium': '269',
    'meitnerium': '278',
    'darmstadtium': '281',
    'roentgenium': '281',
    'copernicium': '285',
    'ununtrium': '286',
    'flerovium': '289',
    'ununpentium': '288',
    'livermorium': '293',
    'ununseptium': '294',
    'ununoctium': '294',
}


MOLECULE_MOLAR_MASS = {  # NOTE: All molar masses are in grams per mole
    'meth': '149.2337',
    'methamphetamine': '149.2337',
    'methylamphetamine': '149.2337',
    'water': '18.01528',
}


SMILES = {
    'cysteine': 'C(C(C(=O)O)N)S',
    'dinitrogen': 'N#N',
    'melatonin': 'CC(=O)NCCC1=CNc2c1cc(OC)cc2',
    'meth': 'N(C(Cc1ccccc1)C)C',
    'methionine': 'CSCCC(C(=O)O)N',
    'methyl_isocyanate': 'CN=C=O',
    'nicotine': 'CN1CCC[C@H]1c2cccnc2',
    'selenocysteine': 'O=C(O)[C@@H](N)C[SeH]',
    'serotonin': 'c1cc2c(cc1O)c(c[nH]2)CCN',
    'tryptophan': 'c1ccc2c(c1)c(c[nH]2)C[C@@H](C(=O)O)N',
    'vanillin': 'O=Cc1ccc(O)c(OC)c1',
    'water': 'O',
}


ALPHA_PARTICLE_MASS = '6.64465675*10^-27 kg'
ALPHA_PARTICLE_MASS_ENERGY_EQUIVALENT = '5.97191967*10^-10 J'
ALPHA_PARTICLE_MASS_ENERGY_EQUIVALENT_MEV = '3727.37924 MeV'
ALPHA_PARTICLE_MASS_AMU = '4.00150617913 amu'
ALPHA_PARTICLE_MOLAR_MASS = '0.00400150617912 kg mol^-1'
ALPHA_PARTICLE_ELECTRON_MASS_RATIO = '7294.2995361'
ALPHA_PARTICLE_PROTON_MASS_RATIO = '3.97259968933'
ANGSTROM_STAR = '1.0001495*10^-10 m'
ATOMIC_MASS_CONSTANT = '1.660538921*10^-27 kg'
ATOMIC_MASS_CONSTANT_ENERGY_EQUIVALENT = '1.492417954*10^-10 J'
ATOMIC_MASS_CONSTANT_ENERGY_EQUIVALENT_MEV = '931.494061 MeV'
ATOMIC_MASS_UNIT_ELECTRON_VOLT_RELATIONSHIP = '931494061.0 eV'
ATOMIC_MASS_UNIT_HARTREE_RELATIONSHIP = '34231776.845 E_h'
ATOMIC_MASS_UNIT_HERTZ_RELATIONSHIP = '2.2523427168*10^23 Hz'
ATOMIC_MASS_UNIT_INVERSE_METER_RELATIONSHIP = '7.5130066042*10^14 m^-1'
ATOMIC_MASS_UNIT_JOULE_RELATIONSHIP = '1.492417954*10^10 J'
ATOMIC_MASS_UNIT_KELVIN_RELATIONSHIP = '1.08095408*10^13 K'
ATOMIC_MASS_UNIT_KILOGRAM_RELATIONSHIP = '1.660538921*10^13 K'
ATOMIC_UNIT_OF_1ST_HYPERPOLARIZABILITY = '3.206361449*10^53 C^3 m^3 J^-2'
ATOMIC_UNIT_OF_2ND_HYPERPOLARIZABILITY = '6.23538054e-65 C^4 m^4 J^-3'
ATOMIC_UNIT_OF_ACTION = '1.054571726e-34 J s'
ATOMIC_UNIT_OF_CHARGE = '1.602176565e-19 C'
ATOMIC_UNIT_OF_CHARGE_DENSITY = '1.081202338e+12 C m^-3'
ATOMIC_UNIT_OF_CURRENT = '0.00662361795 A'
ATOMIC_UNIT_OF_ELECTRIC_DIPOLE_MOMENT = '8.47835326e-30 C m'
ATOMIC_UNIT_OF_ELECTRIC_FIELD = '5.14220652e+11 V m^-1'
ATOMIC_UNIT_OF_ELECTRIC_FIELD_GRADIENT = '9.717362e+21 V m^-2'
ATOMIC_UNIT_OF_ELECTRIC_POLARIZABILITY = '1.6487772754e-41 C^2 m^2 J^-1'
ATOMIC_UNIT_OF_ELECTRIC_POTENTIAL = '27.21138505 V'
ATOMIC_UNIT_OF_ELECTRIC_QUADRUPOLE_MOMENT = '4.486551331e-40 C m^2'
ATOMIC_UNIT_OF_ENERGY = '4.35974434e-18 J'
ATOMIC_UNIT_OF_FORCE = '8.23872278e-08 N'
ATOMIC_UNIT_OF_LENGTH = '5.2917721092e-11 m'
ATOMIC_UNIT_OF_MAGNETIC_DIPOLE_MOMENT = '1.854801936e-23 J T^-1'
ATOMIC_UNIT_OF_MAGNETIC_FLUX_DENSITY = '235051.7464 T'
ATOMIC_UNIT_OF_MAGNETIZABILITY = '7.891036607e-29 J T^-2'
ATOMIC_UNIT_OF_MASS = '9.10938291e-31 kg'
ATOMIC_UNIT_OF_PERMITTIVITY = '1.11265005605e-10 F m^-1'
ATOMIC_UNIT_OF_TIME = '2.4188843265e-17 s'
ATOMIC_UNIT_OF_VELOCITY = '2187691.26379 m s^-1'
AVOGADRO_CONSTANT = '6.02214129e+23 mol^-1'
BOHR_MAGNETON = '9.27400968e-24 J T^-1'
BOHR_MAGNETON_IN_EV = '5.7883818066e-05 eV T^-1'
BOHR_MAGNETON_IN_HZ = '13996245550.0 Hz T^-1'
BOHR_MAGNETON_IN_TESLA = '46.6864498 m^-1 T^-1'
BOHR_MAGNETON_IN_K = '0.67171388 K T^-1'
BOHR_RADIUS = '5.2917721092*10^-11 m'
BOLTZMANN_CONSTANT = '1.3806488e-23 J K^-1'
BOLTZMANN_CONSTANT_IN_EV = '8.6173324e-05 eV K^-1'
BOLTZMANN_CONSTANT_IN_HZ = '20836618000.0 Hz K^-1'
BOLTZMANN_CONSTANT_IN_KELVIN = '69.503476 m^-1 K^-1'
CHARACTERISTIC_IMPEDANCE_OF_VACUUM = '376.730313462 ohm'
CLASSICAL_ELECTRON_RADIUS = '2.8179403267e-15 m'
COMPTON_WAVELENGTH = '2.4263102389e-12 m'
COMPTON_WAVELENGTH_OVER_2_PI = '3.86159268e-13 m'
CONDUCTANCE_QUANTUM = '7.7480917346e-05 S'
CONVENTIONAL_VALUE_OF_JOSEPHSON_CONSTANT = '4.835979e+14 Hz V^-1'
CONVENTIONAL_VALUE_OF_VON_KLITZING_CONSTANT = '25812.807 ohm'
CU_X_UNIT = '1.00207697e-13 m'
DEUTERON_G_FACTOR = '0.8574382308'
DEUTERON_MAGNETIC_MOMENT = '4.33073489e-27 J T^-1'
DEUTERON_MAGNETIC_MOMENT_TO_BOHR_MAGNETON_RATIO = '0.0004669754556'
DEUTERON_MAGNETIC_MOMENT_TO_NUCLEAR_MAGNETON_RATIO = '0.8574382308'
DEUTERON_MASS = '3.34358348e-27 kg'
DEUTERON_MASS_ENERGY_EQUIVALENT = '3.00506297e-10 J'
DEUTERON_MASS_ENERGY_EQUIVALENT_IN_MEV = '1875.612859 MeV'
DEUTERON_MASS_IN_U = '2.01355321271 u'
DEUTERON_MOLAR_MASS = '0.00201355321271 kg mol^-1'
DEUTERON_RMS_CHARGE_RADIUS = '2.1424e-15 m'
DEUTERON_ELECTRON_MAGNETIC_MOMENT_RATIO = '-0.0004664345537'
DEUTERON_ELECTRON_MASS_RATIO = '3670.4829652'
DEUTERON_NEUTRON_MAGNETIC_MOMENT_RATIO = '-0.44820652'
DEUTERON_PROTON_MAGNETIC_MOMENT_RATIO = '0.307012207'
DEUTERON_PROTON_MASS_RATIO = '1.99900750097'
ELECTRIC_CONSTANT = '8.85418781762e-12 F m^-1'
ELECTRON_CHARGE_TO_MASS_QUOTIENT = '-1.758820088e+11 C kg^-1'
ELECTRON_G_FACTOR = '-2.00231930436'
ELECTRON_GYROMAGNETIC_RATIO = '1.760859708e+11 s^-1 T^-1'
ELECTRON_GYROMAGNETIC_RATIO_OVER_2_PI = '28024.95266 MHz T^-1'
ELECTRON_MAGNETIC_MOMENT = '-9.2847643e-24 J T^-1'
ELECTRON_MAGNETIC_MOMENT_ANOMALY = '0.00115965218076'
ELECTRON_MAGNETIC_MOMENT_TO_BOHR_MAGNETON_RATIO = '-1.00115965218'
ELECTRON_MAGNETIC_MOMENT_TO_NUCLEAR_MAGNETON_RATIO = '-1838.2819709'
ELECTRON_MASS = '9.10938291e-31 kg'
ELECTRON_MASS_ENERGY_EQUIVALENT = '8.18710506e-14 J'
ELECTRON_MASS_ENERGY_EQUIVALENT_IN_MEV = '0.510998928 MeV'
ELECTRON_MASS_IN_U = '0.00054857990946 u'
ELECTRON_MOLAR_MASS = '5.4857990946e-07 kg mol^-1'
ELECTRON_TO_ALPHA_PARTICLE_MASS_RATIO = '0.000137093355578'
ELECTRON_TO_SHIELDED_HELION_MAGNETIC_MOMENT_RATIO = '864.058257'
ELECTRON_TO_SHIELDED_PROTON_MAGNETIC_MOMENT_RATIO = '-658.2275971'
ELECTRON_VOLT = '1.602176565e-19 J'
ELECTRON_VOLT_ATOMIC_MASS_UNIT_RELATIONSHIP = '1.07354415e-09 u'
ELECTRON_VOLT_HARTREE_RELATIONSHIP = '0.03674932379 E_h'
ELECTRON_VOLT_HERTZ_RELATIONSHIP = '2.417989348e+14 Hz'
ELECTRON_VOLT_INVERSE_METER_RELATIONSHIP = '806554.429 m^-1'
ELECTRON_VOLT_JOULE_RELATIONSHIP = '1.602176565e-19 J'
ELECTRON_VOLT_KELVIN_RELATIONSHIP = '11604.519 K'
ELECTRON_VOLT_KILOGRAM_RELATIONSHIP = '1.782661845e-36 kg'
ELECTRON_DEUTERON_MAGNETIC_MOM_RATIO = '-2143.923498'
ELECTRON_DEUTERON_MASS_RATIO = '0.00027244371095'
ELECTRON_HELION_MASS_RATIO = '0.00018195430761'
ELECTRON_MUON_MAGNETIC_MOMENT_RATIO = '206.7669896'
ELECTRON_MUON_MASS_RATIO = '0.00483633166'
ELECTRON_NEUTRON_MAGNETIC_MOMENT_RATIO = '960.9205'