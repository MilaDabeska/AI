from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    n = int(input())
    # variables = ["A", "B", "C", "D", "E", "F"]
    # for variable in variables:
    #     problem.addVariable(variable, Domain(set(range(100))))
    variables = range(1, n + 1)
    domain = [(i, j) for i in range(n) for j in range(n)]

    problem.addVariables(variables, domain)

# ---Tuka dodadete gi ogranichuvanjata----------------
for i in variables:
    for j in variables:
        if i < j:
            problem.addConstraint(lambda q1, q2: q1[0] != q2[0] and q1[1] != q2[1] and
                                                 (abs(q1[0] - q2[0]) != abs(q1[1] - q2[1])), (i, j))

# ----------------------------------------------------

if n <= 6:
    print(len(problem.getSolution()))
else:
    print(problem.getSolution())
