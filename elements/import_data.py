# Importering af biblioteker
# Importering af data
nations = open('/Users/kristiandampedersen/Documents/ip_eksamen/eksamensopgave_2/data/nations')


# Definitioner af globale variable
team_list = []


# Importer nationer til en liste.
def import_nations():
    """ Læser nations.txt linje for linje og adder linjen til team_list listen """
    Lines = nations.readlines()
    for line in Lines:
        print('Line: {}'.format(line.strip()))
        team_list.append(line.strip())
