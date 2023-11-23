*** TimeCounter.py ***

A python library created to develop a easy-to-use time counter functionality for developers. 

Constructor : Constructor: __init__(self, initial_time=0)
 - Initialized a new instance of the 'TimeCounter' class
Parameters - 'initial time' The initial time for the counter in seconds. 

Increment Method : def increment(self, increment_seconds=1):
- Increments the time counter by a specific # of seconds 
Parameters - 'increment_seconds' #seconds to increment. 

Decrement Method : def decrement(self, decrement_seconds=1): 
 - Decrements the time coutner by a specific # of seconds. 
 Parameters - The number of seconds to decrement. 

GetTimeMethod : getTime(self)
- Getter to retrieve the current time (seconds)
returns an int

DisplayStandardTime : def displayStandardTime(self):
- Converts and displays the current time in standard time format
(HH | MM | SS)
returns a formatted string 

DisplayMilitaryTime : def displayMilitaryTime(self):
- Converts and displays the current time in military time format (HH | MM | SS)
returns a formatted string

Reset Method : def reset(self):
-Resets the time counter to 0, allowing a fresh start. 


------------------------------------------------------------------
*** TimeTimeCounter.py ***


TestCases : 

Increment:
#1 - PASS Test case increment 60
#2 - FAIL - Intentional Fail to test functionality
#3 - Pass 

Decrement:

#1 - Pass Decremental values
#2 - Pass different decremental values 
#3 - Fail trying to decrement more than current time

DisplayStandardTime: 
#1 - Pass
#2 - Pass
#3 - Pass

DisplayMilitaryTime: 
#1 - Pass
#2 - Pass 
#3 - Pass 

Reset - 
#1 - Pass

Edge Case : 
Trying to incrementing by the maximum allowed time