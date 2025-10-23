import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import tensorflow as tf
import numpy as np
import pandas as pd
import seaborn as sns

DATASETH_PATH = "../Heart_Attack.csv"
heart_data = pd.read_csv(DATASETH_PATH)