import warnings

from Bio.PDB import PDBParser
from Bio.PDB.PDBExceptions import PDBConstructionWarning
from src.PDB_Parser_Encoder.io.parser.parse_pdb import get_contact_info


def parse_and_encode_pdb(pdb_path, angstrom):
    warnings.simplefilter('ignore', PDBConstructionWarning)
    structure = PDBParser().get_structure('X', pdb_path)
    all_contact_infos = []
    for chain in structure[0]:
        for residue in chain:
            hetflag, resseq, icode = residue.get_id()
            if hetflag.strip() == '':
                all_contact_infos.append(get_contact_info(structure, pdb_path, chain.id, angstrom, residue.id[1]))
    return all_contact_infos
