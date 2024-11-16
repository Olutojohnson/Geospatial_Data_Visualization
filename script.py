# Import necessary libraries
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

# Load data from an Excel file
data = pd.read_excel('data.xlsx', 'data')

# Define the coordinate reference system (CRS) - WGS 84 (EPSG:4326)
crs = {'init': 'epsg:4326'}

# Create geometry using latitude and longitude from the data
geometry = [Point(xy) for xy in zip(data['longitude'], data['latitude'])]

# Create GeoDataFrame from the data
geodata = gpd.GeoDataFrame(data, crs=crs, geometry=geometry)

# Plot the GeoDataFrame points to check the basic map
geodata.plot()

# Load the shapefile
shapefile = gpd.read_file('shapefile.shp')

# Plot the map and overlay the points
fig, ax = plt.subplots(figsize=(7, 7))
shapefile.plot(ax=ax, facecolor='grey', edgecolor='black', alpha=1, linewidth=1, cmap='cividis')
geodata.plot(ax=ax, color='red', markersize=5)

# Add titles and axis labels
fig.suptitle('Random Locations', fontsize=12)
ax.set_xlabel('Longitude', fontsize=10)
ax.set_ylabel('Latitude', fontsize=10)

# Show the plot
plt.show()
