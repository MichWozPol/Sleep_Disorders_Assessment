import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
import matplotlib.pyplot as plt


COLUMN_NUMBER = '3'

def encode_columns(df):
    le = preprocessing.LabelEncoder()
    for column in df.columns:
        # print(df[column])
        le.fit(df[column])
        df[column] = le.transform(df[column])
    return df

def divide_into_X_Y(df):
    y = df[COLUMN_NUMBER]
    x = df.drop(columns=[COLUMN_NUMBER])
    return x,y

def train_test(x,y):
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1110)
    return X_train, X_test, y_train, y_test

def tree_classifier(X_train, X_test, y_train, y_test):
    clf = DecisionTreeClassifier(random_state=0)
    clf.fit(X_train, y_train)
    score_tree = clf.score(X_test, y_test)
    print(f'Confusion Matrix Tree: \n {metrics.confusion_matrix(y_test, clf.predict(X_test))}')
    plt.figure(figsize=(30, 30))
    plot_tree(clf, feature_names=df.columns, filled=True)
    plt.show()
    return score_tree

def naive_Bayes(X_train, X_test, y_train, y_test):
    gnb = GaussianNB()
    gnb.fit(X_train, y_train)
    scoreNB = gnb.score(X_test, y_test)
    print(f'Confusion Matrix Gaussian Naive Bayes: \n {metrics.confusion_matrix(y_test, gnb.predict(X_test))}')
    return scoreNB

def KNN_Neighbours(X_train, X_test, y_train, y_test):
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train, y_train)
    score_knn = knn.score(X_test, y_test)
    print(f'Confusion Matrix KNN Neighbours: \n {metrics.confusion_matrix(y_test, knn.predict(X_test))}')
    return score_knn


if __name__ == "__main__":
    path = r"C:\Users\micha\OneDrive\Documents\Programowanie\Python\Sleep_Disorders_Assessment\project_resources\prezentacja 3\with_quotes.csv"
    df = pd.read_csv(path, error_bad_lines=False)
    df = encode_columns(df)
    x,y = divide_into_X_Y(df)
    X_train, X_test, y_train, y_test = train_test(x,y)

    score_tree = tree_classifier(X_train, X_test, y_train, y_test)
    score_nb = naive_Bayes(X_train, X_test, y_train, y_test)
    score_knn = KNN_Neighbours(X_train, X_test, y_train, y_test)
    print(f'Tree: {score_tree}, NB: {score_nb}, KNN: {score_knn}')
