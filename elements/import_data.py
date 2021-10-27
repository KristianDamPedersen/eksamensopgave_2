# Importering af biblioteker
from uuid import uuid4 # Helps generate unique ids
# Importing data
nations = open('/Users/kristiandampedersen/Documents/ip_eksamen/eksamensopgave_2/data/nations')


# Defining global variables
team_list = []
round_dict = {
    'round_id': [],
    'round' : [],
    'path' : []
}

match_dict = {
    'match_text': [],
    'match_id':[],
    'round_id':[],
}



# Imports nations to a list
def import_nations():
    """ reads nations.txt line by line and adds it to the team_list lsit """
    Lines = nations.readlines()
    for line in Lines:
        team_list.append(line.strip())


# Constructing a list of rounds and paths
def import_rounds (round, path_str):
    """ This functions add a given round to the round_dict and generates a unique id for it. """
    round_dict['round'].append(round)
    round_dict['path'].append(path_str)
    round_dict['round_id'].append(uuid4())

import_rounds('round1', '/Users/kristiandampedersen/Documents/ip_eksamen/eksamensopgave_2/data/round1')
import_rounds('round2', '/Users/kristiandampedersen/Documents/ip_eksamen/eksamensopgave_2/data/round2')
import_rounds('round3', '/Users/kristiandampedersen/Documents/ip_eksamen/eksamensopgave_2/data/round3')


# Importing the matches
def import_matches():
    """ This function will look at all the files in the round_dict one by one and record the matches. """
    for round in round_dict['path']:
        round_matches = open(round)
        matches = round_matches.readlines()
        for line in matches:
            print(line)
        print(' ')


        

import_matches()
