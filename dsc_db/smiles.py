"""
Scripts for resolving chemical SMILES strings for compounds
"""

from pubchempy import get_compounds, Compound
from urllib.error import URLError


def get_smiles_pubchem(name):
    """
    Get the SMILES string for a compound by chemical name through the PubChem API.

    :param name: str containing the compound name
    :return: List of valid SMILES strings.
    """

    smiles = []
    try:
        for compound in get_compounds(name, 'name'):
            print(compound.isomeric_smiles)
            smiles.append(compound.isomeric_smiles)
    except URLError:
        print('Problem accessing API for Pubchem...')
        return []

    return smiles


def add_smiles(pv_records):
    """
    Add SMILES from publishers when possible.
    :param pv_records: List of PhotovoltaicRecord objects, to be enriched with SMILES strings
    :return: pv_records: List of PhotovoltaicRecord objects, after SMILES enrichment
    """

    # Logic for merging:
    # Step 1: Check if abbreviations were used for names
    # Step 2: Check if compounds were used for names
    # Step 3: Use the raw_value
    # Currently we are taking the first returned SMILES string

    for pv_record in pv_records:
        for i, dye in enumerate(pv_record.dye['Dye']):
            # Step 1 - check each abbreviation name in turn
            if 'abbreviations' in dye.keys():
                for abbr_list in dye['abbreviations']:
                    abbr = ' '.join(abbr_list)
                    smiles = get_smiles_pubchem(abbr)
                    if smiles:
                        pv_record.dye['Dye'][i]['smiles'] = {'value': smiles[0], 'context':'abbreviation'}
            # Step 2 - check each compound name in turn
            if 'compound' in dye.keys() and 'smiles' not in dye.keys():
                for name in dye['compound']['names']:
                    smiles = get_smiles_pubchem(name)
                    if smiles:
                        pv_record.dye['Dye'][i]['smiles'] = {'value': smiles[0], 'context':'compound'}
            # Step 3 - try using the raw value
            if 'smiles' not in dye.keys():
                raw_value = dye['raw_value']
                smiles = get_smiles_pubchem(raw_value)
                if smiles:
                    pv_record.dye['Dye'][i]['smiles'] = {'value': smiles[0], 'context': 'raw_value'}

    return pv_records