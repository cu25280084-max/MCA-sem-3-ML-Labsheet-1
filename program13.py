# Program 13: Display the last five records
import pandas as pd

student_data = pd.read_csv("students.csv")
print(student_data.tail())
