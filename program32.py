# Program 32: Load a dataset from Scikit-learn
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()

iris_data = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

print(iris_data.head())
