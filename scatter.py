import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("affinity_logbook.csv")

# Scatter plot for relationship between overtime hours and salary
plt.figure(figsize=(10, 6))
plt.scatter(data['OvertimeHours'], data['BaseSalary'], color='orange', alpha=0.5)
plt.title('Relationship between Overtime Hours and Salary')
plt.xlabel('Overtime Hours')
plt.ylabel('Base Salary')
plt.grid(True)
plt.show()