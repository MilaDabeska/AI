from constraint import *


def keys(value, dictionary):
    for key, val in dictionary.items():
        if value == val: return key


if __name__ == '__main__':
    problem = Problem(RecursiveBacktrackingSolver())

    member_number = int(input())
    member_dict = {}
    member_domain = []
    members = [f'Participant {m + 1}' for m in range(5)]
    for _ in range(member_number):
        weight, name = input().split(' ')
        member_dict[name] = float(weight)
        member_domain.append(float(weight))

    leader_number = int(input())
    leader_dict = {}
    leader_domain = []
    leaders = ['Leader']
    for _ in range(leader_number):
        weight, name = input().split(' ')
        leader_dict[name] = float(weight)
        leader_domain.append(float(weight))

    problem.addVariables(leaders, leader_domain)
    problem.addVariables(members, member_domain)
    problem.addConstraint(AllDifferentConstraint(), members)
    problem.addConstraint(MaxSumConstraint(100))

    solutions = {}

    for solution in problem.getSolutions():
        weight = 0
        for value in solution.values():
            if value != weight:
                weight += value
        solutions[weight] = [value for value in solution.values()]

    best = max(solutions)
    team = solutions[best]
    best_leader = team[-1]

    print(f'Total score: {round(best, 1)}')
    print(f'Team leader: {keys(best_leader, leader_dict)}')

    del team[-1]
    team.sort()
    for t in range(len(team)):
        print(f'Participant {t + 1}: {keys(team[t], member_dict)}')