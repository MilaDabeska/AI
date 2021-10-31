from frameworks.uninformed import *


# x1 < 8 ; x1 > 0 -> u slucaj da ne iskoci od tablata
# [x1 + 1, y1] != [x2, y2] and [x1 + 1, y1] != [x3, y3] -> da ne se preklopuva so dr atomi


def move_right(x1, y1, x2, y2, x3, y3, obstacles):  # dvizenje na povekje pozicii za desno
    while x1 < 8 and [x1 + 1, y1] not in obstacles and [x1 + 1, y1] != [x2, y2] and [x1 + 1, y1] != [x3, y3]:
        x1 += 1
    return x1


def move_left(x1, y1, x2, y2, x3, y3, obstacles):  # dvizenje na povekje pozicii za levo
    while x1 > 0 and [x1 - 1, y1] not in obstacles and [x1 - 1, y1] != [x2, y2] and [x1 - 1, y1] != [x3, y3]:
        x1 -= 1
    return x1


def move_up(x1, y1, x2, y2, x3, y3, obstacles):  # dvizenje na povekje pozicii nagore
    while y1 < 6 and [x1, y1 + 1] not in obstacles and [x1, y1 + 1] != [x2, y2] and [x1, y1 + 1] != [x3, y3]:
        y1 += 1
    return y1


def move_down(x1, y1, x2, y2, x3, y3, obstacles):  # dvizenje na povekje pozicii nadolu
    while y1 > 0 and [x1, y1 - 1] not in obstacles and [x1, y1 - 1] != [x2, y2] and [x1, y1 - 1] != [x3, y3]:
        y1 -= 1
    return y1


class Molecule(Problem):
    def __init__(self, obstacles, initial, goal=None):
        super(Molecule, self).__init__(initial, goal)
        self.obstacles = obstacles

    def successor(self, state):
        successors = dict()

        h1_x, h1_y = state[0], state[1]  # koordinati za prviot atom
        o_x, o_y = state[2], state[3]  # koordinati za kislorod
        h2_x, h2_y = state[4], state[5]  # koordinati za vtoriot atom

        # H1 atom
        x_new = move_right(h1_x, h1_y, o_x, o_y, h2_x, h2_y, self.obstacles)
        if x_new != h1_x:
            successors['RightH1'] = (x_new, h1_y, o_x, o_y, h2_x, h2_y)

        x_new = move_left(h1_x, h1_y, o_x, o_y, h2_x, h2_y, self.obstacles)
        if x_new != h1_x:
            successors['LeftH1'] = (x_new, h1_y, o_x, o_y, h2_x, h2_y)

        y_new = move_up(h1_x, h1_y, o_x, o_y, h2_x, h2_y, self.obstacles)
        if y_new != h1_y:
            successors['UpH1'] = (h1_x, y_new, o_x, o_y, h2_x, h2_y)

        y_new = move_down(h1_x, h1_y, o_x, o_y, h2_x, h2_y, self.obstacles)
        if y_new != h1_y:
            successors['DownH1'] = (h1_x, y_new, o_x, o_y, h2_x, h2_y)

        # H2 atom
        x_new = move_right(h1_x, h1_y, o_x, o_y, h2_x, h2_y, self.obstacles)
        if x_new != h2_x:
            successors['RightH2'] = (x_new, h1_y, o_x, o_y, x_new, h2_y)

        x_new = move_left(h1_x, h1_y, o_x, o_y, h2_x, h2_y, self.obstacles)
        if x_new != h2_x:
            successors['LeftH2'] = (x_new, h1_y, o_x, o_y, x_new, h2_y)

        y_new = move_up(h1_x, h1_y, o_x, o_y, h2_x, h2_y, self.obstacles)
        if y_new != h2_y:
            successors['UpH2'] = (h1_x, y_new, o_x, o_y, h2_x, y_new)

        y_new = move_down(h1_x, h1_y, o_x, o_y, h2_x, h2_y, self.obstacles)
        if y_new != h2_y:
            successors['DownH2'] = (h1_x, y_new, o_x, o_y, h2_x, y_new)

        # O atom
        x_new = move_right(h1_x, h1_y, o_x, o_y, h2_x, h2_y, self.obstacles)
        if x_new != o_x:
            successors['RightO'] = (x_new, h1_y, x_new, o_y, h2_x, h2_y)

        x_new = move_left(h1_x, h1_y, o_x, o_y, h2_x, h2_y, self.obstacles)
        if x_new != o_x:
            successors['LeftO'] = (x_new, h1_y, x_new, o_y, h2_x, h2_y)

        y_new = move_up(h1_x, h1_y, o_x, o_y, h2_x, h2_y, self.obstacles)
        if y_new != o_y:
            successors['UpO'] = (h1_x, y_new, o_x, y_new, h2_x, h2_y)

        y_new = move_down(h1_x, h1_y, o_x, o_y, h2_x, h2_y, self.obstacles)
        if y_new != o_y:
            successors['DownO'] = (h1_x, y_new, o_x, y_new, h2_x, h2_y)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        # pozicioniranje na atomite vo redosled, H1 O H2
        # treba da se naogjaat na ista y_position koordinata
        return state[1] == state[3] == state[5] and state[0] + 1 == state[2] and state[2] + 1 == state[4]


if __name__ == '__main__':
    obstacles_list = [[0, 1], [1, 1], [1, 3], [0, 1], [2, 5], [3, 1], [3, 6],
                      [5, 6], [6, 1], [6, 2], [6, 3], [7, 3], [7, 6], [8, 5]]
    h1_pos = [2, 1]
    h2_pos = [2, 6]
    o_pos = [7, 2]

    molecule = Molecule(obstacles_list, (h1_pos[0], h1_pos[1], o_pos[0], o_pos[1], h2_pos[0], h2_pos[1]))
    print(breadth_first_graph_search(molecule).solution())
