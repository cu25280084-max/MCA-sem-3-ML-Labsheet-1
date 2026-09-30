# Program 31: Save modified dataset as a new CSV file
import pandas as pd

student_data = pd.read_csv("students.csv")

student_data["Result"] = student_data["Marks"].apply(
    lambda marks: "Pass" if marks >= 40 else "Fail"
)

student_data.to_csv("modified_students.csv", index=False)

print("Modified dataset saved successfully.")
