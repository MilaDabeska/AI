import csv
from sklearn.preprocessing import OrdinalEncoder
import math
from sklearn.tree import DecisionTreeClassifier

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

    classifier = DecisionTreeClassifier(criterion='entropy')
    classifier.fit(train_x, train_y)

    print(f'Depth: {classifier.get_depth()}')
    print(f'Leaves: {classifier.get_n_leaves()}')

    correct_samples = 0
    for x, y in zip(test_x, test_y):
        y_predicted = classifier.predict([x])[0]
        if y == y_predicted:
            correct_samples += 1

    print(f'Accuracy: {correct_samples / len(test_set)}')

    feature_importances = list(classifier.feature_importances_)  # vaznost na karakteristiki
    print(f'Feature importances: {feature_importances}')

    most_important_feature = feature_importances.index(
        max(feature_importances))  # najvaznata karakteristika,najvisokata vrednost za vaznost
    print(f'Most important feature: {most_important_feature}')

    least_important_feature = feature_importances.index(
        min(feature_importances))  # najmalku vaznata karakteristika,najniskata vrednost za vaznost
    print(f'Least important feature: {least_important_feature}')

    # otstranuvanje na kolona
    train_x_2 = list()
    for t in train_x:
        sample = [t[i] for i in range(0, len(t)) if i != most_important_feature]
        train_x_2.append(sample)

    test_x_2 = list()
    for t in test_x:
        sample = [t[i] for i in range(0, len(t)) if i != most_important_feature]
        test_x_2.append(sample)

    train_x_3 = list()
    for t in train_x:
        sample = [t[i] for i in range(0, len(t)) if i != least_important_feature]
        train_x_3.append(sample)

    test_x_3 = list()
    for t in test_x:
        sample = [t[i] for i in range(0, len(t)) if i != least_important_feature]
        test_x_3.append(sample)

    classifier2 = DecisionTreeClassifier(criterion='entropy')
    classifier3 = DecisionTreeClassifier(criterion='entropy')

    classifier2.fit(train_x_2, train_y)
    classifier3.fit(train_x_3, train_y)

    print(f'Depth (removed most important feature): {classifier2.get_depth()}')
    print(f'Leaves (removed most important feature): {classifier2.get_n_leaves()}')

    print(f'Depth (removed least important feature): {classifier3.get_depth()}')
    print(f'Leaves (removed least important feature): {classifier3.get_n_leaves()}')

    # tocnost
    correct_samples2 = 0
    for x, y in zip(test_x_2, test_y):
        y_predicted = classifier2.predict([x])[0]
        if y == y_predicted:
            correct_samples2 += 1

    correct_samples3 = 0
    for x, y in zip(test_x_3, test_y):
        y_predicted = classifier3.predict([x])[0]
        if y == y_predicted:
            correct_samples3 += 1

    print(f'Accuracy (removed most important feature): {correct_samples2 / len(test_set)}')
    print(f'Accuracy (removed least important feature): {correct_samples3 / len(test_set)}')
