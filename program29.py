# Program 29: Delete an existing column
import pandas as pd

student_data = pd.read_csv("students.csv")

student_data.drop("Age", axis=1, inplace=True)
print(student_data.head())
