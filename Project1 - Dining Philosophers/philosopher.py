"""
An example of the deadlock-philosopher problem we talked about.  Needs fixing!

8/23/2019, ASR
Solution: Let one of the philosophers be dyslexic. He always picks up his right fork first, then his left.
--> See "notepadPhilosopher.txt" for further notes and discussion of my thought process.
--> See "philosopher_test.txt" for the results of some test runs. The fixed version didn't hang so far!

8/27/2019, ASR
Optimize Solution: Moarrr dyslexia! Make every other philosopher dyslexic (Alternating Dyslexic Philosophers solution)
--> See "Resource Hierarchy Optimization.pdf" for the idea here on my improved solution.

"""


# For the purpose of this example, a fork will literally be a threading.Lock
# object but thematically it makes more sense in context of what we talked about
# to keep calling it a fork :D
from threading import Lock as Fork
from threading import Thread
from time import sleep, time

if __name__ == '__main__':
    SEATS_PER_TABLE = 5
    MEALS = 100                 # Hmmm, why does it never seem to end when I
                                # increase this number?  When I make it smaller, it
                                # the program seems to terminate quicker...
    MEAL_CONSUMPTION_TIME = 0.01   # Hmmm, why does it never seem to end when I
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
                sleep(MEAL_CONSUMPTION_TIME)
                self.meals_eaten += 1


    def eat_v1_dyslexic(self):
    # Half the philosophers are dyslexic. They take the right fork first, then left.
        self.right.acquire()
        self.left.acquire()
        sleep(MEAL_CONSUMPTION_TIME)
        self.meals_eaten += 1
        self.left.release()
        self.right.release()

    def eat_v2_dyslexic(self):
    # Half the philosophers are dyslexic. They take the right fork first, then left.
        with self.right:
            with self.left:
                sleep(MEAL_CONSUMPTION_TIME)
                self.meals_eaten += 1

class Philosoper(Thread):
    def __init__(self, number):
        super(Philosoper, self).__init__()
        self.number = number
        self.plate = None

    def run(self):
        if self.number % 2 == 1:
            # every other philosopher is dyslexic.
            for meal in range(MEALS//2):
                self.plate.eat_v1_dyslexic()
                self.plate.eat_v2_dyslexic()
        else:
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

if __name__ == '__main__':
    table = Table(SEATS_PER_TABLE)
    table.go()


