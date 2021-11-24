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
import math
from colorama import Fore, Back, Style
rounds = rounds.copy()
paths = paths.copy()


# Importing data

# App rendering
## render main menu
ren.render_main(title, subheading, subheading_2, option_header, option_1, option_2, option_3)
ren.render_match_log()
print('Width is currently: ' + str(width))