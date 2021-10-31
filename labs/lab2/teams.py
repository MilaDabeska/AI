from constraint import *


def keys(value, dictionary):
    for key, val in dictionary.items():
        if value == val: return key


if __name__ == '__main__':
    problem = Problem(RecursiveBacktrackingSolver())

    member_num = int(input())
    member_dict = {}
    member_dom = []
    members = [f'Participant {m + 1}' for m in range(5)]
    for _ in range(member_num):
        weight, name = input().split(' ')
        member_dict[name] = float(weight)
        member_dom.append(float(weight))

    leader_numb = int(input())
    leader_dict = {}
    leader_dom = []
    leaders = ['Leader']
    for _ in range(leader_numb):
        weight, name = input().split(' ')
        leader_dict[name] = float(weight)
        leader_dom.append(float(weight))

    problem.addVariables(leaders, leader_dom)
    problem.addVariables(members, member_dom)
    problem.addConstraint(AllDifferentConstraint(), members)
    problem.addConstraint(MaxSumConstraint(100))

    solutions = {}

    for s in problem.getSolutions():
        weight = 0
        for v in s.values():
            if v != weight:
                weight += v
        solutions[weight] = [v for v in s.values()]

    best = max(solutions)
    teams = solutions[best]
    best_leader = teams[-1]

    print(f'Total score: {round(best, 1)}')
    print(f'Team leader: {keys(best_leader, leader_dict)}')

    del teams[-1]
    teams.sort()
    for team in range(len(teams)):
        print(f'Participant {team + 1}: {keys(teams[team], member_dict)}')