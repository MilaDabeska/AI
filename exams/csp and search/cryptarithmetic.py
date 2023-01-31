from constraint import *


def check_valid(s, e, n, d, m, o, r, y):
    # s = 3 , e = 2 , n = 5 , d = 4 , send = 3254
    send = s * 1000 + e * 100 + n * 10 + d * 1
    more = m * 1000 + o * 100 + r * 10 + e * 1
    money = m * 10000 + o * 1000 + n * 100 + e * 10 + y * 1
    return send + more == money


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    variables = ["S", "E", "N", "D", "M", "O", "R", "Y"]  # domen
    for variable in variables:
        problem.addVariable(variable, Domain(set(range(10))))

    # ---Tuka dodadete gi ogranichuvanjata----------------

    problem.addConstraint(AllDifferentConstraint(), variables)  # sekoja vrednost treba da bide razlicna
    problem.addConstraint(check_valid,variables)

    # ----------------------------------------------------

    print(problem.getSolution())
