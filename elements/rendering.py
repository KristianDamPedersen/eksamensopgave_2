""" DOCUMENT CONTAINING RENDER UI FUNCTIONS"""
# Text variables
title = 'National Python Football League'
subheading = '( Indledende programmering - Eksamensopgave 2 )'
option_header = 'Choose your option:'
option_1 = '1) See standings'
option_2 = '2) See teams'

# Layout variables
width = 60

class render:
    def render_main(title, subheading, option_header, option_1, option_2):
        """ Function that renders main menu """
        from colorama import Fore, Back, Style
        # Reset styles
        print(Back.RESET)
        print(Fore.RESET)
        ### Menu-header
        print(Fore.YELLOW)
        print((layout.center(title)*' ') + title + (layout.center(title)*' '))
        print(Fore.RESET)
        print(layout.center(subheading)*'-' + subheading + layout.center(subheading)*'-')
        ### Menu-body
        print(Back.WHITE)
        print(Fore.BLACK)
        print(layout.center(option_header)*' ' + option_header + layout.center(option_header)*' ')
        print(20*'- -')
        print(layout.center(option_1)*' ' + option_1 + layout.center(option_1)*' ')
        print(layout.center(option_2)*' ' + option_2 + layout.center(option_2)*' ')
        print(width*' ')
        # Reset styles
        print(Back.RESET)
        print(Fore.RESET)
    
    def render_match_log():
        """ Function that renders stadings if user selects 1. """
        # Importing data for rendering
        import pandas as pd
        from eksamensopgave_2.elements.import_data import imports as imp
        df = imp.construct_match_df()
        df = df[['team1', 'team2', 'points_team_1', 'points_team_2']]
        print(df)



class layout:
    """ Class that controls layout functions """
    def center(text):
        """ Function that centers text """
        spacing = int(width/2-len(text)/2)
        return spacing