""" This document contains the nescessary logic for the scoring system """

from numpy import NaN


points_win = 3
points_draw = 1
points_loss = 0

def identify_winners():
    """ Function that returns the winners of each unique match """
    # Imports the data
    from eksamensopgave_2.elements.import_data import imports as imp
    df = imp.construct_match_df()
    
    # Appends the winner to the dataframe
    df['winner'] = NaN
    count = 0
    for i in range(len(df)):
        df_row = df.iloc[count]
        if df_row['points_team_1'] > df_row['points_team_2']:
            print('team 1 wins!')
        elif df_row['points_team_2'] > df_row['points_team_1']:
            print('team 2 wins!')
        else:
            print('Its a draw!')
        count += 1

    # Appends the loser to the dataframe

    # Returns the dataframe
    #return df
    

identify_winners()