# Importering af biblioteker
from collections import Counter
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
    id_nr = -1 # Just acts as a "counter" that lets me know which round_id we've gotten to
    # for each round
    for round in round_dict['path']:
        id_nr += 1 # Increases the round_id
        id = list(round_dict['round_id']) # Creates a list of the ids in the round_dict
        round_matches = open(round)
        matches = round_matches.readlines()
        # for each line in the round file
        for line in matches:
            print(id[id_nr]) # Prints the id corresponding to the round_id at the id_nr index.
            print(line) # Just prints the match at that point
            line_word_list = line.split()
            print(line_word_list) # Prints the words but in a list
            match_dict['match_text'].append(line_word_list)
            match_dict['match_id'].append(uuid4())
            match_dict['round_id'].append(id[id_nr])
        # adds empty line
        print(' ')


print(round_dict)

import_matches()

my_list = [elem[0] for elem in match_dict.values()]
print(my_list[0])
