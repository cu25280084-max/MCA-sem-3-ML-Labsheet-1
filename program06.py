# Program 6: Generate a basic statistical plot using Seaborn
import seaborn as sns
import matplotlib.pyplot as plt

marks = [55, 62, 68, 74, 81, 69, 72, 88, 76, 64]

sns.histplot(marks, kde=True)
plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()
