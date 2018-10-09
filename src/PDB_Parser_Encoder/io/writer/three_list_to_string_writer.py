
def three_list_to_string(three_list):
    content = ''
    for element in three_list:
        for x in element:
            for y in x:
                content += str(y) + ','
        content = content[:-1]
        content += '\n'
    return content
