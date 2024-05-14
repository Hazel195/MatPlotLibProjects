import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("affinity_logbook.csv")

# Bar chart for richest salary per position
richest_salary = data.groupby('Position')['BaseSalary'].max()

plt.figure(figsize=(10, 6))
plt.bar(richest_salary.index, richest_salary, color='skyblue')
plt.title('Richest Salary per Position')
plt.xlabel('Position')
plt.ylabel('Salary')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()