import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plot_mean_median(ax, data, color, label):
    ax.bar(['Mean', 'Median'], [np.mean(data), np.median(data)], color=color, alpha=0.7, label=label)
    ax.legend()

def plot_histogram(ax, data, color, label):
    ax.hist(data, bins=15, color=color, alpha=0.7, label=label)
    ax.legend()

def plot_scatter(ax, x, y):
    ax.scatter(x, y, alpha=0.7)
    ax.set_xlabel('Variable 1')
    ax.set_ylabel('Variable 2')
    ax.set_title('Scatter Plot of Variable 1 vs Variable 2')

# Generate random data
np.random.seed(0)
data = np.random.randn(100, 2)
variable_1 = data[:, 0]
variable_2 = data[:, 1]

# Create subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Plot Descriptive Statistics
plot_mean_median(axes[0, 0], variable_1, 'blue', 'Variable 1')
plot_mean_median(axes[0, 0], variable_2, 'green', 'Variable 2')
axes[0, 0].set_title('Descriptive Statistics: Mean and Median')

# Plot Correlation Analysis
sns.heatmap(np.corrcoef(data.T), annot=True, ax=axes[0, 1])
axes[0, 1].set_title('Correlation Analysis')

# Plot Histogram of Variables
plot_histogram(axes[1, 0], variable_1, 'blue', 'Variable 1')
plot_histogram(axes[1, 0], variable_2, 'green', 'Variable 2')
axes[1, 0].set_title('Histogram of Variables')

# Plot Scatter Plot of Variables
plot_scatter(axes[1, 1], variable_1, variable_2)

# Adjust layout and display plot
plt.tight_layout()
plt.show()
