# Program 5: Create a simple line plot
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
marks = [55, 62, 68, 74, 81]

plt.plot(days, marks, marker="o")
plt.title("Devesh's Marks Progress")
plt.xlabel("Test Number")
plt.ylabel("Marks")
plt.show()
