import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plot_descriptive_statistics(ax, data, colors, labels):
    means = np.mean(data, axis=0)
    medians = np.median(data, axis=0)
    bar_positions = np.arange(len(means))

    for i in range(data.shape[1]):
        ax.bar(bar_positions + 0.2 * i, [means[i], medians[i]], color=colors[i], alpha=0.7, label=labels[i])

    ax.set_xticks(bar_positions + 0.2)
    ax.set_xticklabels(['Mean', 'Median'])
    ax.legend()
    ax.set_title('Descriptive Statistics: Mean and Median')

def plot_correlation_analysis(ax, data):
    sns.heatmap(np.corrcoef(data.T), annot=True, ax=ax)
    ax.set_title('Correlation Analysis')

def plot_histogram(ax, data, colors, labels):
    ax.hist(data, bins=15, color=colors, alpha=0.7, label=labels)
    ax.legend()
    ax.set_title('Histogram of Variables')

def plot_scatter(ax, x, y):
    ax.scatter(x, y, alpha=0.7)
    ax.set_xlabel('Variable 1')
    ax.set_ylabel('Variable 2')
    ax.set_title('Scatter Plot of Variable 1 vs Variable 2')

# Generate random data
np.random.seed(0)
data = np.random.randn(100, 2)

# Create subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Plot Descriptive Statistics
plot_descriptive_statistics(axes[0, 0], data, ['blue', 'green'], ['Variable 1', 'Variable 2'])

# Plot Correlation Analysis
plot_correlation_analysis(axes[0, 1], data)

# Plot Histogram of Variables
plot_histogram(axes[1, 0], [data[:, 0], data[:, 1]], ['blue', 'green'], ['Variable 1', 'Variable 2'])

# Plot Scatter Plot of Variables
plot_scatter(axes[1, 1], data[:, 0], data[:, 1])

# Adjust layout and display plot
plt.tight_layout()
plt.show()
