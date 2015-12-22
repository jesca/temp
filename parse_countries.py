import re

with open('a.txt') as f:
    lines = f.read().splitlines()
    output = open('output.txt','w+')
    output.write('{' '\n')

    for line in lines:
        # get parts of strings in quotes
        countryAbbr = re.findall(r'"([^"]*)"', line)[0]
        countryPhoneCode = re.findall(r'\b\d+\b', line)[0]
        output.write(countryAbbr + ': ' + countryPhoneCode + ',' + '\n')

    output.write('}')
    output.close()
    f.close()
