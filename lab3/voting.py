from sklearn.tree import DecisionTreeClassifier
from collections import Counter

dataset = [[6.3, 2.3, 4.4, 1.3, 2],
           [6.4, 2.8, 5.6, 2.1, 0],
           [5.1, 3.3, 1.7, 0.5, 1],
           [5.1, 3.5, 1.4, 0.2, 1],
           [4.6, 3.1, 1.5, 0.2, 1],
           [5.8, 2.7, 5.1, 1.9, 0],
           [5.5, 3.5, 1.3, 0.2, 1],
           [5.7, 2.6, 3.5, 1.0, 2],
           [5.0, 3.5, 1.3, 0.3, 1],
           [6.3, 2.5, 5.0, 1.9, 0],
           [6.2, 2.2, 4.5, 1.5, 2],
           [5.0, 3.4, 1.6, 0.4, 1],
           [5.7, 4.4, 1.5, 0.4, 1],
           [4.9, 2.4, 3.3, 1.0, 2],
           [4.4, 2.9, 1.4, 0.2, 1],
           [5.5, 2.4, 3.7, 1.0, 2],
           [5.6, 2.5, 3.9, 1.1, 2],
           [5.6, 2.8, 4.9, 2.0, 0],
           [4.8, 3.4, 1.6, 0.2, 1],
           [5.6, 3.0, 4.5, 1.5, 2],
           [6.0, 3.0, 4.8, 1.8, 0],
           [6.3, 3.3, 4.7, 1.6, 2],
           [4.8, 3.0, 1.4, 0.1, 1],
           [7.9, 3.8, 6.4, 2.0, 0],
           [4.9, 3.0, 1.4, 0.2, 1],
           [4.3, 3.0, 1.1, 0.1, 1],
           [6.8, 3.2, 5.9, 2.3, 0],
           [5.6, 2.7, 4.2, 1.3, 2],
           [5.2, 4.1, 1.5, 0.1, 1],
           [6.2, 2.9, 4.3, 1.3, 2],
           [6.5, 2.8, 4.6, 1.5, 2],
           [5.4, 3.9, 1.3, 0.4, 1],
           [5.8, 2.6, 4.0, 1.2, 2],
           [5.4, 3.7, 1.5, 0.2, 1],
           [4.5, 2.3, 1.3, 0.3, 1],
           [6.3, 3.4, 5.6, 2.4, 0],
           [6.2, 3.4, 5.4, 2.3, 0],
           [5.7, 2.5, 5.0, 2.0, 0],
           [5.8, 2.7, 3.9, 1.2, 2],
           [6.4, 2.7, 5.3, 1.9, 0],
           [5.1, 3.8, 1.6, 0.2, 1],
           [6.3, 2.5, 4.9, 1.5, 2],
           [7.7, 2.8, 6.7, 2.0, 0],
           [5.1, 3.5, 1.4, 0.3, 1],
           [6.8, 2.8, 4.8, 1.4, 2],
           [6.1, 3.0, 4.6, 1.4, 2],
           [5.5, 4.2, 1.4, 0.2, 1],
           [5.0, 2.0, 3.5, 1.0, 2],
           [7.7, 3.0, 6.1, 2.3, 0],
           [5.1, 2.5, 3.0, 1.1, 2],
           [5.9, 3.0, 5.1, 1.8, 0],
           [7.2, 3.2, 6.0, 1.8, 0],
           [4.9, 3.1, 1.5, 0.2, 1],
           [5.7, 3.0, 4.2, 1.2, 2],
           [6.1, 2.9, 4.7, 1.4, 2],
           [5.0, 3.2, 1.2, 0.2, 1],
           [4.4, 3.2, 1.3, 0.2, 1],
           [6.7, 3.1, 5.6, 2.4, 0],
           [4.6, 3.6, 1.0, 0.2, 1],
           [5.1, 3.4, 1.5, 0.2, 1],
           [5.2, 2.7, 3.9, 1.4, 2],
           [6.4, 3.1, 5.5, 1.8, 0],
           [7.4, 2.8, 6.1, 1.9, 0],
           [4.9, 3.1, 1.5, 0.1, 1],
           [5.0, 3.5, 1.6, 0.6, 1],
           [6.7, 3.1, 4.7, 1.5, 2],
           [6.4, 3.2, 5.3, 2.3, 0],
           [6.3, 2.7, 4.9, 1.8, 0],
           [5.8, 4.0, 1.2, 0.2, 1],
           [6.9, 3.1, 5.4, 2.1, 0],
           [5.9, 3.2, 4.8, 1.8, 2],
           [6.6, 2.9, 4.6, 1.3, 2],
           [6.1, 2.8, 4.0, 1.3, 2],
           [7.7, 2.6, 6.9, 2.3, 0],
           [5.5, 2.6, 4.4, 1.2, 2],
           [6.3, 2.9, 5.6, 1.8, 0],
           [7.2, 3.0, 5.8, 1.6, 0],
           [6.5, 3.0, 5.8, 2.2, 0],
           [5.4, 3.9, 1.7, 0.4, 1],
           [6.5, 3.2, 5.1, 2.0, 0],
           [5.9, 3.0, 4.2, 1.5, 2],
           [5.1, 3.7, 1.5, 0.4, 1],
           [5.7, 2.8, 4.5, 1.3, 2],
           [5.4, 3.4, 1.5, 0.4, 1],
           [4.6, 3.4, 1.4, 0.3, 1],
           [4.9, 3.6, 1.4, 0.1, 1],
           [6.7, 2.5, 5.8, 1.8, 0],
           [5.0, 3.6, 1.4, 0.2, 1],
           [6.7, 3.3, 5.7, 2.5, 0],
           [4.4, 3.0, 1.3, 0.2, 1],
           [6.0, 2.2, 5.0, 1.5, 0],
           [6.0, 2.2, 4.0, 1.0, 2],
           [5.0, 3.4, 1.5, 0.2, 1],
           [5.7, 2.8, 4.1, 1.3, 2],
           [5.5, 2.4, 3.8, 1.1, 2],
           [5.1, 3.8, 1.9, 0.4, 1],
           [6.9, 3.1, 5.1, 2.3, 0],
           [5.6, 2.9, 3.6, 1.3, 2],
           [6.1, 2.8, 4.7, 1.2, 2],
           [5.5, 2.5, 4.0, 1.3, 2],
           [5.5, 2.3, 4.0, 1.3, 2],
           [6.0, 2.9, 4.5, 1.5, 2],
           [5.1, 3.8, 1.5, 0.3, 1],
           [5.7, 3.8, 1.7, 0.3, 1],
           [6.7, 3.3, 5.7, 2.1, 0],
           [4.8, 3.1, 1.6, 0.2, 1],
           [5.4, 3.0, 4.5, 1.5, 2],
           [6.5, 3.0, 5.2, 2.0, 0],
           [6.8, 3.0, 5.5, 2.1, 0],
           [7.6, 3.0, 6.6, 2.1, 0],
           [5.0, 3.0, 1.6, 0.2, 1],
           [6.7, 3.0, 5.0, 1.7, 2],
           [4.8, 3.4, 1.9, 0.2, 1],
           [5.8, 2.8, 5.1, 2.4, 0],
           [5.0, 2.3, 3.3, 1.0, 2],
           [4.8, 3.0, 1.4, 0.3, 1],
           [5.2, 3.5, 1.5, 0.2, 1],
           [6.1, 2.6, 5.6, 1.4, 0],
           [5.8, 2.7, 4.1, 1.0, 2],
           [6.9, 3.2, 5.7, 2.3, 0],
           [6.4, 2.9, 4.3, 1.3, 2],
           [7.3, 2.9, 6.3, 1.8, 0],
           [6.3, 2.8, 5.1, 1.5, 0],
           [6.2, 2.8, 4.8, 1.8, 0],
           [6.7, 3.1, 4.4, 1.4, 2],
           [6.0, 2.7, 5.1, 1.6, 2],
           [6.5, 3.0, 5.5, 1.8, 0],
           [6.1, 3.0, 4.9, 1.8, 0],
           [5.6, 3.0, 4.1, 1.3, 2],
           [4.7, 3.2, 1.6, 0.2, 1],
           [6.6, 3.0, 4.4, 1.4, 2]]


def count_vote(votes):
    count = {}
    for i in range(0, 3):
        count[i] = 0

    for v in votes.values():
        count[v] += 1

    return count


def provided_class(vote):
    c = Counter(vote.values())
    if c.most_common(1)[0][1] == 1:
        return 'unknown'
    return c.most_common(1)[0][0]


if __name__ == '__main__':
    first_set = dataset[0:int(0.3 * len(dataset))]  # првите 30%
    second_set = dataset[int(0.3 * len(dataset)):int(0.6 * len(dataset))]  # следните 30%
    third_set = dataset[int(0.6 * len(dataset)):]  # останатите 40%

    first_train_x = [t[:-1] for t in first_set]
    first_train_y = [t[-1] for t in first_set]
    second_train_x = [t[:-1] for t in second_set]
    second_train_y = [t[-1] for t in second_set]
    third_train_x = [t[:-1] for t in third_set]
    third_train_y = [t[-1] for t in third_set]

    classifier1 = DecisionTreeClassifier(criterion='entropy', random_state=0)
    classifier1.fit(first_train_x, first_train_y)
    classifier2 = DecisionTreeClassifier(criterion='entropy', random_state=0)
    classifier2.fit(second_train_x, second_train_y)
    classifier3 = DecisionTreeClassifier(criterion='entropy', random_state=0)
    classifier3.fit(third_train_x, third_train_y)

    n = input().split(', ')
    test = list(map(float, n[:-1])) + [int(n[-1])]

    votes = dict()
    for (i, j) in enumerate([classifier1, classifier2, classifier3]):
        votes[i] = j.predict([test[:-1]])[0]

    print(f'Glasovi: {count_vote(votes)}')
    print(f'Predvidena klasa: {provided_class(votes)}')
