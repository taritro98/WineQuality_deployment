import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import pickle


df = pd.read_csv('winequality-red.csv')

X = df.drop('quality',axis=1)
y = df['quality']  

x_train, x_test, y_train, y_test = train_test_split(X, y, random_state=42)

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.fit_transform(x_test)


clf = RandomForestClassifier()
clf.fit(x_train, y_train)

pickle.dump(clf, open('model.pkl','wb'))



