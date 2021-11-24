# Kør dette program for at køre appen.
# importing libraries 
import sys
sys.path.append(".")
import pandas as pd
from uuid import uuid4 # Helps generate unique ids
from eksamensopgave_2.elements.import_data import imports as imp
from eksamensopgave_2.elements.import_data import rounds, paths
import math
rounds = rounds.copy()
paths = paths.copy()


# Importing data
rD = imp.import_rounds(rounds, paths)
mD = imp.import_matches()
rM = imp.render_matches(mD)

# Render menu
# Text-variables
title = 'National Python Football League'
subheading = '( Indledende programmering - Eksamensopgave 2 )'
# Spacing
width = 60
title_spacing = int(width/2-len(title)/2)
subheading_spacing = int(width/2-len(subheading)/2)

## Print statements
print((title_spacing*' ') + title + (title_spacing*' '))
print(subheading_spacing*'-' + subheading + subheading_spacing*'-')
print(60*'_')

