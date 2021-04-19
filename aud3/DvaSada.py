from searching_framework.utils import Problem
from searching_framework.uninformed import *

class Container(Problem):
    def __init__(self, capacities, initial, goal=None):
        super().__init__(initial,goal)
        self.capacities = capacities

    def successor(self, state):
        successors = dict()

        x, y = state  # tekovni vrednosti za tecnosta vo sadovite
        c0, c1 = self.capacities  # maksimalnite kapaciteti

        if x > 0:
            successors['Isprazni go sadot J0'] = (0, y)  # praznenje na prviot sad J0

        if y > 0:
            successors['Isprazni go sadot J1'] = (0, y)  # praznenje na vtoriot sad J1


        # preturanje vo tecnost od eden vo drug sad,od J0 vo J1
        # treba da bideme sig deka vo J0 ima tecnost, x_position > 0
        # dali vo J1 mozeme da prefrlime nekoja tecnost, y_position < c1
        if x > 0 and y < c1:
            delta = min(x, c1 - y)  # min vrednost od ona sto go imame vo sadot J0
            # i ona sto mozeme da go smestime vo sadot J1,kapacitetot na J1 - ona sto momentalno go imame vo toj sad
            successors['Preturi od sadot J0 vo J1'] = (
            x - delta, y + delta)  # toa sto go imame - toa sto kje go preturime,
            # toa sto go imame + toa sto sakame da go dodademe

        # obratno
        if y > 0 and x < c0:
            delta = min(y, c0 - x)
            successors['Preturi od sadot J1 vo J0'] = (x + delta, y - delta)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        # proverka na tekovnata sostojba so celnata sostojba
        return state == self.goal


if __name__ == '__main__':
    container = Container([15, 5], (5, 5), (10, 0))
    result=breadth_first_graph_search(container)
    print(result.solution())

    result=depth_first_graph_search(container)
    print(result.solution())
