"""
An example of the deadlock-philosopher problem we talked about.  Needs fixing!
"""

# For the purpose of this example, a fork will literally be a threading.Lock
# object but thematically it makes more sense in context of what we talked about
# to keep calling it a fork :D
from threading import Lock as Fork
from threading import Thread
from time import sleep, time

SEATS_PER_TABLE = 5
MEALS = 100                 # Hmmm, why does it never seem to end when I
                            # increase this number?  When I make it smaller, it
                            # the program seems to terminate quicker...
MEAL_CONSUMPTION_TIME = 0   # Hmmm, why does it never seem to end when I
                            # increase this number to 0.1?

class Plate(object):
    def __init__(self, left_fork=None, right_fork=None,):
        self.left = left_fork
        self.right = right_fork
        self.meals_eaten = 0

    def eat_v1(self):
        # In order to eat a meal, both forks are required and cannot be shared
        # with anyone else
        self.left.acquire()
        self.right.acquire()
        sleep(MEAL_CONSUMPTION_TIME)
        self.meals_eaten += 1
        self.right.release()
        self.left.release()

    def eat_v2(self):
        # This is a more "pythonic" way to do locks using the "with" statement
        # but it is essentially equivalent to eat_v1()
        with self.left:
            with self.right:
                self.meals_eaten += 1

class Philosoper(Thread):
    def __init__(self, number):
        super(Philosoper, self).__init__()
        self.number = number
        self.plate = None

    def run(self):
        for meal in range(MEALS//2):
            self.plate.eat_v1()
            self.plate.eat_v2()


class Table(object):
    def __init__(self, seats):
        # Create seats with philosophers sitting in them
        self._seats = [Philosoper(n) for n in range(seats)]
        # Make a left fork for each seat (ultimately, the right fork will be the
        # left fork of the previous seat)
        self._forks = [
            Fork()
            for seat in self._seats
        ]
        # Create the plates
        self._plates = [
            Plate()
            for seat in self._seats
        ]

        # Assign the forks to the plates
        previous_left_fork = None
        for plate, fork in zip(self._plates, self._forks):
            plate.left = fork
            plate.right = previous_left_fork
            previous_left_fork = fork


        # Don't forget to wrap around!
        self._plates[0].right = previous_left_fork

    def go(self):
        start_time = time()
        # Give everyone a plate and dig in
        for eater, plate in zip(self._seats, self._plates):
            eater.plate = plate
            eater.start()

        # Wait for eaters to finish...
        for eater in self._seats:
            eater.join()

        print("Successfully eating {} meals in {} seconds".format(MEALS, time()-start_time))

table = Table(SEATS_PER_TABLE)
table.go()


