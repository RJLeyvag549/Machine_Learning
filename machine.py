from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from matplotlib import pyplot
import numpy
import graphviz  

iris = load_iris()
datos, etiquetas = iris.data, iris.target

#print(iris.DESCR)

x_train, x_test, y_train, y_test = train_test_split(datos, etiquetas, test_size=0.3)

model_tree = tree.DecisionTreeClassifier()
model_tree = model_tree.fit(x_train, y_train)

