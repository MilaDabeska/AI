from sklearn.neural_network import MLPClassifier


def read_dataset():  # citanje linija po linija
    data = []
    with open('wine.csv') as file:
        _ = file.readline()
        while True:
            line = file.readline().strip()
            if line == '':
                break
            parts = line.split(';')  # karakteristiki za dadena linija
            data.append(list(map(float, parts[:-1])) + parts[-1:])

    return data


def divide_sets(dataset):  # podelba na podatocnoto mnozestvo
    bad_classes = [x for x in dataset if x[-1] == 'bad']  # klasata na posledna pozicija
    good_classes = [x for x in dataset if x[-1] == 'good']

    train_set = bad_classes[:int(len(bad_classes) * 0.7)] + good_classes[:int(len(good_classes) * 0.7)]
    valid_set = bad_classes[int(len(bad_classes) * 0.7):int(len(bad_classes) * 0.8)] + good_classes[int(len(good_classes) * 0.7):int(len(good_classes) * 0.8)]
    test_set = bad_classes[int(len(bad_classes) * 0.8):] + good_classes[int(len(good_classes) * 0.8):]

    return test_set, valid_set, train_set


if __name__ == '__main__':
    dataset = read_dataset()
    train_set, valid_set, test_set = divide_sets(dataset)

    train_x = [x[:-1] for x in train_set]  # karakteristiki za train mnozestvoto
    train_y = [x[-1] for x in train_set]  # klasa
    valid_x = [x[:-1] for x in valid_set]
    valid_y = [x[-1] for x in valid_set]
    test_x = [x[:-1] for x in test_set]
    test_y = [x[-1] for x in test_set]

    """
    во скриениот слој од можностите [5, 10, 100]
    Моделите се тренираат со рата на учење од 0.001, 500 епохи и 
    ReLU активациска функција на невроните од скриениот слој.
    """
    classifier = MLPClassifier(5, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)
    classifier2 = MLPClassifier(10, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)
    classifier3 = MLPClassifier(100, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)

    classifier.fit(train_x, train_y)
    classifier2.fit(train_x, train_y)
    classifier3.fit(train_x, train_y)

    """
    Моделот со најдобра точност со валидациското множество
    """
    final_classifier = None
    max_acc = 0
    for i, c in enumerate([classifier, classifier2, classifier3]):
        valid_predictions = c.predict(valid_x)
        valid_acc = 0
        for true, pred in zip(valid_y,
                              valid_predictions):  # dali imame poklopuvanje na vistinskata klasa i taa shto e predvidena
            if true == pred:
                valid_acc += 1

        valid_acc = valid_acc / len(valid_y)

        print(f'The classifier {i} has accuracy with the validation set {valid_acc}')

        if valid_acc > max_acc:
            max_acc = valid_acc
            final_classifier = c

    accuracy = 0
    predictions = final_classifier.predict(test_x)

    for true, pred in zip(test_y, predictions):
        if true == pred:
            accuracy += 1

    accuracy = accuracy / len(test_y)
    print(f'The accuracy with the test set is {accuracy}')
