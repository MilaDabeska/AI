from constraint import *

if __name__ == '__main__':
    n=int(input())
    problem = Problem(BacktrackingSolver())
    variables = ["A", "B", "C", "D", "E", "F"]
    for variable in variables:
        problem.addVariable(variable, Domain(set(range(100))))

    # ---Tuka dodadete gi ogranichuvanjata----------------

    for queen1 in variables:
        for queen2 in variables:
            if queen1 < queen2:
                problem.addConstraint(
                    lambda q1, q2: q1[0] != q2[0] and q1[1] != q2[1] and abs(q1[0] - q2[0]) != abs(q1[1] - q2[1]),
                    (queen1, queen2))

    # ----------------------------------------------------

    if variables <= 6:
        print(len(problem.getSolution()))
    else:
        print(problem.getSolution())
