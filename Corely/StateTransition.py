# ------------------------------------------------------
#
#   StateTransition.py
#   By: Fred Stakem
#   Created: 6.23.13
#
# ------------------------------------------------------


# Libs
# None

# User defined
from Utilities import *
from Jsonable import Jsonable

# Main
class StateTransition(Jsonable):
    
    # Setup logging
    logger = Utilities.getLogger(__name__)
    
    def __init__(self, next_state=None, name=__name__):
        self.name = name
        self.next_state = next_state
        
    def isMatch(self, buffer):
        pass
                             

    
    