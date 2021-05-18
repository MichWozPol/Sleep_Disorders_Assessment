import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
import matplotlib.pyplot as plt

path = r"D:\Dokumenty\Studia\SEM6\HIED\votes_weka_80_80.csv"
df = pd.read_csv(path, error_bad_lines=False)

le = preprocessing.LabelEncoder()
for column in df.columns:
    # print(df[column])
    le.fit(df[column])
    df[column] = le.transform(df[column])

# print(le.inverse_transform(df['6']))
y = df['30']

x = df.drop(columns=['30'])

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=10)

clf = DecisionTreeClassifier(random_state=0)

clf.fit(X_train, y_train)

score = clf.score(X_test, y_test)

gnb = GaussianNB()

gnb.fit(X_train, y_train)

scoreNB = gnb.score(X_test, y_test)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
score_knn = knn.score(X_test, y_test)

print(f'Tree: {score}, NB: {scoreNB}, KNN: {score_knn}')
print(f'Confusion Matrix Tree: \n {metrics.confusion_matrix(y_test, clf.predict(X_test))}')

plt.figure(figsize=(30, 30))
plot_tree(clf)
plt.show()
