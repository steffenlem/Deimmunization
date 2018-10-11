import warnings

from Bio.PDB import PDBParser
from Bio.PDB.PDBExceptions import PDBConstructionWarning
from src.PDB_Parser_Encoder.io.parser.ddG_trainings_dataset_parser import parser_dataset
from src.PDB_Parser_Encoder.io.parser.parse_pdb import get_contact_info
from src.PDB_Parser_Encoder.model.encoding import blopmap_encode_one_letter
from src.PDB_Parser_Encoder.io.writer.ddG_trainings_data_writer import write_ddG_trainings_data


def write_test_data_for_ddg_regression():
    # Ignore ContructionWarnings by PDBParser
    warnings.simplefilter('ignore', PDBConstructionWarning)
    list = parser_dataset()
    # Write a file for each angstrom value marking the residue neighbour threshold
    angstroms = [7]  # 6, 8, 10, 12]
    for a in angstroms:
        test_data = []
        for x in list:
            # Setup PDBParser
            path = 'data/pdb_files/' + x[0] + '.pdb'
            structure = PDBParser().get_structure('X', path)
            # Compute contact information for residue x
            element = get_contact_info(structure, path, x[1], a, int(x[3]))
            element[1].extend(blopmap_encode_one_letter(x[4]))
            element[len(element)-1].append(float(x[7]))
            test_data.append(element)
        # Write file
        write_ddG_trainings_data(a, test_data)
