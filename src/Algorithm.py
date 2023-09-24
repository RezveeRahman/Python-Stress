"""
    This is the algorithm section. 
"""

class Algorithm:
    """
        Algorithm    
    """
    INT_LIMIT = 10_000_000
    FLOAT_LIMIT = 10_000_000
    intPerf = 0
    floatPerf = 0.0
    
    def __init__(self):
        self.intPerf = 0
        self.floatPerf = 0.0

    def startIOPS(self): 
        while(self.intPerf != self.INT_LIMIT ):
            self.intPerf += 1

    def startFlops(self):
        while(self.floatPerf < self.FLOAT_LIMIT):
            self.floatPerf += 1.0
    
    #XXX: MAYBE USE BIT-SHIFT?
    # BAD IDEA USE REGULAR INCREMENT ~ Rezvee
        