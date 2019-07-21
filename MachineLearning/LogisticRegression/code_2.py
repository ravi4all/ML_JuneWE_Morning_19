import math
import random
import csv

def loadDataset(path):
    data = []
    with open(path) as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

def str_to_float(dataset):
    for i in range(len(dataset)):
        for j in range(len(dataset[i])):
            dataset[i][j] = float(dataset[i][j])

def minMax(dataset):
    data = []
    for i in range(len(dataset[0])):
        col = [row[i] for row in dataset]
        minVal = min(col)
        maxVal = max(col)
        data.append([minVal, maxVal])
    return data

def normalization(dataset, minMaxValues):
#    n = x - min(x) / max(x) - min(x)
    for i in range(len(dataset)):
        for j in range(len(dataset[i])):
            numer = dataset[i][j] - minMaxValues[j][0]
            denom = minMaxValues[j][1] - minMaxValues[j][0]
            dataset[i][j] = numer/denom

def crossValidation(dataset, k=5):
    dataset_copy = list(dataset)
    folds = []
    fold_size = len(dataset) // k
    for i in range(k):
        fold = []
        while len(fold) < fold_size:
            index = random.randrange(len(dataset_copy))
            fold.append(dataset_copy.pop(index))
        folds.append(fold)
    return folds

def predict(row, coef):
    x = coef[0]
    for i in range(len(row) - 1):
        x += coef[i+1] * row[i]
    return 1 / (1 + math.exp(-x))

def accuracy_score(pred,actual):
    count = 0
    for i in range(len(actual)):
        if actual[i] == pred[i]:
            count += 1
    return count / len(predict) * 100

def sgd_logistic(dataset, alpha, epochs):
    coef = [0] * len(dataset[0])
    for epoch in range(epochs):
        for row in dataset:
            y_pred = predict(row, coef)
            loss = y_pred - row[-1]
            coef[0] = coef[0] - alpha * loss
            for j in range(len(row) - 1):
                coef[j+1] = coef[j+1] - alpha * loss * row[j]
    return coef
    

def logisticRegression():
    pass

def evaluateAlgorithm():
    pass

filename = 'data.csv'
dataset = loadDataset(filename)
str_to_float(dataset)
minMaxValues = minMax(dataset)
normalization(dataset, minMaxValues)
#folds = crossValidation(dataset)


