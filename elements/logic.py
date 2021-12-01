""" This document contains the nescessary logic for the scoring system """
class logic:
    points_win = 3
    points_draw = 1
    points_loss = 0

    def identify_winners():
        """ Function that returns the winners of each unique match """
        import pandas as pd
        from numpy import NaN
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

    def team_points(win_points, draw_points, loss_points):
        """ This function calculates the number of points and goals and outputs a dataframe """
        # import the data
        df = logic.identify_winners()

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
        point_dict = {
            'team': unique_names, 
            'no. matches': [],
            'no. wins': [],
            'no. draws': [],
            'no. losses': [],
            'points_wins': [], 
            'points_draws': [], 
            'points_losses': [], 
            'total_scores': []
            }
        
        for i in point_dict['team']:

            ## Retrieving the correct dataframe
            data = df.copy()
            data_t1 = data[data['team1'].isin([i])]
            data_t2 = data[data['team2'].isin([i])]
            data = data_t1.append(data_t2)

            ## Calculate points from wins
            win_df = data[data['winner'] == i]
            point_dict['points_wins'].append(len(win_df)*win_points)

            ## Calculate points from draws
            draw_df = data[data['draw'] == 1]
            point_dict['points_draws'].append(len(draw_df)*draw_points)
            
            ## Calculate points from losses
            loss_df = data[data['loser'] == i]
            point_dict['points_losses'].append(len(loss_df)*loss_points)

            ## Calculate nr. of scores
            scores_t1 = data[data['team1'] == i]
            scores_t1 = scores_t1['points_team_1'].sum()
            scores_t2 = data[data['team2'] == i]
            scores_t2 = scores_t2['points_team_1'].sum()
            scores = scores_t1 + scores_t2
            point_dict['total_scores'].append(scores)

            ## Calculate no. matches
            point_dict['no. matches'].append(len(data))

            ## Calculate no. wins
            point_dict['no. wins'].append(len(win_df))

            ## Calculate no. draws
            point_dict['no. draws'].append(len(draw_df))

            ## Calculate no. losses
            point_dict['no. losses'].append(len(loss_df))

        score_df = pd.DataFrame(point_dict)
        score_df['total_points'] = score_df['points_wins'] + score_df['points_draws'] + score_df['points_losses']
                
        # Return
        return score_df

    def construct_rankings(win_points, draw_points, loss_points, sortby):
        """ This function constructs the dataframe used for rankings with the ability to sort. """
        df = logic.team_points(win_points, draw_points, loss_points)
        df = df[['team', 'no. matches', 'no. wins', 'no. losses', 'no. draws', 'total_points', 'total_scores']]
        if sortby == 'P':
            return df.sort_values(by='total_points', ascending=False)
        elif sortby == 'S':
            return df.sort_values(by=['total_scores', 'total_points'], ascending=False)
        elif sortby == 'A':
            return df.sort_values(by='team')
        else:
            return df
logic.construct_rankings(logic.points_win, logic.points_draw, logic.points_loss, 'A')