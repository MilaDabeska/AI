import random

random.seed(0)


class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y


class Game:

    def __init__(self, matrix):
        self.matrix = matrix

    def num_dots(self):
        result = 0
        for i in range(m):
            for j in range(n):
                if self.matrix[i][j] == '.':
                    result += 1
        return result


class Pacman:
    def __init__(self, p, g):
        self.player = p
        self.game = g

    def play_game(self):
        self.game.matrix[0][0] = '#'
        num_dots = self.game.num_dots()

        if num_dots == 0:
            print('Nothing to do here')

        while num_dots != 0:
            wanted = []
            normal = []
            wanted_position = 0
            normal_position = 0

            if self.player.x_position > 0:
                if self.game.matrix[self.player.x_position - 1][self.player.y_position] == '.':
                    wanted_position += 1
                    wanted.append(f"[{self.player.x_position - 1}, {self.player.y_position}]")
                else:
                    normal_position += 1
                    normal.append(f"[{self.player.x_position - 1}, {self.player.y_position}]")

            if self.player.y_position > 0:
                if self.game.matrix[self.player.x_position][self.player.y_position - 1] == '.':
                    wanted_position += 1
                    wanted.append(f"[{self.player.x_position}, {self.player.y_position - 1}]")
                else:
                    normal_position += 1
                    normal.append(f"[{self.player.x_position}, {self.player.y_position - 1}]")

            if self.player.x_position < m - 1:
                if self.game.matrix[self.player.x_position + 1][self.player.y_position] == '.':
                    wanted_position += 1
                    wanted.append(f"[{self.player.x_position + 1}, {self.player.y_position}]")
                else:
                    normal_position += 1
                    normal.append(f"[{self.player.x_position + 1}, {self.player.y_position}]")

            if self.player.y_position < n - 1:
                if self.game.matrix[self.player.x_position][self.player.y_position + 1] == '.':
                    wanted_position += 1
                    wanted.append(f"[{self.player.x_position}, {self.player.y_position + 1}]")
                else:
                    normal_position += 1
                    normal.append(f"[{self.player.x_position}, {self.player.y_position + 1}]")

            if wanted_position != 0:
                idx = random.randint(0, wanted_position - 1)
                parts = list(wanted[idx])
                self.player.move(int(parts[1]), int(parts[4]))
                print(wanted[idx])
                self.game.matrix[int(parts[1])][int(parts[4])] = "#"
                num_dots = num_dots - 1
            else:
                idx = random.randint(0, normal_position - 1)
                parts = list(normal[idx])
                self.player.move(int(parts[1]), int(parts[4]))
                print(normal[idx])


if __name__ == '__main__':
    m = int(input())
    n = int(input())

    matrix = []
    for i in range(0, m):
        matrix2 = [element for element in list(input())]
        matrix.append(matrix2)

    player = Player(0, 0)
    game = Game(matrix)
    pacman = Pacman(player, game)
    pacman.play_game()
