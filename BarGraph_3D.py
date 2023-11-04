import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
# Define the names and scores of the participants
sorted_names = ["Callum", "Yuzu", "Sparkie", "Geo", "Caff", "Cummy", "Mores", "Ruru"]
sorted_scores = [
    [43, 87, 100, 87, 63, 83, 57, 93, 90],
    [97, 63, 100, 80, 100, 93, 83, 80, 10],
    [93, 97, 80, 60, 83, 77, 97, 70, 100],
    [67, 53, 73, 43, 60, 67, 90, 63, 93],
    [67, 80, 100, 63, 97, 73, 80, 27, 100],
    [67, 77, 40, 83, 73, 90, 80, 77, 70],
    [47, 73, 53, 67, 70, 63, 93, 50, 47],
    [83, 70, 47, 37, 57, 50, 57, 13, 100]
]
# Define the types of intelligences
intelligences = ["Linguistic", "Logical-mathematical", "Musical", "Bodily-kinesthetic", "Spatial-Visual", "Inter-personal", "Intra-personal", "Naturalistic", "Existential"]
# Define the colors for each participant
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "pink"]
# Create a 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# Plot the bars for each participant and each type of intelligence
for i in range(len(sorted_names)):
    # Get the x and y coordinates for the bars
    x = np.arange(len(intelligences))
    y = np.full(len(intelligences), i)
    # Get the z values (scores) for the bars
    z = np.array(sorted_scores[i])
    # Plot the bars with the corresponding color and label
    ax.bar3d(x, y, np.zeros(len(intelligences)), 1, 1, z, color=colors[i], alpha=1, label=sorted_names[i])
# Get the average scores for each type of intelligence
avg_scores = np.mean(sorted_scores, axis=0)
# Plot the average line with a higher z value to make it appear above the bars
ax.plot(x, np.full(len(intelligences), len(sorted_names) + 1), avg_scores, color="black", linewidth=3, label="Average", zorder=10)
# Set the ticks and labels for the x and y axes
ax.set_xticks(x)
ax.set_xticklabels(intelligences, rotation=90, fontsize=10)
ax.set_yticks(np.arange(len(sorted_names)))
ax.set_yticklabels(sorted_names, rotation=90, fontsize=10)
# Set the label for the z axis
ax.set_zlabel("Score")
# Set the title for the figure
ax.set_title("3D Data Visualization for Multiple Participants in an Intelligence Test")
# Show the legend
ax.legend()
# Show the figure
plt.show()
