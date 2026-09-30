# Program 18: Display complete information about the dataset
import pandas as pd

student_data = pd.read_csv("students.csv")
student_data.info()
