import csv
from sklearn.preprocessing import OrdinalEncoder
from sklearn.naive_bayes import CategoricalNB
import math

if __name__ == '__main__':
    with open('cars.csv') as csv_file:
        # csv_file=open('cars.csv')
        csv_reader = csv.reader(csv_file, delimiter=';')  # odvoeno so zapirka

        data = list(csv_reader)[1:]  # otstranuvanje na prvata redica
        # print(data)

        encoder = OrdinalEncoder()
        # encoder.fit(data)  # prakjanje
        encoder.fit([data[i][:-1] for i in range(0, len(data))])
        # data = encoder.transform(data)  # transformiranje vo numericki
        # print(data)

        trening = data[0:math.ceil(0.7 * len(data))]  # math.ceil -> zaokrruzuvanje
        test = data[math.ceil(0.7 * len(data)):]

        X = [trening[i][:-1] for i in range(0, len(trening))]  # atributi,bez posledna kolona
        X = encoder.transform(X)
        Y = [trening[i][-1] for i in range(0, len(trening))]  # klasna labela,samo poslednata kolona

        clf = CategoricalNB()
        clf.fit(X, Y)

        # print(clf.predict_proba([test[0][0:-1]]))

        #tocnost
        test_x = encoder.transform([test[i][:-1] for i in range(0, len(test))])
        accuracy = 0
        # for row in test:
        for i in range(0, len(test)):
            # predict = clf.predict([row[:-1]])
            predict = clf.predict([test_x[i]])
            # if predict[0] == row[-1]:
            if predict[0] == test[i][-1]:
                accuracy += 1

        print(accuracy / len(test))

        entry = [elem for elem in input().split(' ')]
        entry = encoder.transform([entry])
        print(clf.predict(entry))

        # for row in csv_reader: #iterator
        #     print(row)

        # csv_file.close()
