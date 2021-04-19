from constraint import *

if __name__ == '__main__':
    problem = Problem()

    variables = range(0, 16)  # promenlivi od 0 do 16
    domain = range(1, 17)
    problem.addVariables(variables, domain)
    problem.addConstraint(AllDifferentConstraint(), variables)

    for row in range(0, 4):
        """
        0 1 2 3
        4 5 6 7
        """
        problem.addConstraint(ExactSumConstraint(34), [row * 4 + i for i in range(0, 4)])
        problem.addConstraint(ExactSumConstraint(34), [row * 4 + i for i in range(0, 4)])
    # 0*4 = 0 -> 0,1,2,3
    # 1*4 = 4 + 0 = 4 -> 4,5,6,7

    for column in range(0, 4):
        """
        0 1 2 3
        4 5 6 7
        """
        problem.addConstraint(ExactSumConstraint(34), [column + 4 * i for i in range(0, 4)])  # 0,4,8,12 ; 1,5,9,13...

    problem.addConstraint(ExactSumConstraint(34), range(0, 16, 5))  # [0,5,10,15]
    problem.addConstraint(ExactSumConstraint(34), range(3, 13, 3))  # [3,6,9,12]

    print(problem.getSolution())
