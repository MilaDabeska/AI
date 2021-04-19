from searching_framework.utils import Problem
from searching_framework.informed import *


class GraphExplorer(Problem):
    def __init__(self, initial, goal=None):
        super(GraphExplorer, self).__init__(initial, goal)

    def successor(self, state):
        successors = dict()

        player = state[0]
        links = state[2]

        # Up
        if player - 4 >= 1 and (player - 4, player) in links or (player, player - 4) in links:
            stars = tuple([x for x in state[1] if x != player - 4])
            new_links = [x for x in links if x != (player - 4, player) and (player, player - 4)]
            successors['Up'] = player - 4, stars, new_links

        # Down
        if player + 4 <= 16 and (player + 4, player) in links or (player, player + 4) in links:
            stars = tuple([x for x in state[1] if x != player + 4])
            new_links = [x for x in links if x != (player + 4, player) and (player, player + 4)]
            successors['Down'] = player + 4, stars, new_links

        # Left
        if player % 4 != 1 and (player - 1, player) in links or (player, player - 1) in links:
            stars = tuple([x for x in state[1] if x != player - 1])
            new_links = [x for x in links if x != (player - 1, player) and (player, player - 1)]
            successors['Left'] = player - 1, stars, new_links

        # Right
        if player % 4 != 0 and (player + 1, player) in links or (player, player + 1) in links:
            stars = tuple([x for x in state[1] if x != player + 1])
            new_links = [x for x in links if x != (player + 1, player) and (player, player + 1)]
            successors['Right'] = player + 1, stars, new_links

        # UpLeft
        if player % 4 != 1 and player - 4 >= 1 and (player + 5, player) in links or (player, player + 5) in links:
            stars = tuple([x for x in state[1] if x != player + 5])
            new_links = [x for x in links if x != (player + 5, player) and (player, player + 5)]
            successors['UpLeft'] = player + 5, stars, new_links

        # DownRight
        if player % 4 != 0 and player + 4 <= 16 and (player - 5, player) in links or (player, player - 5) in links:
            stars = tuple([x for x in state[1] if x != player - 5])
            new_links = [x for x in links if x != (player - 5, player) and (player, player - 5)]
            successors['DownRight'] = player - 5, stars, new_links

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[1]) == 0

    @staticmethod
    def euclidean(point1, point2):
        return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 1 / 2


points = []


def h(self, node):
    min_score = 1000000000
    for star in node.state[1]:
        distance = self.euclidean(points[star], points[node.state[0]])
        if distance < min_score:
            min_score = distance
    return min_score


if __name__ == '__main__':
    player_position = int(input())
    star1 = int(input())
    star2 = int(input())
    initial_state = (
        player_position, (star1, star2), ((1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12), (13, 14), (15, 16),
                                          (1, 5), (2, 6), (3, 7), (4, 8), (6, 10), (7, 11), (9, 13), (18, 14),
                                          (11, 15), (12, 16), (6, 11)))

    graph = GraphExplorer((player_position, star1, star2), initial_state)
    print(astar_search(graph).solution())
