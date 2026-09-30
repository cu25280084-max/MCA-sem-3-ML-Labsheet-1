# Program 30: Remove duplicate records
import pandas as pd

student_data = pd.read_csv("students.csv")

print("Rows before removing duplicates:", len(student_data))

student_data.drop_duplicates(inplace=True)

print("Rows after removing duplicates:", len(student_data))
