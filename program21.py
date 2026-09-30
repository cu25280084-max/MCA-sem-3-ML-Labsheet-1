# Program 21: Display unique values in a selected column
import pandas as pd

student_data = pd.read_csv("students.csv")

print("Unique cities:")
print(student_data["City"].unique())
