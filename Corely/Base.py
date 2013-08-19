# ------------------------------------------------------
#
#   Base.py
#   By: Fred Stakem
#   Created: 8.16.13
#
# ------------------------------------------------------


# Libs
# None

# User defined
# None

# Main
class Base(object):
    
    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False

    def __ne__(self, other):
        return not self.__eq__(other)