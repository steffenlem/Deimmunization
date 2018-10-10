from src.EvoCS.model.aminoacid_classes import aminoacid_classes_by_number
from src.EvoCS.model.aminoacid_classes import aminoacid_classes_by_code
from src.EvoCS.model.aminoacid_classes import one_letter_encoding_to_number
from src.EvoCS.model.aminoacid_classes import one_letter_encoding_to_letter


def compute_majorities(position_specific_list_of_acids, threshold):
    # Count for every acid at this position
    lower_threshold = len(position_specific_list_of_acids) * threshold
    major_class = ''
    gapcount = 0
    acidcounts = [0 for i in range(20)]
    for acid in position_specific_list_of_acids:
        if acid == '-':
            gapcount += 1
        else:
            acidcounts[one_letter_encoding_to_number[acid]] += 1

    # Check if count of acids exceeds threshold
    for count in acidcounts:
        if count >= lower_threshold:
            major_class = one_letter_encoding_to_letter[acidcounts.index(count)]

    # If no major acid not found yet: Find major acidclass at position
    if major_class == '':
        major_class = find_major_class(acidcounts, lower_threshold)

    # Return major acid/-class if found else '' and gap-percentage at position
    return major_class, gapcount/len(position_specific_list_of_acids)


def find_major_class(acid_counts, lower_threshold):
    # Count for every aminoacidclass at this position
    major_class = ''
    aminoacid_class_counts = [0 for i in range(11)]
    for i in range(len(aminoacid_class_counts)):
        class_string = aminoacid_classes_by_number[i]
        acids_in_class = aminoacid_classes_by_code[class_string]
        for j in range(len(acid_counts)):
            acid = one_letter_encoding_to_letter[j]
            if acid in acids_in_class:
                aminoacid_class_counts[i] += acid_counts[j]

    # Check if count of acids exceeds threshold
    for i in range(len(aminoacid_class_counts)):
        if aminoacid_class_counts[i] >= lower_threshold:
            major_class = aminoacid_classes_by_number[i]
            break

    # Return class if found else ''
    return major_class
