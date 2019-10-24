"""
Run benchmarks on the philosopher.py method.
 > vary meals
 > vary meal_consumption_time
 > collect the data points as triples (meals, meal_consumption_time, run_time)
"""
from threading import Lock as Fork
from threading import Thread
from time import sleep, time
import philosopher_waiter_module

class database:
    # store our benchmark run data here
    # Goal: 2D Matrix (x,y,z) = (meals, meal_consumption_time, run_time)
    #  M_C_T \ MEALS  10  20  50  100 200 ...
    #                ---  --  --  --- --- ---
    #    0.00      | t    t   t    t   t
    #    0.01      | t    t   t    t   t
    #    0.02      | t    t   t    t   t  ...
    #    0.05      | t    t   t    t   t
    #    0.1       | t    t   t    t   t
    #    ...       |         ...          ...
    #
    def __init__(self):
        self.data = []
        # raw data as a list of 3-tuples

    def Bench(self, seats_per_table, meals, meal_consumption_time,):
        # execute the code with a set of inputs and return the run time.
        table = Table(seats_per_table)
        t = table.go()
        return t

    def addDatum(self, datum):
        # must be a 3-tuple
        if isinstance(datum, tuple):
            if len(datum) == 3:
                self.data.append(datum)
            else:
                print("ERROR: Datum is not length 3. Use format (meals, meal_consumption_time, run_time)")
        else:
            print("ERROR: Datum is not a tuple. Use format (meals, meal_consumption_time, run_time)")

    def buildMatrix(self):
        pass

    def plotData(self):
        # --> get average and variance on t for each (x,y)
        # --> x-y-t surface plot of average
        # --> x-y-t surface plot of variance
        pass


### Run some benchmarks and add them to the database ###
# Initialize the database:
db = database()

# Vary MEALS @ MEAL_CONSUMPTION_TIME = 0.00
# static vars:
seats_per_table = 5
meal_consumption_time = 0.01
# varying:
inp_meals = [1,10,50,100,200,500,1000]
for meals in inp_meals:
    run_time = db.Bench(seats_per_table, meals, meal_consumption_time)
    db.addDatum(meals, meal_consumption_time, run_time)

# Vary MEALS @ MEAL_CONSUMPTION_TIME = 0.01

# Vary MEALS @ MEAL_CONSUMPTION_TIME = 0.01

# Vary MEALS and MEAL_CONSUMPTION_TIME
seats_per_table = 5
inp_meals = [1, 10, 50, 100, 500, 1000]
inp_meal_consumption_time = [0.000, 0.005, 0.010, 0.020]
for x in inp_meals:
    for y in inp_meal_consumption_time:
        t = db.Bench(seats_per_table, x, y)
        db.addDatum(x, y, t)