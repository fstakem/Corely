# ------------------------------------------------------
#
#   StateMachine.py
#   By: Fred Stakem
#   Created: 6.23.13
#
# ------------------------------------------------------


# Libs
# None

# User defined
from Globals import *
from Utilities import *
from State import State
from Jsonable import Jsonable

# Main
class StateMachine(Jsonable):
    
    # Setup logging
    logger = Utilities.getLogger(__name__)
    
    def __init__(self, start_state=None, name=__name__):
        self.name = name
        self.stream = None
        self.start_state = start_state
        self.current_state = None
        
    def start(self, stream):
        self.stream = stream
        self.stream.reset()
        
    def changeState(self, new_state):
        if self.current_state != None:
            self.current_state.exitState()
        self.current_state = new_state
        self.current_state.enterState()
    
    def reset(self):
        self.changeState(self.start_state)
                
  