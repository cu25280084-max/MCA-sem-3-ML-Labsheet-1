# Program 14: Find total number of rows and columns
import pandas as pd

student_data = pd.read_csv("students.csv")
rows, columns = student_data.shape

print("Number of rows:", rows)
print("Number of columns:", columns)
