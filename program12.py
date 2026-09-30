# Program 12: Display the first five records
import pandas as pd

student_data = pd.read_csv("students.csv")
print(student_data.head())
