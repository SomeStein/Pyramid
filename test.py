import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Example sequence and corresponding points
sequence = [0, 1, 2, 1, 0, 2, 2, 0, 1, 3, 3, 4, 4]
points = [
    (1, 2, 3),
    (2, 3, 4),
    (3, 4, 5),
    (4, 5, 6),
    (5, 6, 7),
    (6, 7, 8),
    (7, 8, 9),
    (8, 9, 10),
    (9, 10, 11),
    (10, 11, 12),
    (11, 12, 13),
    (12, 13, 14),
    (13, 14, 15)
]

# Define a colormap with up to 13 different colors
colormap = {
    0: 'red',
    1: 'green',
    2: 'blue',
    3: 'yellow',
    4: 'cyan',
    5: 'magenta',
    6: 'orange',
    7: 'purple',
    8: 'brown',
    9: 'pink',
    10: 'gray',
    11: 'olive',
    12: 'navy'
}

# Convert sequence to colors
colors = [colormap[number] for number in sequence]

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Extract x, y, z coordinates
x_coords = [point[0] for point in points]
y_coords = [point[1] for point in points]
z_coords = [point[2] for point in points]

# Scatter plot with colors
ax.scatter(x_coords, y_coords, z_coords, c=colors, marker='o')

# Add lines connecting points of the same color
for color_index in colormap.keys():
    # Get indices of points with the current color
    indices = [i for i, val in enumerate(sequence) if val == color_index]
    if len(indices) > 1:
        for i in range(len(indices) - 1):
            idx1 = indices[i]
            idx2 = indices[i + 1]
            ax.plot(
                [x_coords[idx1], x_coords[idx2]],
                [y_coords[idx1], y_coords[idx2]],
                [z_coords[idx1], z_coords[idx2]],
                color=colormap[color_index]
            )

# Add labels for clarity
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
