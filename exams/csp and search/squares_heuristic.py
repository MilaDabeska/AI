from frameworks.utils import Problem
from frameworks.informed import *


class Squares(Problem):
    def __init__(self, initial, house):
        super().__init__(initial, house)

    def goal_test(self, state):
        return state == self.goal

    @staticmethod
    def check_valid(state):
        for x, y in state:
            if x < 0 or x > 4 or y < 0 or y > 4:
                return False
        return True

    def successor(self, state):
        succ = {}

        for i in range(5):  # 5 kvadratcinja
            # up
            square = state[i]  # tekovno kvadratce
            new_square = (square[0], square[1] + 1)  # x i y koordinati
            temp_squares = list(state)
            if self.check_valid(new_square):  # dali pozicijata na novoto kvadratce e validno
                temp_squares[i] = new_square
                succ[f'Pomesti kvadratche {i + 1} gore'] = tuple(temp_squares)

            # down
            square = state[i]  # tekovno kvadratce
            new_square = (square[0], square[1] - 1)  # x i y koordinati
            temp_squares = list(state)
            if self.check_valid(new_square):  # dali pozicijata na novoto kvadratce e validno
                temp_squares[i] = new_square
                succ[f'Pomesti kvadratche {i + 1} dole'] = tuple(temp_squares)

            # left
            square = state[i]  # tekovno kvadratce
            new_square = (square[0] - 1, square[1])  # x i y koordinati
            temp_squares = list(state)
            if self.check_valid(new_square):  # dali pozicijata na novoto kvadratce e validno
                temp_squares[i] = new_square
                succ[f'Pomesti kvadratche {i + 1} levo'] = tuple(temp_squares)

            # right
            square = state[i]  # tekovno kvadratce
            new_square = (square[0] + 1, square[1])  # x i y koordinati
            temp_squares = list(state)
            if self.check_valid(new_square):  # dali pozicijata na novoto kvadratce e validno
                temp_squares[i] = new_square
                succ[f'Pomesti kvadratche {i + 1} desno'] = tuple(temp_squares)

        return succ

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def h(self, node):
        state = node.state
        total_distance = 0
        for current_position, goal_position in zip(state, self.goal):
            distance = abs(current_position[0] - goal_position[0]) + abs(current_position[1] - goal_position[1])
            total_distance += distance
        return total_distance

    # def h(self, node):
    #     state = node.state
    #     goal = self.goal
    #     value = 0
    #     for x, y in zip(state, goal):
    #         if x != y:
    #             value += 1
    #     return value


if __name__ == '__main__':
    # ((x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5))
    initial_state = tuple()
    for _ in range(5):
        initial_state += (tuple(map(int, input().split(','))),)

    goal_state = ((0, 4), (1, 3), (2, 2), (3, 1), (4, 0))

    squares = Squares(initial_state, goal_state)
    print(astar_search(squares).solution())
