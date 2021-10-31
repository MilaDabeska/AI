from frameworks.uninformed import *


class Explorer(Problem):
    def __init__(self, initial, goal=None):
        super(Explorer, self).__init__(initial, goal)
        self.grid_size = (8, 6)  # gi pretstavuva granicite na tablata

    def successor(self, state):
        successors = dict()

        man_x = state[0]  # desno,levo
        man_y = state[1]  # gore,dole
        obstacle1 = list(state[2])
        obstacle2 = list(state[3])
        max_x = self.grid_size[0]
        max_y = self.grid_size[1]

        # 1 precka
        if obstacle1[2] == 0:  # up
            if obstacle1[1] == max_y - 1:  
                obstacle1[2] = 1
                obstacle1[1] -= 1  
            else:
                obstacle1[1] += 1  # nagore
        else:  # down
            if obstacle1[1] == 0:  # proveruvame dali preckata stignala do granicata na tablata
                obstacle1[2] = 0  
                obstacle1[1] += 1  
            else:
                obstacle1[1] -= 1  # nadolu

        # 2 precka
        if obstacle2[2] == 0:  # up
            if obstacle2[1] == max_y - 1:  # dali preckata e stignata do granicata na sistemot
                obstacle2[2] = 1
                obstacle2[1] -= 1  
            else:
                obstacle2[1] += 1  # nagore
        else:  # down
            if obstacle2[1] == 0:  # proveruvame dali preckata stignala do granicata na tablata
                obstacle2[2] = 0  
                obstacle2[1] += 1  
            else:
                obstacle2[1] -= 1  # nadolu

        # coveceto da izleze nadvor od granicite
        if man_x < max_x - 1 and (man_x + 1, man_y) not in [obstacle1, obstacle2]:
            successors['Right'] = (man_x + 1, man_y, tuple(obstacle1), tuple(obstacle2))

        if man_x > 0 and (man_x - 1, man_y) not in [obstacle1, obstacle2]:
            successors['Left'] = (man_x - 1, man_y, tuple(obstacle1), tuple(obstacle2))

        if man_y < max_y - 1 and (man_x, man_y + 1) not in [obstacle1, obstacle2]:
            successors['Up'] = (man_x, man_y + 1, tuple(obstacle1), tuple(obstacle2))

        if man_y > 0 and (man_x, man_y - 1) not in [obstacle1, obstacle2]:
            successors['Down'] = (man_x, man_y - 1, tuple(obstacle1), tuple(obstacle2))

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        position = (state[0], state[1])  # pozicija na coveceto
        return position == self.goal


if __name__ == '__main__':
    goal_state = (7, 4)
    initial_state = (0, 2)  
    obstacle_1 = (2, 5, 1)  
    obstacle_2 = (5, 0, 0)  

    explorer = Explorer((initial_state[0], initial_state[1], obstacle_1, obstacle_2), goal_state)
    result = breadth_first_graph_search(explorer)
    print(result.solution())
