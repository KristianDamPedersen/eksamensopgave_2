# Kør dette program for at køre appen.
# importing libraries 
from os import terminal_size
import sys
sys.path.append(".")
import pandas as pd
from eksamensopgave_2.elements.import_data import imports as imp
from eksamensopgave_2.elements.import_data import rounds, paths
from eksamensopgave_2.elements.rendering import render as ren
from eksamensopgave_2.elements.rendering import title, subheading, subheading_2, option_header, option_1, option_2, option_3, terminal_size
from eksamensopgave_2.elements.rendering import layout as lay
from eksamensopgave_2.elements.rendering import width
from eksamensopgave_2.elements.logic import logic
from eksamensopgave_2.elements.logic import points_win, points_draw, points_loss
import math
from colorama import Fore, Back, Style
rounds = rounds.copy()
paths = paths.copy()

# Default logic variables
points_win = points_win
points_draw = points_draw
points_loss = points_loss
sortby = 'P'

# App rendering
## render main menu
ren.render_main(title, subheading, subheading_2, option_header, option_1, option_2, option_3)
        
## Print width of terminal (delete in production)
#print('Width is currently: ' + str(width))