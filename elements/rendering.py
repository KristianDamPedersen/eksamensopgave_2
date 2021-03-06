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
        render.render_switcher(prompt)
    
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
        
        # Guiding the user
        print('Input 0 for main menu, 2 for teams or 3 for matchlog!')
        
        ## Re-resetting styling
        print(Fore.RESET)
        print(Back.RESET)

        ## input
        prompt = input('Please choose an option: ')
        render.render_switcher(prompt)
    

    def render_rankings(points_win, points_draw, points_loss, sortby):
        """ Functions that render the rankings if the user presses 1"""
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
        ## Input printing
        print('Want to sort? write "sort by scores" to sort by "goals" \n or "sort by points" to sort by total points!')
        print('Else input 0 for main menu, 2 for teams or 3 for matchlog!')
        ## Re-resetting styling
        print(Fore.RESET)
        print(Back.RESET)

        ## Input
        prompt = input('Please choose an option: ')
        render.render_switcher(prompt)
        
    

    def render_switcher(prompt):
        """ Small functions that switches between menus"""
        from eksamensopgave_2.app import points_win, points_draw, points_loss, sortby
        if prompt == '0':
            render.render_main(title, subheading, subheading_2, option_header, option_1, option_2, option_3)
        elif prompt == '1':
            render.render_rankings(points_win, points_draw, points_loss, sortby)
        elif prompt == '2':
            print('Not implemented yet')
            prompt = input('Please choose an option: ')
            render.render_switcher(prompt)
        elif prompt == '3':
            render.render_match_log()
        elif prompt == 'sort by scores':
            render.render_rankings(points_win, points_draw, points_loss, 'S')
        elif prompt == 'sort by points':
            render.render_rankings(points_win, points_draw, points_loss, 'P')
        else:
            print('Wrong input!')
            prompt = input('Please choose an option: ')
            render.render_switcher(prompt)




class layout:
    """ Class that controls layout functions """
    def center(text):
        """ Function that centers text """
        spacing = int(width/2-len(text)/2)
        return spacing