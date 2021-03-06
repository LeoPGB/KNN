#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

dataset = pd.read_csv('KNN.csv')
x = dataset.iloc[:, 2:4].values
y = dataset.iloc[:, 4].values

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.5, random_state=0)

sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.fit_transform(x_test)

classifier = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)
cm = confusion_matrix(y_pred, y_test)
print(cm)

# %%