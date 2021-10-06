from django.http import HttpResponse
from django.shortcuts import render


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

def index(request):
    #return HttpResponse('Hemlo!!')
    return render(request, 'index.html',)

def pyt(request):
    diabetes_dataset = pd.read_csv('static/diabetes_prediction/diabetes.csv')

    X = diabetes_dataset.drop(columns='Outcome', axis=1)

    scaler = StandardScaler()
    scaler.fit(X)
    standardized_data = scaler.transform(X)

    X = standardized_data
    Y = diabetes_dataset['Outcome']

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, stratify=Y, random_state=2)

    classifier = svm.SVC(kernel='linear')
    classifier.fit(X_train, Y_train)

    X_train_prediction = classifier.predict(X_train)
    training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

    X_test_prediction = classifier.predict(X_test)
    test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

    input_data = (5, 166, 72, 19, 175, 25.8, 0.587, 51)

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    # standardize the input data
    std_data = scaler.transform(input_data_reshaped)
    print(std_data)

    prediction = classifier.predict(std_data)
    print(prediction)

    if (prediction[0] == 0):
        return HttpResponse('The person is not diabetic')
    else:
        return HttpResponse('The person is diabetic')