# Program 15: Display names of all columns
import pandas as pd

student_data = pd.read_csv("students.csv")
print("Column names:")
print(student_data.columns)
