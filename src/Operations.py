"""
    Desc: This is the Operations class
    This class is responsible for keeping 
    track of time for the algorithm we 
    will be running.

    For Reference: I have used this to create my 
    own version

    link: https://realpython.com/python-timer/#python-timer-functions
"""

# Imports 
import time

class Operations:
    Time_elapsedTime = None
    Time_startTime = None 
    Time_timeDiff = None

    def __init__(self):
        self.Time_elapsedTime = None
        self.Time_startTime = None
        self.Time_timeDiff = None        

    def start(self): 
        """
            Raise Error if we haven't constructed anything
        """
        if self.Time_startTime is not None:
            raise TimeErrorException(2)

        self.Time_startTime = time.time_ns()

    def end(self):
        """
            Raise Error if there is nothing to end
        """
        if self.Time_startTime is None:
            raise TimeErrorException(3)
        
        self.Time_timeDiff = self.timeElapsed()

    """
        Time that elapsed
    """
    def timeElapsed(self):
        self.Time_elapsedTime = time.time_ns() - self.Time_startTime
        return self.Time_elapsedTime

    def getDiff(self):
        """
            Raise Error if there is no Diffrence
        """
        if(self.Time_timeDiff is None):
            raise TimeErrorException(4)

        return self.Time_timeDiff
     
"""
    Custom Time Error
    This is reference from the link in the header
"""
class TimeErrorException(Exception):

    def ThrowTimeError():
        if(Exception == 0):
            print("Timer is not Running!")
        elif(Exception == 1):
            print("Timer has already started!") # <-- Might be Dead code ~ Rezvee TODO: Fix this BS
        elif(Exception == 2):
            print("Timer did not construct yet")
        elif(Exception == 3):
            print("Timer started! Please Stop the timer before starting again")
        elif(Exception == 4):
            print("Timer has not stopped.")
        else:
            print("Unknown Error has occured")