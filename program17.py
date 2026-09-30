# Program 17: Generate descriptive statistics
import pandas as pd

student_data = pd.read_csv("students.csv")
print(student_data.describe())
