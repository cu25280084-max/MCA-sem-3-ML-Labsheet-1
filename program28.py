# Program 28: Add a new column
import pandas as pd

student_data = pd.read_csv("students.csv")

student_data["Result"] = student_data["Marks"].apply(
    lambda marks: "Pass" if marks >= 40 else "Fail"
)

print(student_data)
