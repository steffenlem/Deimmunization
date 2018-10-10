
def write_predicted_blomap_file(predicted_contact_map, output_filepath):
    f = open(output_filepath, 'w+')
    content = predicted_contact_map.to_csv(None, header=False, index=False).split('\n')
    for line in content:
        while ',0.0,' in line:
            line = line.replace(',0.0,', ',0,')
        f.write(line + '\n')
