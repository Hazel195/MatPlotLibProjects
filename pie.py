import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("affinity_logbook.csv")

# Pie chart for count of each position
position_count = data['Position'].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(position_count, labels=position_count.index, autopct='%1.1f%%', startangle=140)
plt.title('Count of Employees by Position')
plt.axis('equal')
plt.show()