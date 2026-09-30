# Program 25: Select rows and columns using iloc[]
import pandas as pd

student_data = pd.read_csv("students.csv")

selected_data = student_data.iloc[0:5, 0:3]
print(selected_data)
