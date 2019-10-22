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

seats_per_table = 5
meals = 100
meal_consumption_time = 0

class Plate:
    def __init__(self, left_fork=None, right_fork=None,):
        self.left = left_fork
        self.right = right_fork
        self.meals_eaten = 0

    def eat_v1(self, meal_consumption_time):
        # In order to eat a meal, both forks are required and cannot be shared
        # with anyone else
        self.left.acquire()
        self.right.acquire()
        sleep(meal_consumption_time)
        self.meals_eaten += 1
        self.right.release()
        self.left.release()

    def eat_v2(self, meal_consumption_time):
        # This is a more "pythonic" way to do locks using the "with" statement
        # but it is essentially equivalent to eat_v1()
        with self.left:
            with self.right:
                sleep(meal_consumption_time)
                self.meals_eaten += 1


class Philosoper(Thread):
    def __init__(self, number, waiter = None):
        super(Philosoper, self).__init__()
        self.number = number
        self.plate = None
        self.waiter = waiter

    def run(self):
        for meal in range(meals//2):
            # Get index for left fork and right fork before asking the waiter
            # eater index goes with fork index and index + 1 (see Table class setting)
            n = self.number
            fork1_index = n
            #length = len(self.waiter._seats)
            if n + 1 == seats_per_table:
                fork2_index = 0  # wrap around!
            else:
                fork2_index = n + 1

            # To ask Jeeves, use a Lock for his attention
            with self.waiter._attention:
                can_i = self.waiter.ask(fork1_index, fork2_index)
                if can_i == 'yes':
                    self.plate.left.acquire()
                    self.plate.right.acquire()
            # release Jeeves' attn and start eating.
            self.plate.eat_v1(meal_consumption_time)
            self.plate.eat_v2(meal_consumption_time)
            # put down the forks
            self.plate.left.release()
            self.plate.right.release()
            # Update Jeeves; the forks are available
            self.waiter.markForkAvailable(fork1_index, fork2_index)


class Waiter:
    def __init__(self, seats, forks, plates):
        # Upon hire, the waiter is given a list of seats, forks, and plates to track.
        # The waiter keeps a list of which forks are available. 0 for not-in-use. 1 for in-use.
        # The waiter keeps a list of his current answer ('yes' or 'no') to each philosopher.
        self._seats = seats
        self._forks = forks
        self._plates = plates
        # initialize the queue to.. Ask Jeeves (TM)
        #self._queue = []
        # Endow Jeeves with singular attention (as a lock or "fork")
        self._attention = Fork()

    def __enter__(self):
        self._attention.acquire()

    def __exit__(self):
        self._attention.release()

    def makeForkStatusList(self):
        # initially set all forks status to 0, "not in use"
        # it lines up against indices for Forks list
        self._forkStatus = [
            [fork, 0] for fork in range(len(self._forks))
            ]

    def markForkInUse(self, fork1_index, fork2_index):
        self._forkStatus[fork1_index][1] = 0
        self._forkStatus[fork2_index][1] = 0

    def markForkAvailable(self, fork1_index, fork2_index):
        self._forkStatus[fork1_index][1] = 0
        self._forkStatus[fork2_index][1] = 0

    def ask(self, fork1_index, fork2_index):
        # Philosopher asks the waiter to pick up his forks, passing in the fork indices.
        # Waiter checks his list.
        #   If fork1 and fork2 are available, he gives this philosopher 'yes' and changes these forks status to 1, "in use".
        #   If they aren't both available, he gives this philosopher a 'no'.
#        print('f1: '+str(fork1_index))
#        print('f2: '+str(fork2_index))
        if self._forkStatus[fork1_index][1] == 0 and self._forkStatus[fork2_index][1] == 0:
            # give the philosopher a 'yes'
            #print('YES')
            #print('Before marked in use:')
            #print(self._forkStatus[fork1_index][1])
            #print(self._forkStatus[fork2_index][1])
            self.markForkInUse(fork1_index, fork2_index)
            #print('After marked in use:')
            #print(self._forkStatus[fork1_index][1])
            #print(self._forkStatus[fork2_index][1])
            # update fork status to in-use
            return 'yes'
        else:
            # give a 'no'
            #print('NO')
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
        # assign Jeeves to the table
        self._waiter = Jeeves

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
        end_time = time()

        # how long did it take?
        delta_t = start_time - end_time
        print(f"Successfully eating {meals} meals in {delta_t} seconds")
        return delta_t

table = Table(seats_per_table)
table.go()
