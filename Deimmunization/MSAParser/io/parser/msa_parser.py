import logging

console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
LOG = logging.getLogger("File parser")
LOG.addHandler(console)
LOG.setLevel(logging.INFO)


def parse_and_setup_info(inputfile, reference_sequence):
    LOG.info("Start Read")
    with open(inputfile) as text:
        msa = []
        for line in text:
            msa.append(line)
    content = remove_non_sequences(msa)
    content = reduce_space(remove_newline(content))

    LOG.info("Start Grouping Content")
    msa_content = []
    for i in content:
        if i.startswith(reference_sequence):
            msa_element = [i]
            msa_content.append(msa_element)
        else:
            msa_element.append(i)
    LOG.info("End Grouping Content")
    LOG.info("End Read")

    return msa_content


def remove_newline(stringlist):
    newlist = []
    for i in range(len(stringlist)):
        if '\n' in stringlist[i] and stringlist[i] != '\n':
            newlist.append(stringlist[i].replace('\n', ''))
    return newlist


def reduce_space(stringlist):
    for i in range(len(stringlist)):
        while '  ' in stringlist[i]:
            stringlist[i] = stringlist[i].replace('  ', ' ')
    return stringlist


def remove_title(stringlist):
    stringlist.remove(stringlist[0])
    return stringlist


def remove_non_sequences(stringlist):
    newstringlist = []
    for i in stringlist:
        if not(':' in i or '.' in i or '*' in i):
            newstringlist.append(i)
    return newstringlist
