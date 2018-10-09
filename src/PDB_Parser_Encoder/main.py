from Bio.PDB import PDBParser
from src.PDB_Parser_Encoder.io.parser.parse_pdb import get_contact_info


def parse_and_encode_pdb(pdb_path, angstrom):
    structure = PDBParser().get_structure('X', pdb_path)
    all_contact_infos = []
    for chain in structure[0]:
        for residue in chain:
            all_contact_infos.append(get_contact_info(structure, pdb_path, chain.id, angstrom, residue.id[1]))
    return all_contact_infos
