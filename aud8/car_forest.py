import csv
from sklearn.preprocessing import OrdinalEncoder
import math
from sklearn.ensemble import RandomForestClassifier

if __name__ == '__main__':
    with open('cars.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        dataset = list(csv_reader)[1:]

    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])  # predavanje na site koloni osven klasata

    train_set = dataset[0:math.ceil(0.7 * len(dataset))]
    train_x = [t[:-1] for t in train_set]  # site karakteristiki osven klasata
    train_x = encoder.transform(train_x)  # transformacija vo celobrojna vrednost
    train_y = [t[-1] for t in train_set]  # klasata

    test_set = dataset[math.ceil(0.7 * len(dataset)):]
    test_x = [t[:-1] for t in test_set]
    test_x = encoder.transform(test_x)
    test_y = [t[-1] for t in test_set]

    classifier = RandomForestClassifier(n_estimators=150, criterion='entropy')
    classifier.fit(train_x, train_y)

    correct_samples = 0
    for x, y in zip(test_x, test_y):
        y_predicted = classifier.predict([x])[0]
        if y == y_predicted:
            correct_samples += 1

    print(f'Accuracy: {correct_samples / len(test_set)}')

    feature_importances = list(classifier.feature_importances_)
    most_important_feature = feature_importances.index(max(feature_importances))
    least_important_feature = feature_importances.index(min(feature_importances))

    print(f'Most important feature: {most_important_feature}')
    print(f'Least important feature: {least_important_feature}')
