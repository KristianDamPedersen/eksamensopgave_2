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

# Text variables ranking
r_title = 'Rankings'


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

        # Input
        prompt = input('Please choose an option: ')
        prompt_number = int(prompt)
        
        ## Where do we go from here?
        from eksamensopgave_2.app import points_win, points_draw, points_loss, sortby
        if prompt_number == 1:
            render.render_rankings(points_win, points_draw, points_loss, sortby)
        elif prompt_number == 3:
            render.render_match_log()
        else:
            print('Wrong input!')
    
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

    def render_rankings(points_win, points_draw, points_loss, sortby):
        # Importing data for rendering
        import pandas as pd
        from colorama import Fore, Back, Style
        from eksamensopgave_2.elements.logic import logic
        # Defining data
        df = logic.construct_rankings(points_win, points_draw, points_loss, sortby)
        df = df.rename(columns={
            'team': '___Team___',
            'total_points': 'Total points',
            'total_scores': 'Total goals'
        })
        ## RESET styling
        print(Fore.RESET)
        print(Back.RESET)

        # actual rendering:
        print(Fore.YELLOW)
        print(layout.center(r_title)*' ' + r_title + layout.center(r_title)*' ')
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