import unittest
from TimeCounter import TimeCounter

class TestTimeCounter(unittest.TestCase):
    def testIncrement(self):
        #1
        counter = TimeCounter()
        counter.increment(60)
        self.assertEqual(counter.getTime(), 60)
        #2 FAIL TEST CASE
        counter = TimeCounter()
        counter.increment(120)
        self.assertEqual(counter.getTime(), 130) 
        #3
        counter = TimeCounter(initial_time=30)
        counter.increment(30)
        self.assertEqual(counter.getTime(), 60)


    def testDecrement(self):
        #1
        counter = TimeCounter(initial_time=120)
        counter.decrement(60)
        self.assertEqual(counter.getTime(), 60)
        #2
        counter = TimeCounter(initial_time=90)  
        counter.decrement(30)
        self.assertEqual(counter.getTime(), 60)
        #3 FAIL test case
        counter = TimeCounter(initial_time=30)
        counter.decrement(45) 
        self.assertEqual(counter.getTime(), 0)
        
    def testDisplayStandardTime(self):
        #test case 1
        counter = TimeCounter(initial_time=364)
        self.assertEqual(counter.displayStandardTime(), "00:06:04")
        #test case 2
        counter = TimeCounter(initial_time=3661)
        self.assertEqual(counter.displayStandardTime(), "01:01:01")
        #test case 3
        counter = TimeCounter(initial_time=7890)
        self.assertEqual(counter.displayStandardTime(), "02:11:30")

    def testDisplayMilitaryTime(self):
        #test case 1 
        counter = TimeCounter(initial_time=254)
        self.assertEqual(counter.displayMilitaryTime(), "00:04:14")
        #test case 2 
        counter = TimeCounter(initial_time=3661)
        self.assertEqual(counter.displayMilitaryTime(), "01:01:01")
        #test csae 3
        counter = TimeCounter(initial_time=9876)
        self.assertEqual(counter.displayMilitaryTime(), "02:44:36")
        
    def testReset(self):
        counter = TimeCounter(initial_time=3661)
        counter.reset()
        self.assertEqual(counter.getTime(), 0)
    
    def testEdgeCases(self):
        counter = TimeCounter()
        counter.increment(3600)  # Increment by 1 hour
        self.assertEqual(counter.getTime(), 3600)


if __name__ == '__main__':
    unittest.main(verbosity=2)
