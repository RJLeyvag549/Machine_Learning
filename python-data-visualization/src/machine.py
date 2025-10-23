from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score
from matplotlib import pyplot
import numpy
import graphviz  

iris = load_iris()
datos, etiquetas = iris.data, iris.target

x_train, x_test, y_train, y_test = train_test_split(datos, etiquetas, test_size=0.3)

model_tree = tree.DecisionTreeClassifier()
model_tree = model_tree.fit(x_train, y_train)

y_pred = model_tree.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión del modelo: {accuracy * 100:.2f}%")

cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=iris.target_names)
disp.plot()
pyplot.show()

#Visualizar el árbol con graphviz
dot_data = tree.export_graphviz(
    model_tree, 
    out_file=None, 
    feature_names=iris.feature_names, 
    class_names=iris.target_names, 
    filled=True, 
    rounded=True, 
    special_characters=True
)
graph = graphviz.Source(dot_data)
graph.render("arbol_decision_iris", view=True) 