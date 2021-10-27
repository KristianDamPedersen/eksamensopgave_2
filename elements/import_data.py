# Importering af biblioteker
# Importering af data
nations = open('/Users/kristiandampedersen/Documents/ip_eksamen/eksamensopgave_2/data/nations')


# Definitioner af globale variable
team_list = []
runder = {
    'round' : 'path',
}



# Importer nationer til en liste.
def import_nations():
    """ Læser nations.txt linje for linje og adder linjen til team_list listen """
    Lines = nations.readlines()
    for line in Lines:
        print('Line: {}'.format(line.strip()))
        team_list.append(line.strip())


# Funktion der konstruerer en liste af runder
def add_round (round, path_str):
    runder['round'].append(round)
    runder['path'].append(path_str)

add_round('runde1', 'sample_path')
print(runder)
