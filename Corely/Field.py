# ------------------------------------------------------
#
#   Field.py
#   By: Fred Stakem
#   Created: 8.1.13
#
# ------------------------------------------------------


# Libs
# None

# User defined
from Utilities import *
from Node import Node

# Main
class Field(Node):
    
    # Setup logging
    logger = Utilities.getLogger(__name__)
    
    def __init__(self, data=None, children=[], name=__name__):
        super(Field, self).__init__(children, name)
        self.data = data
        
            


    
    
                
                
                
                
                
                
                
                
                
            
            