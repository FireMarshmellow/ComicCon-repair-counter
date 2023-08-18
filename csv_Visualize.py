import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/tomas/Documents/GitHub/ComicCon-repair-counter/button_presses.csv')


# Create a pivot table to reshape the data for visualization
pivot_df = df.pivot(index='Hour', columns='Date', values='Count')

# Calculate totals for each day
daily_totals = pivot_df.sum()

# Plot the data
fig, axes = plt.subplots(1, len(pivot_df.columns) + 1, figsize=(18, 6), sharey=True)

for i, column in enumerate(pivot_df.columns):
    axes[i].bar(pivot_df.index, pivot_df[column], label=column)
    axes[i].set_title(f'Date: {column} (Total: {daily_totals[column]})')
    axes[i].set_xlabel('Hour')
    axes[i].grid(True, which='both', linestyle='--', linewidth=0.5)

# Plot the overall total in the last subplot
axes[-1].bar(pivot_df.index, pivot_df.sum(axis=1), color='grey')
axes[-1].set_title(f'Total Overall: {daily_totals.sum()}')
axes[-1].set_xlabel('Hour')
axes[-1].grid(True, which='both', linestyle='--', linewidth=0.5)

axes[0].set_ylabel('Count')
plt.tight_layout()
plt.show()