# Program 34: Create a scatter plot
import pandas as pd
import matplotlib.pyplot as plt

student_data = pd.read_csv("students.csv")

plt.scatter(
    student_data["Attendance"],
    student_data["Marks"]
)

plt.title("Attendance vs Marks")
plt.xlabel("Attendance")
plt.ylabel("Marks")
plt.show()
