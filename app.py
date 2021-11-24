# Kør dette program for at køre appen.
# importing libraries 
import sys
sys.path.append(".")
import pandas as pd
from uuid import uuid4 # Helps generate unique ids
from eksamensopgave_2.elements.import_data import imports as imp
from eksamensopgave_2.elements.import_data import rounds, paths
rounds = rounds.copy()
paths = paths.copy()

match_dict = {
    'match_text': [], # Can be removed in the final version
    'match_id':[],
    'round_id':[],
    'team1': [],
    'team2': [],
    'points_team_1': [],
    'points_team_2': [],
}
# Importing data
print(rounds)
print(paths)


rd = imp.import_rounds(rounds, paths)
md = imp.import_matches()
print(md)
imp.render_matches(md)