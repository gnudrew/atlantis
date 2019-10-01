"""
An example of the deadlock-philosopher problem we talked about.  Needs fixing!

9/23/2019 ASR
Implement a 'Waiter' entity to manage the philosophers.
The rules for waiter-philosopher interaction shall be:
(1) philosophers must queue up to ask the waiter's permission before picking up a fork
(2) the waiter only allows a philosopher to pick up both forks or none at all (and return to back of the line).
(3) philosophers can put down forks without the waiter's permission
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
MEAL_CONSUMPTION_TIME = .01   # Hmmm, why does it never seem to end when I
                            # increase this number to 0.1?

class Plate:
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


class Philosoper(Thread):
    def __init__(self, number, waiter=None,):
        super(Philosoper, self).__init__()
        self.number = number
        self.plate = None
        self.waiter = waiter

    def run(self):
        for meal in range(MEALS//2):

            # Get index for left fork and right fork before asking Jeeves
            n = self.number # see how Table class sets the table; eater index matches to fork index and index + 1.
            fork1_index = n
            length = len(self.waiter._seats)
            if n + 1 == length:
                fork2_index = 0  # wrap around!
            else:
                fork2_index = n + 1

            # Ask Jeeves... and keep asking till he says yes.
            while self.waiter.ask(fork1_index, fork2_index) != 'yes':
                print("Philosopher "+self.number+" asked Jeeves and got a 'NO'.")
            self.plate.eat_v1()
            self.plate.eat_v2()

class Waiter:
    def __init__(self, seats, forks, plates):
        # Upon hire, the waiter is given a list of seats, forks, and plates to track.
        # The waiter keeps a list of which forks are available. 0 for not-in-use. 1 for in-use.
        # The waiter keeps a list of his current answer ('yes' or 'no') to each philosopher.
        #self._forksStatus = [0 for n in range(seats)]
        #self._askStatus = ['no' for n in range(seats)]
        self._seats = seats
        self._forks = forks
        self._plates = plates
        # initialize an asking queue
        self._queue = []

    def makeForkStatusList(self):
        # how many forks?
        n = len(self._forks)
        # initially set all forks status to 0, "not in use"
        self._forkStatus = zip(self._forks, [0]*n)

    def ask(self, fork1_index, fork2_index):
        # Philosopher at a given plate asks the waiter to pick up his forks.
        # Waiter checks his list.
        #   If fork1 and fork2 are available, he gives this philosopher 'yes' and changes these forks status to 1, "in use".
        #   If they aren't both available, he gives this philosopher a 'no'.
        print('f1:'+fork1_index)
        print('f2:'+fork2_index)
        if self._forkStatus[fork1_index][1] == 0 and self._forkStatus[fork2_index][1] == 0:
            # give the philosopher a 'yes'
            print('YES')
            return 'yes'
            # update fork status to in-use
            print('Before marked in use:')
            # Why does the program not seem be reading out to print the forkStatus values??
            print(self._forkStatus[fork1_index][1])
            print(self._forkStatus[fork2_index][1])
            self._forkStatus[fork1_index][1] = 1
            self._forkStatus[fork2_index][1] = 1
            print('After marked in use:')
            print(self._forkStatus[fork1_index][1])
            print(self._forkStatus[fork2_index][1])
        else:
            # give a 'no'
            print('NO')
            return 'no'

class Table:
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

        # Hire the waiter *ahem* Jeeves, giving him the list of seats, forks, and plates
        Jeeves = Waiter(self._seats, self._forks, self._plates)
        Jeeves.makeForkStatusList() # initially all forks are available

        # Let the philosophers know Jeeves is the waiter.
        for philo in self._seats:
            philo.waiter = Jeeves

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
