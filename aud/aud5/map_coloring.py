from constraint import *

if __name__ == '__main__':
    problem = Problem(RecursiveBacktrackingSolver()) #tipovi na solvers

    problem.addVariables(['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T'], ['red', 'green', 'blue'])

    problem.addConstraint(lambda a, b: a != b, ('WA', 'NT'))
    problem.addConstraint(lambda a, b: a != b, ('WA', 'SA'))
    problem.addConstraint(lambda a, b: a != b, ("SA", "NT"))
    problem.addConstraint(lambda a, b: a != b, ('SA', 'NSW'))
    problem.addConstraint(lambda a, b: a != b, ('SA', 'Q'))
    problem.addConstraint(lambda a, b: a != b, ('SA', 'V'))
    problem.addConstraint(lambda a, b: a != b, ('NT', 'Q'))
    problem.addConstraint(lambda a, b: a != b, ('Q', 'NSW'))
    problem.addConstraint(lambda a, b: a != b, ('NSW', 'V'))

    solutions=problem.getSolutions()

    print(solutions[0]['WA'])

    print(problem.getSolution())
    print(problem.getSolutions())
    print(len(problem.getSolution())) #kolku reshenija imame
