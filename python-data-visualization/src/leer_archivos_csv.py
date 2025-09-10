import pandas as pd
import matplotlib.pyplot as plt
#buscar archivos en kaggle.com
DATASET_PATH = "data/iris.csv"
iris_dataset = pd.read_csv(DATASET_PATH)
#print(iris_dataset)
iris_dataset.hist()
plt.show()

test_iris_list = []

for species in iris_dataset['species'].unique():
    sample = iris_dataset[iris_dataset['species'] == species].sample(frac=0.3)
    test_iris_list.append(sample)

# concatenar todos los subconjuntos
test_iris = pd.concat(test_iris_list)
train_iris = iris_dataset[~iris_dataset.index.isin(test_iris.index)]

setosa = train_iris[train_iris["species"] == "setosa"]
versicolor = train_iris[train_iris["species"] == "versicolor"]
virginica = train_iris[train_iris["species"] == "virginica"]

"""
def ininterval (value, mean, min_val, max_val): 
    print(value, mean, min_val, max_val)
    dif = max_val - min_val
    if mean
"""

#print(setosa.agg(['sum', 'max', 'count']))
#print(versicolor.agg(['sum', 'max', 'count']))
#print(virginica.agg(['sum', 'max', 'count']))

"""
print('setosa  \n', setosa)
print('versicolor  \n', versicolor) 
print('virginica  \n', virginica)   
"""
#print('test iris  \n', test_iris)
#print('train iris  \n', train_iris)
#iris_dataset.plot()
#plt.show()
#iris_dataset.agg(['sum', 'max', 'count'])

"""
setosa = iris_dataset[iris_dataset["variety"] == "Setosa"]
versicolor = iris_dataset[iris_dataset["variety"] == "Versicolor"]
virginica = iris_dataset[iris_dataset["variety"] == "Virginica"]
"""