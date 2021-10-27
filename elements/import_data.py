# Importering af biblioteker
from uuid import uuid4 # Helps generate unique ids
# Importering af data
nations = open('/Users/kristiandampedersen/Documents/ip_eksamen/eksamensopgave_2/data/nations')


# Definitioner af globale variable
team_list = []
round_dict = {
    'round_id': [],
    'round' : [],
    'path' : []
}



# Imports nations to a list
def import_nations():
    """ reads nations.txt line by line and adds it to the team_list lsit """
    Lines = nations.readlines()
    for line in Lines:
        team_list.append(line.strip())


# Constructing a list of rounds and paths
def add_round (round, path_str):
    """ This functions add a given round to the round_dict and generates a unique id for it. """
    round_dict['round'].append(round)
    round_dict['path'].append(path_str)
    round_dict['round_id'].append(uuid4())


        
