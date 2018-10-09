
def write_ddG_trainings_data(angstrom, data):
    with open('data/regression_trainings_data/contact_blomap_' + str(angstrom) + 'A.csv', 'w') as f:
        content = ''
        for element in data:
            for x in element:
                for y in x:
                    content += str(y) + ','
            content = content[:-1]
            content += '\n'
        f.write(content)
