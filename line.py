import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("affinity_logbook.csv")

# Line graph for average overtime hours per position
plt.figure(figsize=(10, 6))
positions = data['Position'].unique()
print(positions)
for position in positions:
    avg_overtime = data[data['Position'] == position].groupby('PayMonth')['OvertimeHours'].mean()
    plt.plot(avg_overtime.index, avg_overtime, label=position)

plt.title('Average Overtime Hours per Position')
plt.xlabel('Month')
plt.ylabel('Average Overtime Hours')
plt.legend(loc='lower right') 
# `’upper left’`, `’upper right’`, `’lower left’`, `’lower right’`, and `’center’`.
plt.grid(True)
plt.show()