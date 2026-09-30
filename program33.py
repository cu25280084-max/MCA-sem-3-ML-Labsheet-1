# Program 33: Create a histogram using Matplotlib
import pandas as pd
import matplotlib.pyplot as plt

student_data = pd.read_csv("students.csv")

plt.hist(student_data["Marks"], bins=5, edgecolor="black")
plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()
