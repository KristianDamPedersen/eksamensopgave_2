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
    
    # Appends the winner and losers to the dataframe
    df['winner'] = NaN
    df['loser'] = NaN
    df['draw'] = 0
    count = 0
    for i in range(len(df)):
        df_row = df.iloc[count]
        if df_row['points_team_1'] > df_row['points_team_2']:
            df.loc[df.index[count], 'winner'] = df.loc[df.index[count], 'team1']
            df.loc[df.index[count], 'loser'] = df.loc[df.index[count], 'team2'] 
        elif df_row['points_team_2'] > df_row['points_team_1']:
            df.loc[df.index[count], 'winner'] = df.loc[df.index[count], 'team2']
            df.loc[df.index[count], 'loser'] = df.loc[df.index[count], 'team1']
        else:
            df.loc[df.index[count], 'draw'] = 1
        count += 1

    # Returns the dataframe
    return df

def team_points():
    """ This function calculates the number of points """
    # import the data
    df = identify_winners()

    # Create a list of all unique team names
    t1_names = list(df['team1'].unique())
    t2_names = list(df['team2'].unique())
    team_names = t1_names + t2_names
    unique_names = []
    for i in team_names:
        # check if exists in unique_list or not
        if i not in unique_names:
            unique_names.append(i)
    
    # Create a df containing team names and points from wins
    point_dict = {'team': unique_names, 'points_wins': [], 'points_draws': [], 'points_losses': []}
    
    for i in point_dict['team']:
        ## Retrieving the correct dataframe
        data = df.copy()
        data_t1 = data[data['team1'].isin([i])]
        data_t2 = data[data['team2'].isin([i])]
        data = data_t1.append(data_t2)
        print(data)

        ## Calculate points from wins
        win_df = data[data['winner'] == i]
        print(win_df)
        point_dict['points_wins'].append(len(win_df)*points_win)

        ## Calculate points from draws
        draw_df = data[data['draw'] == 1]
        point_dict['points_draws'].append(len(draw_df)*points_draw)
        
        ## Calculate points from losses
        loss_df = data[data['loser'] == i]
        point_dict['points_losses'].append(len(point_dict)*points_loss)
            
    
    # Create another column containing wins from losses
    # Calculte the total number of points
    # Return
    return point_dict

def team_goals():
    """ This function finds the number of goals for each team. """
    pass

def construct_rankings():
    """ This function constructs the dataframe used for rankings """
    pass

team_points()