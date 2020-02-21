"""
Run benchmarks on the philosopher.py method.
 > vary meals
 > vary meal_consumption_time
 > collect the data points as triples (meals, meal_consumption_time, run_time)
"""
from threading import Lock as Fork
from threading import Thread
from time import sleep, time

from philosopher_waiter_module import Table
from philosopher_waiter_module import Plate
from philosopher_waiter_module import Philosoper
from philosopher_waiter_module import Waiter 

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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
        # raw data is a list of 3-tuples

    def addDatum(self, datum):
        # check datum is a 3-tuple
        if isinstance(datum, tuple):
            if len(datum) == 3:
                self.data.append(datum)
            else:
                print("ERROR: Datum is not length 3. Use format (meals, meal_consumption_time, run_time)")
        else:
            print("ERROR: Datum is not a tuple. Use format (meals, meal_consumption_time, run_time)")

    def Bench(self, seats_per_table, meals, meal_consumption_time,):
        # execute the code with a set of inputs and return the run time.
        table = Table(seats_per_table, meals, meal_consumption_time)
        t = table.go()
        return t

    def buildMatrix(self):
        # USE PANDAS FOR THIS
        pass

    def plotData(self):
        # IMPORT MATPLOTLIB and/or SCIPLOTLIB for this.
        # --> get average and variance on t for each (x,y)
        # --> x-y-t surface plot of average
        # --> x-y-t surface plot of variance
        pass


### Run some benchmarks and add them to the database ###
# Initialize the database:
db = database()

# Do some Plotting and Analyzing stuff
toggle = 'on'
if toggle == 'on':
    # make the pandas data frame
    df = pd.read_csv('data.txt')
    x = df['meals']
    y = df['meal_time']
    z = df['run_time']
    
    #do some plotting-- scatter plot to start EZ
    #                -- stacked line plots for time vs. x, varying y
    #                -- stacked line plots for time vs. y, varying x
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    Axes3D.scatter(x,y,z)

# Vary MEALS @ MEAL_CONSUMPTION_TIME = 0.00
toggle = 'off' # turn this chunk ON or OFF
if toggle == 'on':
    # static vars:
    seats_per_table = 5
    meal_consumption_time = 0.01
    # varying:
    inp_meals = [1,10,50]
    for meals in inp_meals:
        run_time = db.Bench(seats_per_table, meals, meal_consumption_time)
        newDatum = (meals, meal_consumption_time, run_time)
        db.addDatum(newDatum)
    #write to file
    file1 = open("benchmark_data_philosopher_waiter.txt", "a")
    write_data = [
        str(db.data[i])+"\n" for i in range(len(db.data))
    ]
    file1.writelines(write_data)
    file1.close()

# Vary MEALS and MEAL_CONSUMPTION_TIME
toggle = 'off'
if toggle == 'on':
    for i in range(30): # a statistical sampling!!
        seats_per_table = 5
        inp_meals = [1, 10, 50, 100]
        inp_meal_consumption_time = [0.000, 0.005, 0.010]
        for x in inp_meals:
            for y in inp_meal_consumption_time:
                t = db.Bench(seats_per_table, x, y)
                newDatum = (x, y, t)
                db.addDatum(newDatum)
    #write to file
    file1 = open("benchmark_data_philosopher_waiter.txt", "a")
    write_data = [
        str(db.data[i])+"\n" for i in range(len(db.data))
    ]
    file1.writelines(write_data)
    file1.close()