from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from aud.aud9.wine_neural import read_dataset, divide_sets

if __name__ == '__main__':
    dataset = read_dataset()
    train_set, valid_set, test_set = divide_sets(dataset)

    train_x = [x[:-1] for x in train_set]  # karakteristiki za train mnozestvoto
    train_y = [x[-1] for x in train_set]  # klasa
    valid_x = [x[:-1] for x in valid_set]
    valid_y = [x[-1] for x in valid_set]
    test_x = [x[:-1] for x in test_set]
    test_y = [x[-1] for x in test_set]

    scaler = StandardScaler()
    scaler.fit(train_x)

    scaler2 = MinMaxScaler()
    scaler2.fit(train_x)

    """
    Употребете ја истата поделба на податочните множества од претходната задача и 
    креирајте модел кој се покажал како најдобар од претходната задача.
    """
    classifier = MLPClassifier(10, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)
    classifier2 = MLPClassifier(10, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)
    classifier3 = MLPClassifier(10, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)

    classifier.fit(train_x, train_y)
    classifier2.fit(scaler.transform(train_x), train_y)  # gi transformirame i gi dobivame skaliranite vrednosti
    classifier3.fit(scaler2.transform(train_x), train_y)

    valid_acc1 = 0
    valid_predictions = classifier.predict(valid_x)
    for true, pred in zip(valid_y, valid_predictions):
        if true == pred:
            valid_acc1 += 1

    valid_acc1 = valid_acc1 / len(valid_y)

    print(f'Without normalization we have an accuracy with a validation set of {valid_acc1}')

    valid_acc2 = 0
    valid_predictions = classifier2.predict(scaler.transform(valid_x))
    for true, pred in zip(valid_y, valid_predictions):
        if true == pred:
            valid_acc2 += 1

    valid_acc2 = valid_acc2 / len(valid_y)

    print(f'With standard normalization we have an accuracy with a validation set of {valid_acc2}')

    valid_acc3 = 0
    valid_predictions = classifier3.predict(scaler2.transform(valid_x))
    for true, pred in zip(valid_y, valid_predictions):
        if true == pred:
            valid_acc3 += 1

    valid_acc2 = valid_acc3 / len(valid_y)

    print(f'With min-max scaling we have an accuracy with a validation set of {valid_acc3}')

    tp, fp, tn, fn = 0, 0, 0, 0
    predictions = classifier3.predict(scaler2.transform(test_x))
    for pred, true in zip(predictions, test_y):
        if true == 'good':
            if pred == true:
                tp += 1  # true positive
            else:
                fn += 1  # false negative
        else:
            if pred == true:
                tn += 1  # true negative
            else:
                fp += 1  # false positive

    acc = (tp + tn) / (tp + fp + tn + fn)
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)

    print(f'Evaluation:')
    print(f'Accuracy: {acc}')
    print(f'Precision: {precision}')
    print(f'Recall: {recall}')
