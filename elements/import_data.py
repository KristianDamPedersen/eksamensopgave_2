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
    'match_text': [], # Can be removed in the final version
    'match_id':[],
    'round_id':[],
    'team1': [],
    'team2': [],
    'points_team_1': [],
    'points_team_2': [],
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
            line_word_list = line.split()
            match_dict['match_text'].append(line_word_list) # Can be removed in final build
            match_dict['match_id'].append(uuid4())
            match_dict['round_id'].append(id[id_nr])
            team1 = line_word_list[0]
            team2 = line_word_list[2]
            team1_points = int(line_word_list[3])
            team2_points = int(line_word_list[5])
            match_dict['team1'].append(team1)
            match_dict['team2'].append(team2)
            match_dict['points_team_1'].append(team1_points)
            match_dict['points_team_2'].append(team2_points)
        # adds empty line
        print(' ')


# Quick render function (for trouble shooting)
def render_matches():
    count = -1
    for i in match_dict:
        count +=1
        first_team = list(match_dict['team1'])
        second_team = list(match_dict['team2'])
        render_first = first_team[count]
        render_second = second_team[count]

        print(
            'This is the match between ' +
            render_first +
            ' and ' +
            render_second
        )


import_matches()
render_matches()
#my_list = [elem[0] for elem in match_dict.values()]
