import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

iris_dataset = pd.read_csv("data/iris.csv")

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.scatterplot(
    data=iris_dataset,
    x='petal_length',
    y='petal_width',
    hue='species',
    palette='Set1',
    ax=axes[0] 
)
axes[0].set_title("Pétalos")

sns.scatterplot(
    data=iris_dataset,
    x='sepal_length',
    y='sepal_width',
    hue='species',
    palette='Set2',
    ax=axes[1] 
)
axes[1].set_title("Sépalos")

plt.tight_layout()
plt.show()