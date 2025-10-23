import pandas as pd

from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score
from matplotlib import pyplot
import numpy
import graphviz  

DATASET_PATH = "../data/diabetes.csv"
diab = pd.read_csv(DATASET_PATH)

def filtrar_ceros(df):
    return df[(df["Insulin"] != 0) & (df["BloodPressure"] != 0) & (df["SkinThickness"] != 0)]

diab = filtrar_ceros(diab)

datos = diab.drop(columns=["Outcome"])
etiquetas = diab["Outcome"]

x_train, x_test, y_train, y_test = train_test_split(datos, etiquetas, test_size=0.2)
model_tree = tree.DecisionTreeClassifier()
model_tree = model_tree.fit(x_train, y_train)


y_pred = model_tree.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión del modelo: {accuracy * 100:.2f}%")


cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["No Diabetes", "Diabetes"])
disp.plot()   
pyplot.show()