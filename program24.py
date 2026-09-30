# Program 24: Select rows and columns using loc[]
import pandas as pd

student_data = pd.read_csv("students.csv")

selected_data = student_data.loc[0:4, ["Name", "Course", "Marks"]]
print(selected_data)
