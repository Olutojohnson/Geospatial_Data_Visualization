# Geospatial Data Visualization

This project demonstrates how to visualize and manipulate geospatial data using Python, specifically utilizing the **GeoPandas** library. The workflow includes reading geospatial data, defining a coordinate reference system (CRS), and plotting it on a map.

## Features

- **Data Loading**: Load and visualize geospatial data from an Excel file.
- **Coordinate Reference System (CRS)**: Define the CRS for geospatial data.
- **Point Plotting**: Plot random data points on a map.
- **Shapefile Integration**: Overlay geospatial data on top of a shapefile map (e.g., a country map).
  
## Installation

To install the required libraries, simply run the following command:

```bash
pip install -r requirements.txt
```

## Usage

Follow these steps to visualize your geospatial data:

1. Ensure your data is in an Excel file (`data.xlsx`) with columns for `longitude` and `latitude`.
2. Define the coordinate reference system (CRS). This example uses WGS 84 (EPSG:4326).
3. Load a shapefile (e.g., Nigeria's shapefile) for the map overlay.
4. Use the provided script to generate the plot.

### Example Usage

```python
# Load data from Excel file
data = pd.read_excel('data.xlsx', 'data')

# Create GeoDataFrame with coordinates
geometry = [Point(xy) for xy in zip(data['longitude'], data['latitude'])]
geodata = gpd.GeoDataFrame(data, crs={'init': 'epsg:4326'}, geometry=geometry)

# Load shapefile and plot on map
shapefile = gpd.read_file('shapefile.shp')
geodata.plot_on_map(shapefile)
```

## Example Use Cases

- **Visualizing Random Data Points**: Visualize randomly generated locations on a map, such as cities, landmarks, or points of interest.
- **Geospatial Analysis**: You can easily extend the functionality to perform spatial analysis, such as finding distances between points, or adding other layers of data.

## Customizing the Code

- You can modify the CRS if you're working with a different projection.
- The data visualization can be customized with different color schemes (cmap) or markers.

Feel free to fork this repository, extend the functionality, and adapt the code to suit your specific use cases.