  # Paste your Python script inside these triple quotes
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KernelDensity
from sklearn.model_selection import GridSearchCV

# Load coordinates data
df = pd.read_csv("crim_analyzed.csv")  # Replace with your actual file path
coordinates = df[["LONGITUDE", "LATITUDE"]].dropna()

# Optimize bandwidth for KDE
params = {"bandwidth": np.linspace(0.001, 0.01, 20)}
grid = GridSearchCV(KernelDensity(kernel="gaussian"), params)
grid.fit(coordinates)

best_kde = grid.best_estimator_
print(f"Best bandwidth: {grid.best_params_['bandwidth']}")

# Create a grid covering the geographic area
xmin, xmax = coordinates["LONGITUDE"].min(), coordinates["LONGITUDE"].max()
ymin, ymax = coordinates["LATITUDE"].min(), coordinates["LATITUDE"].max()

xx, yy = np.meshgrid(np.linspace(xmin, xmax, 100), np.linspace(ymin, ymax, 100))
grid_points = np.vstack([xx.ravel(), yy.ravel()]).T

# Calculate density scores for the grid
log_density = best_kde.score_samples(grid_points)
density = np.exp(log_density).reshape(xx.shape)

# Threshold for high-risk areas (top 10% density)
threshold = np.percentile(density, 90)
high_risk = np.where(density > threshold)

# Get coordinates of high-risk areas
high_risk_coords = grid_points[high_risk[0]]
print(f"High-risk areas (longitude, latitude):\n {high_risk_coords}")

# Ask user for input method
input_method = input("Do you want to input a new observation manually or from a file? (manual/file): ").strip().lower()

if input_method == "manual":
    new_longitude = float(input("Enter the longitude of the new observation: "))
    new_latitude = float(input("Enter the latitude of the new observation: "))
    new_observation = np.array([[new_longitude, new_latitude]])  
elif input_method == "file":
    new_observations_file = input("Enter the path to the file containing new observations: ")
    new_observations = pd.read_csv(new_observations_file)
    new_observation = new_observations[["LONGITUDE", "LATITUDE"]].values
else:
    raise ValueError("Invalid input method. Choose 'manual' or 'file'.")

log_density_new = best_kde.score_samples(new_observation)
density_new = np.exp(log_density_new)

# Check if the new observation(s) is in a high-risk area
for i, (lon, lat) in enumerate(new_observation):
    print(f"Crime Density for observation {i+1} ({lon}, {lat}): {density_new[i]}")
    if density_new[i] > threshold:
        print("This location is in a high-risk area for crime.")
    else:
        print("This location is not in a high-risk area for crime.")

# Plot the results
plt.figure(figsize=(12, 8))
plt.scatter(coordinates["LONGITUDE"], coordinates["LATITUDE"], s=5, c="red", alpha=0.1)
plt.contourf(xx, yy, density, levels=50, cmap="Reds", alpha=0.6)
plt.colorbar(label="Crime Density")
plt.scatter(new_observation[:, 0], new_observation[:, 1], s=100, c="blue", marker="x", label="New Observation")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Crime Hotspots with New Observation")
plt.legend()
plt.show()
