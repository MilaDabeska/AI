from searching_framework.utils import Problem
from searching_framework.informed import *


def valid(state):
    farmer, wolf, goat, cabbage = state
    if wolf == goat and farmer != wolf:
        return False
    if goat == cabbage and farmer != goat:
        return False
    return True


class Farmer(Problem):
    def __init__(self, initial, goal=None):
        super(Farmer, self).__init__(initial, goal)

    def successor(self, state):
        successors = dict()

        farmer, wolf, goat, cabbage = state

        # farmerot se prenesuva samiot sebe
        farmer_new = 'e' if farmer == 'w' else 'w'
        state_new = farmer_new, wolf, goat, cabbage
        if valid(state_new):
            successors['Farmer nosi farmer'] = state_new

        # farmerot go prenesuva volkot
        if farmer == wolf:
            wolf_new = 'e' if farmer == 'w' else 'w'
            state_new = farmer_new, wolf_new, goat, cabbage
            if valid(state_new):
                successors['Farmer nosi volk'] = state_new

        # farmerot go prenesuva jareto
        if farmer == goat:
            goat_new = 'e' if farmer == 'w' else 'w'
            state_new = farmer_new, wolf, goat_new, cabbage
            if valid(state_new):
                successors['Farmer nosi jare'] = state_new

        # farmerot ja prenesuva zelkata
        if farmer == cabbage:
            cabbage_new = 'e' if farmer == 'w' else 'w'
            state_new = farmer_new, wolf, goat, cabbage_new
            if valid(state_new):
                successors['Farmer nosi zelka'] = state_new
        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return

    def h(self, node):
        state = node.state
        goal = self.goal
        value = 0
        for x, y in zip(state, goal):
            if x != y:
                value += 1
        return value


if __name__ == '__main__':
    initial_state = ('e', 'e', 'e', 'e')  # east
    goal_state = ('w', 'w', 'w', 'w')  # west

    farmer = Farmer(initial_state, goal_state)
    print(astar_search(farmer).solution())
