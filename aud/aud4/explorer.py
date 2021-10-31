from frameworks.utils import Problem
from frameworks.informed import *


def update_obstacle_position(position):  # pomestuvanje na preprekite vertikalno
    x, y, direction = position
    if y == 0 and direction == -1 or y == 5 and direction == 1:  # dokolku y stigne do kraj na tablata,
        # nasokata se vrakja nazad
        direction *= -1
    y_new = y + direction
    position_new = x, y_new, direction
    return position_new


def chek_collision(man, obstacle1, obstacle2):
    return man != obstacle1[:2] and man != obstacle2[:2]  # [:2] -> od 0 do 2


class Explorer(Problem):
    def __init__(self, initial, goal=None):
        super(Explorer, self).__init__(initial, goal)

    def successor(self, state):
        successors = dict()

        x, y = state[0], state[1]  # pozicii na coveceto
        obstacle1 = (state[2], state[3], state[4])
        obstacle2 = (state[5], state[6], state[7])

        obstacle1_new = update_obstacle_position(obstacle1)
        obstacle2_new = update_obstacle_position(obstacle2)

        # right
        if x < 7:
            x_new = x + 1
            y_new = y
            man = x_new, y_new
            if chek_collision(man, obstacle1_new, obstacle2_new):
                successors['Right'] = (x_new, y_new, obstacle1_new[0], obstacle1_new[1], obstacle1_new[2],
                                       obstacle2_new[0], obstacle2_new[1], obstacle2_new[2])

        # left
        if x > 0:
            x_new = x - 1
            y_new = y
            man = x_new, y_new
            if chek_collision(man, obstacle1_new, obstacle2_new):
                successors['Left'] = (x_new, y_new, obstacle1_new[0], obstacle1_new[1], obstacle1_new[2],
                                      obstacle2_new[0], obstacle2_new[1], obstacle2_new[2])

        # up
        if y < 5:
            x_new = x
            y_new = y + 1
            man = x_new, y_new
            if chek_collision(man, obstacle1_new, obstacle2_new):
                successors['Up'] = (x_new, y_new, obstacle1_new[0], obstacle1_new[1], obstacle1_new[2],
                                    obstacle2_new[0], obstacle2_new[1], obstacle2_new[2])

        # down3
        if y > 0:
            x_new = x
            y_new = y - 1
            man = x_new, y_new
            if chek_collision(man, obstacle1_new, obstacle2_new):
                successors['Down'] = (x_new, y_new, obstacle1_new[0], obstacle1_new[1], obstacle1_new[2],
                                      obstacle2_new[0], obstacle2_new[1], obstacle2_new[2])

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        g = self.goal
        return state[0] == g[0] and state[1] == state[1]

    def h(self, node):
        x = node.state[0]
        y = node.state[1]
        x1 = self.goal[0]  # pozicija na kukjickata
        y1 = self.goal[0]  # pozicija na kukjickata

        return abs(x - x1) + abs(y - y1)


if __name__ == '__main__':
    man_x = int(input())
    man_y = int(input())
    house_x = int(input())
    house_y = int(input())

    house = [house_x, house_y]

    explorer = Explorer((man_x, man_y, 2, 5, -1, 5, 0, 1), house)
    print(astar_search(explorer).solution())
