# --------------------------------------------------
# File Name : homework_01_t6.py
# Problem   : Homework 01 - Task 06
# Author    : Worralop Srichainont
# Date      : 2026-01-13
# --------------------------------------------------

import math

# List of point on 2D spaces.
POINTS = [[1, 2], [3, 3], [2, 2], [8, 8], [6, 6], [7, 7], [-3, -3], [-2, -4], [-7, -7]]

# Initialize variables to store distance of each point to each centroids.
point_distances = []

# Initialize variable to store points in each clusters.
clusters = [[], [], []]

# Initialize centroids.
centroids = [[-3, -3], [2, 2], [-7, -7]]

# Repeat process until centroid doesn't change.
for iteration in range(100):
    print(f"========== ITERATION {iteration + 1} ==========")

    # Display centroids
    for idx, [x, y] in enumerate(centroids):
        print(f"Centroid {idx + 1}: ({round(x, 2)}, {round(y, 2)})")
    print()

    # Calculate distance to each centroids, and assign each point to the cluster.
    print("LaTeX script for distances.")
    for point in POINTS:
        # Calculate distance to each centroids.
        x, y = point
        distances = []
        for idx, centroid in enumerate(centroids):
            xc, yc = centroid
            distances.append(math.sqrt(((xc - x) ** 2) + ((yc - y) ** 2)))
        point_distances.append(distances)

        # Assign each point to the cluster.
        cluster_idx = distances.index(min(distances))
        clusters[cluster_idx].append(point)

        # Print LaTeX scripts
        print(
            " & ".join(f"{dist:.2f}" for dist in distances)
            + f" & Cluster {cluster_idx + 1}"
        )
    print()

    # Display points in each cluster, and re-calculate new centroids.
    new_centroids = []
    for idx, cluster in enumerate(clusters):
        print(
            f"Cluster {idx + 1}: {', '.join(f'({round(_x, 2)}, {round(_y, 2)})' for _x, _y in cluster)}"
        )

        # Re-calculate new centroids.
        mean_x = 0.0
        mean_y = 0.0

        for x, y in cluster:
            mean_x += float(x)
            mean_y += float(y)

        mean_x /= len(cluster)
        mean_y /= len(cluster)
        new_centroids.append([mean_x, mean_y])
    print()

    # Display new centroids
    for idx, [x, y] in enumerate(new_centroids):
        print(f"New centroid {idx + 1}: ({round(x, 2)}, {round(y, 2)})")
    print()

    # Stop condition
    if centroids == new_centroids:
        break

    # Reset variables
    centroids = new_centroids.copy()
    point_distances = []
    clusters = [[], [], []]
