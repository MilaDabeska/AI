import csv
import math
from sklearn.naive_bayes import GaussianNB

if __name__ == '__main__':
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        data = list(csv_reader)[1:]
        data = [[int(data[i][j]) for j in range(0, len(data[i]))] for i in range(0, len(data))]  # vgnezden
        # print(data)

        training = data[0:math.ceil(0.8 * len(data))]
        test = data[math.ceil(0.8 * len(data)):]

        x = [training[i][:-1] for i in range(0, len(training))]
        y = [training[i][-1] for i in range(0, len(training))]

        clf = GaussianNB()
        clf.fit(x, y)
        # print(clf.predict_proba([test[0][:-1]]))

        # entry=[int(el) for el in input().split(' ')]
        # print(clf.predict_proba([entry]))

        accuracy = 0
        for row in test:
            predict = clf.predict([row[:-1]])
            if predict[0] == row[-1]:
                accuracy += 1

        print(accuracy / len(test))
