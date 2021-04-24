from constraint import *


def check(row, column):
    if row in range(0, 3):
        if column in range(0, 3): return 1
        if column in range(3, 6): return 2
        if column in range(6, 9): return 3
    if row in range(3, 6):
        if column in range(0, 3): return 4
        if column in range(3, 6): return 5
        if column in range(6, 9): return 6
    if row in range(6, 9):
        if column in range(0, 3): return 7
        if column in range(3, 6): return 8
        if column in range(6, 9): return 9


if __name__ == '__main__':
    solver = input()
    if solver == 'BacktrackingSolver':
        problem = Problem(BacktrackingSolver())
    elif solver == 'RecursiveBacktrackingSolver':
        problem = Problem(RecursiveBacktrackingSolver())
    else:
        problem = Problem(MinConflictsSolver())

    variables = range(81)
    domain = range(1, 10)

    problem.addVariable(variables, domain)
    # ---Tuka dodadete gi ogranichuvanjata----------------
    for i in range(81):
        for j in range(81):
            if i < j:
                if i // 9 == j // 9:
                    problem.addConstraint(lambda s1, s2: s1 != s2, (i, j))
                if i % 9 == j % 9:
                    problem.addConstraint(lambda s1, s2: s1 != s2, (i, j))
            square_1 = check((i % 9), (i // 9))
            square_2 = check((j % 9), (j // 9))
            if square_1 == square_2:
                problem.addConstraint(lambda s1, s2: s1 != s2, (i, j))

# ----------------------------------------------------

print(problem.getSolution())
