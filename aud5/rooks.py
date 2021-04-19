from constraint import *

if __name__ == '__main__':
    problem = Problem(RecursiveBacktrackingSolver())

    domain = []
    for i in range(0, 8):
        for j in range(0, 8):
            domain.append((i, j))
    # print(domain)

    rooks = range(1, 9)

    problem.addVariables(rooks, domain)

    for rook1 in rooks:
        for rook2 in rooks:
            if rook1 < rook2:
                problem.addConstraint(lambda r1, r2: r1[0] != r2[0] and r1[1] != r2[1], (rook1, rook2))
                # dali redicata od prviot top e razlicna so redicata od vtoriot top i dali
                # kolonata od prviot top e razlicna so kolonata od vtoriot top

    print(problem.getSolution())
