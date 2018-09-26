from Deimmunization.MSAParser.model.aminoacid_classes import aminoacid_classes_by_number
from Deimmunization.MSAParser.model.aminoacid_classes import aminoacid_classes_by_code
from Deimmunization.MSAParser.model.aminoacid_classes import one_letter_encoding_to_number
from Deimmunization.MSAParser.model.aminoacid_classes import one_letter_encoding_to_letter


def compute_majorities(position_specific_list_of_acids, threshold):
    lower_threshold = len(position_specific_list_of_acids) * threshold
    major_class = ''
    gapcount = 0
    acidcounts = [0 for i in range(20)]
    for acid in position_specific_list_of_acids:
        if acid == '-':
            gapcount += 1
        else:
            acidcounts[one_letter_encoding_to_number[acid]] += 1
    # print(acidcounts)
    for count in acidcounts:
        if count >= lower_threshold:
            major_class = one_letter_encoding_to_letter[acidcounts.index(count)]
    if major_class == '':
        major_class = find_major_class(acidcounts, lower_threshold)
    return major_class, gapcount/len(position_specific_list_of_acids)


def find_major_class(acid_counts, lower_threshold):
    major_class = ''
    aminoacid_class_counts = [0 for i in range(11)]
    for i in range(len(aminoacid_class_counts)):
        class_string = aminoacid_classes_by_number[i]
        acids_in_class = aminoacid_classes_by_code[class_string]
        for j in range(len(acid_counts)):
            acid = one_letter_encoding_to_letter[j]
            if acid in acids_in_class:
                aminoacid_class_counts[i] += acid_counts[j]
    for i in range(len(aminoacid_class_counts)):
        if aminoacid_class_counts[i] >= lower_threshold:
            major_class = aminoacid_classes_by_number[i]
            break
    return major_class
