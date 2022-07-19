from constraint import *


def meeting(marija, petar, time):
    if marija == 1 and petar == 0 and time == 14: return True
    if marija == 0 and petar == 1 and time == 19: return True
    if marija == 0 and petar == 1 and time == 16: return True
    if marija == 0 and petar == 1 and time == 13:
        return True
    else:
        return None


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    times = range(12, 21)

    # ---Dadeni se promenlivite, dodadete gi domenite-----
    problem.addVariable("Simona_prisustvo", [1])
    problem.addVariable("Marija_prisustvo", [0, 1])
    problem.addVariable("Petar_prisustvo", [0, 1])
    problem.addVariable("vreme_sostanok", times)
    # problem.addVariable("Marija_prisustvo", [0, 1])
    # problem.addVariable("Simona_prisustvo", [0, 1])
    # problem.addVariable("Petar_prisustvo", [0, 1])
    # problem.addVariable("vreme_sostanok", range(12, 21))
    # ----------------------------------------------------

    # simona = tuple(range(13, 15)) + tuple(range(16, 17)) + tuple(range(19, 20))
    # marija = tuple(range(14, 16)) + tuple(range(18, 19))
    # petar = tuple(range(12, 14)) + tuple(range(16, 21))

    # ---Tuka dodadete gi ogranichuvanjata----------------

    # problem.addConstraint(InSetConstraint({1}), ["Simona_prisustvo"])  # Симона како менаџер мора да присуствува на состанокот
    # problem.addConstraint(SomeInSetConstraint({1}), ["Marija_prisustvo", "Petar_prisustvo"])  # со најмалку уште една личност
    # problem.addConstraint(lambda i, j: i == 1 and j in simona, ["Simona_prisustvo", "vreme_sostanok"])
    # problem.addConstraint(lambda i, j: i == 0 if j in petar else i == 1, ["Petar_prisustvo", "vreme_sostanok"])
    # problem.addConstraint(lambda i, j: i == 1 if j in marija else i == 1, ["Marija_prisustvo", "Simona_prisustvo"])
    problem.addConstraint(meeting, ["Marija_prisustvo", "Petar_prisustvo", "vreme_sostanok"])
    # ----------------------------------------------------

    [print(solution) for solution in problem.getSolutions()]
