# Program 22: Count frequency of unique values
import pandas as pd

student_data = pd.read_csv("students.csv")

city_frequency = student_data["City"].value_counts()

print("Frequency of each city:")
print(city_frequency)
