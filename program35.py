# Program 35: Correlation matrix and heatmap
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

student_data = pd.read_csv("students.csv")

numerical_data = student_data[["Age", "Marks", "Attendance"]]

correlation_matrix = numerical_data.corr()

print("Correlation Matrix:")
print(correlation_matrix)

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Matrix")
plt.show()
