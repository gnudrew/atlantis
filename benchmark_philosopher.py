"""
Run benchmarks on the philosopher.py method.

"""
from philosopher import Plate
from philosopher import Philosoper
from philosopher import Table

def Bench(seats_per_table, meals, meal_consumption_time):
    table = Table(seats_per_table)
    t = table.go()
    return t

class database:
    # store our benchmark run data here
    # Goal: 2D Matrix (x,y,z) = (meals, meal_consumption_time, time)
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

    def addDatum(self, datum):
        # must be a 3-tuple
        if isinstance(datum, tuple):
            if len(datum) == 3:
                self.data.append(datum)
            else:
                print("ERROR: Datum is not length 3. Use format (meals, meal_consumption_time, time)")
        else:
            print("ERROR: Datum is not a tuple. Use format (meals, meal_consumption_time, time)")

    def buildMatrix(self):
        pass

### Run some benchmarks and add them to the database ###
# Vary MEALS @ MEAL_CONSUMPTION_TIME = 0.00
for

# Vary MEALS @ MEAL_CONSUMPTION_TIME = 0.01

# Vary MEALS @ MEAL_CONSUMPTION_TIME = 0.01