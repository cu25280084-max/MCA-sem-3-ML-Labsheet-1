# Program 26: Filter records based on a condition
import pandas as pd

student_data = pd.read_csv("students.csv")

high_marks = student_data[student_data["Marks"] > 80]
print(high_marks)
