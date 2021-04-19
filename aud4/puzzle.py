from searching_framework.utils import Problem
from searching_framework.informed import *


class Puzzle(Problem):
    def __init__(self, initial, goal=None):
        super(Puzzle, self).__init__(initial, goal)

    def successor(self, state):
        """
         state = '*32415678'
                0 1 2
                3 4 5
                6 7 8
        """
        successors = dict()

        idx = state.index('*')  # prvo pojavuvanje na daden element,index na prazno pole
        if idx >= 3:
            tmp = list(state)
            tmp[idx], tmp[idx - 3] = tmp[idx - 3], tmp[idx]  # zamena na elementi
            new_state = ''.join(tmp)  # spojuvanje na stringovi
            successors['Gore'] = new_state

        if idx <= 5:
            tmp = list(state)
            tmp[idx], tmp[idx + 3] = tmp[idx + 3], tmp[idx]  # zamena na elementi
            new_state = ''.join(tmp)  # spojuvanje na stringovi
            successors['Dolu'] = new_state

        if idx % 3 != 0:  # gi isklucuvame 0,3,6
            tmp = list(state)
            tmp[idx], tmp[idx - 1] = tmp[idx - 1], tmp[idx]  # zamena na elementi
            new_state = ''.join(tmp)  # spojuvanje na stringovi
            successors['Levo'] = new_state

        if idx % 3 != 2:
            tmp = list(state)
            tmp[idx], tmp[idx + 1] = tmp[idx + 1], tmp[idx]  # zamena na elementi
            new_state = ''.join(tmp)  # spojuvanje na stringovi
            successors['Desno'] = new_state

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def h(self, node):  # hevristika,br na polinja koi ne se na vistinsko mesto
        counter = 0

        """
        a = [1, 2, 3] b = ['a', 'b', 'c']
        zip(a, b) = [(1, 'a'), (2, 'b'), (3, 'c')]
        """

        for x, y in zip(node.state, self.goal):  # so 1 ciklus da izmineme 2 listi odednash
            if x != y:  # dali momentalnoto pole e razlicno so ocekuvanoto
                counter += 1

        return counter


class Puzzle2(Puzzle):
    coordinates = {0: (0, 2), 1: (1, 2), 2: (2, 2), 3: (0, 1), 4: (1, 1), 5: (2, 1), 6: (0, 0), 7: (1, 0), 8: (2, 0)}
    """
    state = '*32415678'
           0 1 2
           3 4 5
           6 7 8
    """

    @staticmethod
    def mhd(n, m):  # manhattan rastojanie
        x1, y1 = Puzzle2.coordinates[n]  # na daden index n koi mu se negovite x i y koordinati
        x2, y2 = Puzzle2.coordinates[m]  # na daden index m koi mu se negovite x i y koordinati

        return abs(x1 - x2) + abs(y1 - y2)

    def h(self, node):
        sum_value = 0

        for x in '12345678':  # se izminuva sekoj string
            value = Puzzle2.mhd(node.state.index(x), int(x))
            sum_value += value

        return sum_value


if __name__ == '__main__':
    puzzle = Puzzle('*32415678', '*12345678')
    # print(greedy_best_first_graph_search(puzzle).solution())
    # print(greedy_best_first_graph_search(puzzle).solve())
    print(astar_search(puzzle).solution())
    print(astar_search(puzzle).solve())
    # print(recursive_best_first_search(puzzle).solution())
    # print(recursive_best_first_search(puzzle).solve())

    puzzle = Puzzle2('*32415678', '*12345678')
    # print(greedy_best_first_graph_search(puzzle).solution())
    # print(greedy_best_first_graph_search(puzzle).solve())
    print(astar_search(puzzle).solution())
    print(astar_search(puzzle).solve())
    # print(recursive_best_first_search(puzzle).solution())
    # print(recursive_best_first_search(puzzle).solve())
