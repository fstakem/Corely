# ------------------------------------------------------
#
#   State.py
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
class State(Jsonable):
    
    # Setup logging
    logger = Utilities.getLogger(__name__)
    
    def __init__(self, transition_table=[], name=__name__):
        self.name = name
        self.transition_table = transition_table
        
    def nextState(self, buffer):
        pass
    
    def enterState(self):
        State.logger.debug('Entering state: %s' % (self.name))
    
    def exitState(self):
        State.logger.debug('Exiting state: %s' % (self.name))
        
    def isFinalState(self):
        if len(self.transition_table) == 0:
            return True
        
        return False
 
    