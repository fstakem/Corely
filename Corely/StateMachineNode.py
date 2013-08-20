# ------------------------------------------------------
#
#   StateMachineNode.py
#   By: Fred Stakem
#   Created: 7.26.13
#
# ------------------------------------------------------


# Libs
# None

# User defined
from Utilities import *
from StateMachine import StateMachine

# Main
class StateMachineNode(StateMachine):
    
    # Setup logging
    logger = Utilities.getLogger(__name__)
     
    def __init__(self, start_state=None, name=__name__, children=[]):
        super(StateMachineNode, self).__init__(start_state, name)
        self.children = children
        
    def isLeaf(self):
        if len(self.children) == 0:
            return True
        
        return False
        
    
        
