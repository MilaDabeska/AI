from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # ---Dadeni se promenlivite, dodadete gi domenite-----
    problem.addVariable("Marija_prisustvo", [0, 1])
    problem.addVariable("Simona_prisustvo", [0, 1])
    problem.addVariable("Petar_prisustvo", [0, 1])
    problem.addVariable("vreme_sostanok", range(12, 21))
    # ----------------------------------------------------

    simona = tuple(range(13, 15)) + tuple(range(16, 17)) + tuple(range(19, 20))
    marija = tuple(range(14, 16)) + tuple(range(18, 19))
    petar = tuple(range(12, 14)) + tuple(range(16, 21))

    # ---Tuka dodadete gi ogranichuvanjata----------------

    problem.addConstraint(InSetConstraint({1}), ["Simona_prisustvo"])  # Симона како менаџер мора да присуствува на состанокот
    problem.addConstraint(SomeInSetConstraint({1}), ["Marija_prisustvo", "Petar_prisustvo"])  # со најмалку уште една личност
    problem.addConstraint(lambda i, j: i == 1 and j in simona, ["Simona_prisustvo", "vreme_sostanok"])
    problem.addConstraint(lambda i, j: i == 0 if j in petar else i == 1, ["Petar_prisustvo", "vreme_sostanok"])
    problem.addConstraint(lambda i, j: i == 1 if j in marija else i == 1, ["Marija_prisustvo", "Simona_prisustvo"])

    # ----------------------------------------------------

    [print(solution) for solution in problem.getSolutions()]