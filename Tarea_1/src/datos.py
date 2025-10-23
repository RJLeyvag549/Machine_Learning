import pandas as pd
import matplotlib.pyplot as plt 

DATASET_PATH = "../data/diabetes.csv"
diab_dataset = pd.read_csv(DATASET_PATH)

columna = "Insulin" 
#Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome
#BMI entre 29 y 36 con diabetes, 22 y 28 sin diabetes
#Insulin, BloodPressure, SkinThickness
# Filtrar por Outcome
sin_diabetes = diab_dataset[diab_dataset["Outcome"] == 0][columna]
con_diabetes = diab_dataset[diab_dataset["Outcome"] == 1][columna]
""""
plt.hist(sin_diabetes, bins=20, alpha=0.7, label="Sin Diabetes")
plt.hist(con_diabetes, bins=20, alpha=0.7, label="Con Diabetes")
plt.xlabel(columna)
plt.ylabel("Frecuencia")
plt.title(f"Histograma de {columna} por Outcome")
plt.legend()
plt.show()
"""
def frecuencia_insulin(df):
    frecuencias = df["DiabetesPedigreeFunction"].value_counts().sort_values(ascending=False)
    print(frecuencias)

# Ejemplo de uso:
frecuencia_insulin(diab_dataset)