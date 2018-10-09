from src.PDB_Parser_Encoder.model.encoding import blopmap_encode_one_letter
from src.PDB_Parser_Encoder.model.encoding import blopmap_encode_three_letter
from src.PDB_Parser_Encoder.io.writer.three_list_to_string_writer import three_list_to_string


def do_and_return_pointmutation(encoded_pdb_informations, residue_id, new_residue):
    for residue_info in encoded_pdb_informations:
        if residue_info[1] == [residue_id]:
            if len(new_residue) == 1:
                residue_info[1] = blopmap_encode_one_letter(new_residue)
            elif len(new_residue) == 3:
                residue_info[1] = blopmap_encode_three_letter(new_residue)
            return residue_info
    raise ValueError('The given residue id does not exist in this pdb-file!')


def write_three_list_as_string(mutations):
    return three_list_to_string(mutations)
