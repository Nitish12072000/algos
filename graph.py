import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Data
labels = ['TSO', 'TSODE', 'TSOPSO', 'TSOGWO', 'TSOSA', 'TSOOBL', 'TSOLVY']
values = [99.8740, 99.8740, 99.8740, 99.9980, 99.8740, 99.8740, 99.8740]

# Colors (highlight baseline + proposed)
colors = ['gray', 'lightgray', 'lightgray', 'goldenrod', 'lightgray', 'lightgray', 'lightgray']

x = np.arange(len(labels))

plt.figure(figsize=(10,6))
bars = plt.bar(x, values, color=colors, edgecolor='black')

# Y-axis settings
plt.ylim(99, 100)
plt.yticks(np.arange(99, 100.01, 0.2))

# Labels and title
plt.ylabel('Accuracy (%)')

plt.xticks(x, labels, rotation=30)

# Value labels on bars
for bar, val in zip(bars, values):
    plt.text(bar.get_x() + bar.get_width()/2, val + 0.005,
             f'{val:.4f}%', ha='center', fontsize=10, fontweight='bold')

# Legend (top-right)
legend_elements = [
    Patch(facecolor='gray', edgecolor='black', label='Baseline (TSO)'),
    Patch(facecolor='goldenrod', edgecolor='black', label='Proposed (TSOGWO)')
]
plt.legend(handles=legend_elements, loc='upper right')

# Grid
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()