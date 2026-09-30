# Program 20: Count missing values in each column
import pandas as pd

student_data = pd.read_csv("students.csv")

missing_values = student_data.isnull().sum()
print("Missing values in each column:")
print(missing_values)
