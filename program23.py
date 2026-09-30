# Program 23: Rename one or more columns
import pandas as pd

student_data = pd.read_csv("students.csv")

student_data.rename(
    columns={
        "Marks": "Exam_Marks",
        "Attendance": "Attendance_Percentage"
    },
    inplace=True
)

print(student_data.head())
