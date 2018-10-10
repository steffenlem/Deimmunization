import csv

# Parse and write content of dataset_S2648_edited_tsv.csv
def parser_dataset():
    f = open('data/dataset_S2648_edited_tsv.csv', 'r')
    reader = csv.reader(f, delimiter=',')
    content = []
    for row in reader:
        content.append(row)
    content.remove(content[0])
    return content
