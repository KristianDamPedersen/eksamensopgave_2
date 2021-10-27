# Importering af biblioteker
# Importering af data
nations = open('/Users/kristiandampedersen/Documents/ip_eksamen/eksamensopgave_2/data/nations')

def import_nations():
    Lines = nations.readlines()
    for line in Lines:
        print('Line: {}'.format(line.strip()))

import_nations()

