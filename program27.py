# Program 27: Sort the dataset
import pandas as pd

student_data = pd.read_csv("students.csv")

sorted_data = student_data.sort_values(by="Marks", ascending=False)
print(sorted_data)
