""" DOCUMENT CONTAINING RENDER UI FUNCTIONS"""
import shutil
# Text variables - main menu
title = 'National Python Football League'
subheading = '( Indledende programmering - Eksamensopgave 2 )'
subheading_2 = 'Coded by: Kristian Dam Pedersen'
option_header = 'Choose your option:'
option_1 = '1) See standings'
option_2 = '2) See teams'
option_3 = '3) See all matches'

# Text variables match log
ml_title = 'All matches:'


# Layout variables
terminal_size = shutil.get_terminal_size()
t_size = str(terminal_size[:3])
t_size_cut = str(t_size[1:3])
width = int(t_size_cut)

class render:
    def render_main(title, subheading, subheading_2, option_header, option_1, option_2, option_3):
        """ Function that renders main menu """
        from colorama import Fore, Back, Style
        import math
        # Reset styles
        print(Back.RESET)
        print(Fore.RESET)
        ### Menu-header
        print(Fore.YELLOW)
        print((layout.center(title)*' ') + title + (layout.center(title)*' '))
        print(Fore.RESET)
        print(layout.center(subheading)*'-' + subheading + layout.center(subheading)*'-')
        print(layout.center(subheading_2)*' ' + '*' + subheading_2 + '*' + layout.center(subheading_2)*' ')
        ### Menu-body
        print(Back.WHITE)
        print(Fore.BLACK)
        print(layout.center(option_header)*' ' + option_header + layout.center(option_header)*' ')
        print(math.floor(width/3)*'- -')
        print(layout.center(option_1)*' ' + option_1 + layout.center(option_1)*' ')
        print(layout.center(option_2)*' ' + option_2 + layout.center(option_2)*' ')
        print(layout.center(option_3)*' ' + option_3 + layout.center(option_3)*' ')
        print(width*' ')
        # Reset styles
        print(Back.RESET)
        print(Fore.RESET)
    
    def render_match_log():
        """ Function that renders stadings if user selects 3. """
        # Importing data for rendering
        import pandas as pd
        from colorama import Fore, Back, Style
        from eksamensopgave_2.elements.import_data import imports as imp
        df = imp.construct_match_df()
        df = df[['team1', 'team2', 'points_team_1', 'points_team_2', 'round_id']]
        df = df.rename(columns={
            'team1': 'Team 1',
            'team2': 'Team 2',
            'points_team_1': 'team 1 points',
            'points_team_2': 'team 2 points',
            'round_id': 'Round'
        })
        ## RESET styling
        print(Fore.RESET)
        print(Back.RESET)

        # actual rendering:
        print(Fore.YELLOW)
        print(layout.center(ml_title)*' ' + ml_title + layout.center(ml_title)*' ')
        print(Fore.RESET)
        print(width*'_')
        
        print(Fore.BLACK)
        print(Back.WHITE)
        for i in range(len(df)):
            print(df.iloc[[i]])
            print(' ')
        
        ## Re-resetting styling
        print(Fore.RESET)
        print(Back.RESET)

    def render_rankings():
                # Importing data for rendering
        import pandas as pd
        from colorama import Fore, Back, Style
        from eksamensopgave_2.elements.logic import logic
        df = logic.team_points()
        df = df[['team1', 'team2', 'points_team_1', 'points_team_2', 'round_id']]
        df = df.rename(columns={
            'team1': 'Team 1',
            'team2': 'Team 2',
            'points_team_1': 'team 1 points',
            'points_team_2': 'team 2 points',
            'round_id': 'Round'
        })
        ## RESET styling
        print(Fore.RESET)
        print(Back.RESET)

        # actual rendering:
        print(Fore.YELLOW)
        print(layout.center(ml_title)*' ' + ml_title + layout.center(ml_title)*' ')
        print(Fore.RESET)
        print(width*'_')
        
        print(Fore.BLACK)
        print(Back.WHITE)
        for i in range(len(df)):
            print(df.iloc[[i]])
            print(' ')
        
        ## Re-resetting styling
        print(Fore.RESET)
        print(Back.RESET)




class layout:
    """ Class that controls layout functions """
    def center(text):
        """ Function that centers text """
        spacing = int(width/2-len(text)/2)
        return spacing