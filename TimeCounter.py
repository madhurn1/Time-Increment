class TimeCounter:
    def __init__(self, initial_time=0): ##constructor
        self.seconds = initial_time

    def increment(self, increment_seconds=1): #increment
        self.seconds += increment_seconds

    def decrement(self, decrement_seconds=1): #decrment
        self.seconds -= decrement_seconds

    def getTime(self): #getter
        return self.seconds

    def displayStandardTime(self): #display standard time
        hours, remainder = divmod(self.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    def displayMilitaryTime(self): #display military time.
        hours, remainder = divmod(self.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    def reset(self): #allows us to reset the time
        self.seconds = 0

