# Program 16: Check data types of all columns
import pandas as pd

student_data = pd.read_csv("students.csv")
print(student_data.dtypes)
