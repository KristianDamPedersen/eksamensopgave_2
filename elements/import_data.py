# Importering af biblioteker
from collections import Counter
from uuid import uuid4 # Helps generate unique ids
import sys
sys.path.append(".")
# Importing data
nations = open('/Users/kristiandampedersen/Documents/ip_eksamen/eksamensopgave_2/data/nations')
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

rounds = ['round1', 'round2', 'round3', 'round4', 'round5', 'round6']
paths = ['/Users/kristiandampedersen/Documents/ip_eksamen/eksamensopgave_2/data/round1',
'/Users/kristiandampedersen/Documents/ip_eksamen/eksamensopgave_2/data/round2',
'/Users/kristiandampedersen/Documents/ip_eksamen/eksamensopgave_2/data/round3',
'/Users/kristiandampedersen/Documents/ip_eksamen/eksamensopgave_2/data/round4',
'/Users/kristiandampedersen/Documents/ip_eksamen/eksamensopgave_2/data/round5',
'/Users/kristiandampedersen/Documents/ip_eksamen/eksamensopgave_2/data/round6']
class imports:
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
        nations = open('/Users/kristiandampedersen/Documents/ip_eksamen/eksamensopgave_2/data/nations')
        team_list = []
        Lines = nations.readlines()
        for line in Lines:
            team_list.append(line.strip())
        return team_list


    # Constructing a list of rounds and paths
    def import_rounds (rounds, path_strs):
        """ This functions add a given round to the round_dict and generates a unique id for it. """
        round_dict = {
            'round_id': [],
            'round' : [],
            'path' : []
            }
        count = 0
        for i in rounds:
            round_dict['round'].append(rounds[count])
            round_dict['path'].append(path_strs[count])
            round_dict['round_id'].append(uuid4())
            count += 1
        return round_dict

    
    # Importing the matches
    def import_matches():
        """ This function will look at all the files in the round_dict one by one and record the matches. """
        match_dict = {
            'match_text': [], # Can be removed in the final version
            'match_id':[],
            'round_id':[],
            'team1': [],
            'team2': [],
            'points_team_1': [],
            'points_team_2': [],
        }
        id_nr = -1 # Just acts as a "counter" that lets me know which round_id we've gotten to
        # for each round
        round_dict = imports.import_rounds(rounds, paths)
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
        return match_dict

    # "Quick" render function (for trouble shooting) 
    def render_matches(match_dict):
        count = -1
        list_length = list(match_dict['team1'])
        output = []
        for i in range(len(list_length)):
            count += 1
            first_team = list(match_dict['team1'])
            second_team = list(match_dict['team2'])
            score_team_1 = match_dict['points_team_1']
            score_team_2 = match_dict['points_team_2']
            round_id = list(match_dict['round_id'])
            render_first = first_team[count]
            render_second = second_team[count]
            render_first_score = str(score_team_1[count])
            render_second_score = str(score_team_2[count])
            render_last = str(round_id[count])
            output.append(['Match between ' + render_first +
                ' and ' +
                render_second + 
                ' that ended: ' +
                render_first_score +
                ' - ' +
                render_second_score +
                ' to ' + 
                render_first + 
                ', this belongs to round_id: ' +
                render_last])
        return output
    
    def construct_match_df():
        """ Function that creates a DataFrame containing all the matches """
        import pandas as pd
        rD = imports.import_rounds(rounds, paths)
        mD = imports.import_matches()
        df = pd.DataFrame(mD)
        df = df[['team1', 'team2', 'points_team_2', 'points_team_2', 'match_id', 'round_id']]
        return df
